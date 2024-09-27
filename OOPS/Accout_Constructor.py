class Accout:
    name=''
    acType=''
    balance=0
    
    def __init__(self,name,acType,balance):
        self.name=name
        self.acType=acType
        self.balance=balance
    def withdraw(self,amount=0):
        amount=float(input('Enter amount to withdraw: '))
        if amount<=0 or amount>=self.balance:
            print('Invalid amount')
        elif self.acType=='Savings' and self.balance-amount==1000:
            print('For \'Savings\' account type, minimum required acoount balance is Rs.1000')
            print(f'Clear balance is: {self.balance}')
        else:
            self.balance-=amount
            print(f'Withdraw amount is {amount}')
            print(f'Clear balance is: {self.balance}')
    def deposit(self,amount=0):
        amount=float(input('Enter amount to deposit: '))
        if amount<=0:
            print('Invalid amount')
        else:
            self.balance+=amount
            print(f'Deposit amount is {amount}')
            print(f'Clear balance is: {self.balance}')
    def account_details(self):
        print(f'''
              --------------------------------------
              | Name: {self.name}                  |
              | Account Type: {self.acType}        |
              | Clear Balance: Rs.{self.balance}   |
              --------------------------------------
              ''')
ac=Accout('Yash','Current',15000000)

while True:
    print("""
        -------------------------------
        Press 1 to see Account Details
        Press 2 to withdraw amount
        Press 3 to deposit amount
        Press 4 to exit
        -------------------------------
          """)
    choice=int(input('Enter your choice: '))
    
    if choice==1:
        ac.account_details()
    elif choice==2:
        ac.withdraw()
    elif choice==3:
        ac.deposit()
    elif choice==4:
        break
    else:
        print('Invalid choice')