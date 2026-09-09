
class backpack:
    def __init__(self,color, size, material):
        self.color=color 
        self.size=size
        self.material=material

    def open(self):
            print("the backpack is open")

    def describe(self):
            print(f"the backpack is made with {self.material}")

#create miltiple instances using the class "backpack"
backpack1=backpack("black", "14in","cotton")
backpack2=backpack("white", "16in","polyester")

print(backpack1.material)
print(backpack2.material)
backpack1.describe()
backpack2.describe()

#Lab1. Bank Account Class

class BankAccount:
    def __init__(self,holder,curr_balance):
        self.holder=holder
        self.__balance = curr_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance= self.balance - amount 
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print("Current balance:", self.__balance)



raul = BankAccount("Raúl Pérez", 5000)
joel = BankAccount("Joel López", 3000)



print("Account holder:", raul.holder)
raul.check_balance()

raul.deposit(1000)
raul.withdraw(500)

print("Updated balance:")
raul.check_balance()



print("\nAccount holder:", joel.holder)
joel.check_balance()

joel.deposit(500)
joel.withdraw(200)

print("Updated balance:")
joel.check_balance()

         
         
         