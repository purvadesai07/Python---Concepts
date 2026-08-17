class Account:
    def __init__(self):
        self.name = ""
        self.acct_no = 0
        self.balance = 2000
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawal Successful!!")
        else:
            print("Insufficient Bank Balance!")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited Successfully!!")
    def input_data(self):
        self.name = input("Enter Name: ")
        self.acct_no = int(input("Enter Account No: "))
    def print_info(self):
        print("ACCOUNT DETAILS")
        print("Owner of the Account: ", self.name)
        print("Account No: ", self.acct_no)
        print("Total Balance: ",self.balance)
acc1 = Account()
acc1.input_data()
acc1.deposit(1000)
acc1.withdraw(500)
acc1.print_info()

            