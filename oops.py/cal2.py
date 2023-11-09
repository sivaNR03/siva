class calculation():
    def __init__(self):
        self.result = 0
    def sum (self,num1,num2):
        self.sum =(num1+num2)
    def subtract(self,num1,num2):
        self.subtract =(num1-num2)
    def product(self,num1,num2):
        self.product =(num1*num2)
    def divide(self,num1,num2):
        if num2 !=0:
           self.divide = (num1/num2)
        else:
            print("error: divide by  zero ")  

def main():
       calculator = calculation()

       while True:
           print("current result:",calculator.result)
           print("1. sum")
           print("2.subtract")
           print("3.product")
           print("4 divide")
           print("5. exit")


           choice = input("enter the number(1/2/3/4/5):")
           if choice == '1':
              num1 = float(input("Enter the first number: "))
              num2 = float(input("Enter the second number: "))
              calculator.sum(num1, num2)
           elif choice == '2':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                calculator.subtract(num1, num2)
           elif choice == '3':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                calculator.divide(num1, num2)

           elif choice == '4':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                calculator.divide(num1, num2)
           elif choice == '5':
                break
           else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()






             

    