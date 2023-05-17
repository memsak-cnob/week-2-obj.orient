#import the class

from CheckingAccount import CheckingAccount

#create an object of CheckingAccount

account1 = CheckingAccount("Mike Whipreck","Hull Ave",7645,76.4)

#perform operation as credit and debit

account1.creditAccount(63.80)

account1.debitAccount(430.00)

account1.debitAccount(12.00)

#show the balance of the account

account1.showBalance()