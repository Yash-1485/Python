class Calculator:
    def getData(self):
        self.n1=int(input("Enter Number 1: "))
        self.n2=int(input("Enter Number 2: "))
    def addition(self):return self.n1+self.n2
    def subtraction(self):return self.n1-self.n2
    def multiplication(self):return self.n1*self.n2
    def division(self):return self.n1/self.n2
    def modulation(self):return self.n1%self.n2
    def power(self):return self.n1**self.n2
obj=Calculator()
while True:
    print("""
          ---------------------------
          Press 1 for Addition
          Press 2 for Subtraction
          Press 3 for Multiplication
          Press 4 for Division
          Press 5 for Modulation
          Press 6 for Power
          Press 7 for Exit
          ---------------------------          
          """)
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        obj.getData()
        print('Addition of two numbers {0} and {1} is {2}'.format(obj.n1,obj.n2,obj.addition()))
    elif choice==2:
        obj.getData()
        print('Subtraction of two numbers {0} and {1} is {2}'.format(obj.n1,obj.n2,obj.subtraction()))
    elif choice==3:
        obj.getData()
        print('Multiplication of two numbers {0} and {1} is {2}'.format(obj.n1,obj.n2,obj.multiplication()))
    elif choice==4:
        obj.getData()
        print('Division of two numbers {0} and {1} is %.2f'.format(obj.n1,obj.n2) %obj.division())
    elif choice==5:
        obj.getData()
        print('Modulation of two numbers {0} and {1} is {2}'.format(obj.n1,obj.n2,obj.modulation()))
    elif choice==6:
        obj.getData()
        print('Power for number {0} raised to {1} is {2}'.format(obj.n1,obj.n2,obj.power()))
    elif choice==7:
        break
    else:
        print('Invalid choice')