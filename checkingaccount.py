class CheckingAccount:

    #constructor

    def __init__(self,name,address,accountnumber,balance):

        #private variable by using __

        self.__name = name;

        self.__address = address

        self.__accountNumber = accountnumber

        self.__balance = balance

#perform credit operation on the account

def creditAccount(self,amount):

        self.__balance = self.__balance + amountfrom CheckingAccount import CheckingAccount

# this is how creating a new bank user is done
user = CheckingAccount("Ravi", "New Delhi, India", "564656156549", 2000)

# print a menu
print("1-Debit")
print("2-Credit")
print("3-View Balance")
print("q-Quit")
while True:
    # read user choice and execute corresponding method
    choice = input("Enter Choice : ")
    if choice == "1":
        amount = int(input("Enter Amount : "))
        user.debit(amount)
    elif choice == "2":
        amount = int(input("Enter Amount : "))
        user.credit(amount)
    elif choice == "3":
        user.view_balance()
    else:
        break