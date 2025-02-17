 OOP learning tst

    Encapsulation  concepts

class BankAccount:
    def __init__ (self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient funds")

    def get_balance(self):
        return self.balance
    
    def __str__ (self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
    

account = BankAccount("foncy", 10000)
account.withdraw(9000000002)
print(account.owner)
print(account.get_balance())





  Inheritance concepts

class Animals:
    def __init__ (self,name):
        self.name = name
    def make_sound(self):
        return  "some sound"

class Dog(Animals):
    def make_sound(self):
        return "Bark"
    
class Cat(Animals):
    def make_sound(self):
        return "Meow"
    
dog = Dog("Rex")   
cat = Cat("kitty") 
print(dog.name)
print(dog.make_sound())
print(cat.name)
print(cat.make_sound())


   Polymorphism concepts

class Birds:
    def sound(self):
        return "chirp"
    
class Cat:
    def sound(self):
        return "Meow"
    
for animals in (Birds(), Cat()):
    print(animals.sound())


#   Abstraction concepts

