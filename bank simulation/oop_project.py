from bank_aaccount import *

Deepak = BankAccount(1000, "Deepak")
Jivan = BankAccount(2000, "jivan")

Deepak.getBalance()
Jivan.getBalance()

Deepak.deposit(500)
Jivan.deposit(500)

Deepak.withdraw(100)
Jivan.withdraw(100)

Deepak.transferMoney(100, Jivan)

Binod = InterestRewardsAcct(1000, "Binod")
Binod.getBalance()
Binod.deposit(100)
Binod.transferMoney(100, Deepak)

Samir = SavingAcc(1000, "Samir")
Samir.getBalance()
Samir.deposit(100)
Samir.transferMoney(1000, Deepak)