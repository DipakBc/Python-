import pwinput
import sqlite3
import os
from cryptography.fernet import Fernet
import bcrypt
import csv

# Key Management
def load_key():
    """Load or generate encryption key"""
    key_path = "secret.key"
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            return key_file.read()
    
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        os.chmod(key_path, 0o600)
        key_file.write(key)
    return key

key = load_key()
cipher = Fernet(key)

# Database Functions
def initialize_database():
    """Create database and tables if they don't exist"""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    
    # Create master table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS master (
            id INTEGER PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)
    
    # Create credentials table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            UNIQUE(service, username)
        )
    """)
    
    conn.commit()
    conn.close()

# Password Encryption
def encrypt_password(password):
    """Encrypt password using Fernet"""
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Decrypt password using Fernet"""
    return cipher.decrypt(encrypted_password.encode()).decode()

# Master Password Functions
def set_master_password():
    """Set the master password with validation"""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    
    while True:
        master_password = pwinput.pwinput("Set a master password (min 8 chars): ", mask="*")
        if len(master_password) < 8:
            print("❌ Password must be at least 8 characters")
            continue
        
        confirm = pwinput.pwinput("Confirm master password: ", mask="*")
        if master_password != confirm:
            print("❌ Passwords don't match!")
            continue
        
        hashed_password = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())
        cursor.execute("INSERT INTO master (password) VALUES (?)", (hashed_password,))
        conn.commit()
        print("✅ Master password set successfully!")
        break
    
    conn.close()

def verify_master_password():
    """Verify the master password"""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    
    # Check if master table exists and has a password
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='master'")
    if not cursor.fetchone():
        conn.close()
        print("No master password set. Please set one first.")
        set_master_password()
        return True
    
    cursor.execute("SELECT password FROM master LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        print("No master password set. Please set one first.")
        set_master_password()
        return True
    
    attempts = 3
    while attempts > 0:
        entered_password = pwinput.pwinput(f"Enter master password ({attempts} attempts remaining): ", mask="*")
        if bcrypt.checkpw(entered_password.encode(), result[0]):
            return True
        attempts -= 1
        print("❌ Incorrect password!")
    
    print("⛔ Too many failed attempts!")
    return False

# Password Management
def add_password(service, username, password):
    """Add a new password entry"""
    try:
        encrypted_password = encrypt_password(password)
        conn = sqlite3.connect("passwords.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO credentials (service, username, password)
            VALUES (?, ?, ?)
        """, (service, username, encrypted_password))
        
        conn.commit()
        print(f"✅ Password saved for {service}")
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()

def get_password(service, username):
    """Retrieve a password"""
    try:
        conn = sqlite3.connect("passwords.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT password FROM credentials 
            WHERE service = ? AND username = ?
        """, (service, username))
        
        result = cursor.fetchone()
        if result:
            decrypted_password = decrypt_password(result[0])
            print(f"🔑 Service: {service}\n👤 Username: {username}\n🔐 Password: {decrypted_password}")
        else:
            print(f"❌ No password found for {service} with username {username}")
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()

def delete_password(service, username):
    """Delete a password entry"""
    try:
        conn = sqlite3.connect("passwords.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM credentials 
            WHERE service = ? AND username = ?
        """, (service, username))
        
        conn.commit()
        print(f"🗑️ Deleted password for {service} with username {username}")
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()

# Main Application
def main():
    """Main program flow"""
    # Initialize database and tables
    initialize_database()
    
    # Verify or set master password
    if not verify_master_password():
        print("Exiting due to authentication failure")
        return
    
    # Main menu
    while True:
        print("\n🔒 Password Manager 🔒")
        print("1. Add password")
        print("2. Get password")
        print("3. Delete password")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            service = input("Service name: ")
            username = input("Username: ")
            password = pwinput.pwinput("Password: ", mask="*")
            add_password(service, username, password)
        
        elif choice == "2":
            service = input("Service name: ")
            username = input("Username: ")
            get_password(service, username)
        
        elif choice == "3":
            service = input("Service name: ")
            username = input("Username: ")
            delete_password(service, username)
        
        elif choice == "4":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()