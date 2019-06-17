# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:07:28 2019

@author: Aryan Kumar
"""


print ("Hello World")



# programs in python demonstrating various OOP concepts such as encapsulation and inheritance

class employee:
    name="raj";
    
    def display(x):
        print("Name is ",x.name);
        
e=employee()
print(e.name)
e.display();

class dog:
    name='Tiger'
    legs=4
    color="red"
    breed="German shepard"
    
    def display(x):
        print("Dogs name is:",x.name,"\n","It has ",x.legs,"legs",'\n',"Its color is",x.color,'\n',"its breed is",x.breed);
        print("It has ",x.legs,"legs");
        print("Its color is",x.color);
        print("its breed is",x.breed);
d=dog()
d.display();
        



#A simple bank demo using class concepts
class bank:
    amount=0;
    
    def deposit(self):
        print("Enter the deposit amount:")
        dep=int(input())
        self.amount += dep
    
    def withdraw(self):
        print("Enter the amount:")
        draw=int(input());
        if draw >=self.amount:
            print ("Insufficient Balance")
        else : 
            self.amount=self.amount-draw
            print("amount withdrawn successfully!")
            print("Remaining Balance: ",self.amount)
    def check_balance(self):
        print("The current balance is: ",self.amount)
            
b=bank()

b.check_balance()
b.deposit()
b.check_balance()
b.withdraw()
b.check_balance
b.withdraw()

while (1):
    print("Enter your choice:",'\n',"1.Check Balance",'\n',"2.Deposit",'\n',"3.Withdraw")
    x=int(input())
    
    if x==1:
        b.check_balance()
    
    elif x==2:
        b.deposit()

    elif x==3:
        b.withdraw()

    else:
        exit
              

# single inheritance
class Human:
    def __init__(self):
        print("I'm a human")
        
    def Live(self):
        print("I live on earth")
        
class Name(Human):
    def Aryan(self):
        print("my name is Aryan")
        
nam=Name()
nam.Live()
nam.Aryan()


# Multilevel Inheritance
class Human:
    def __init__(self):
        print("I'm a human")
        
    def Live(self):
        print("I live on earth")
        
class Name(Human):
    def Aryan(self):
        print("my name is Aryan")
        
class Gender(Name):
    def MyGender(self):
        print("Male")

g=Gender()
g.Live()
g.Aryan()
g.MyGender()


# Multiple Inheritance
class Human:
    def __init__(self):
        print("I'm a human")
        
    def Live(self):
        print("I live on earth")
        
class Name():
    def Aryan(self):
        print("my name is Aryan")
        
class Gender(Name,Human):
    def MyGender(self):
        print("Male")

g=Gender()
g.Live()
g.Aryan()
g.MyGender()


# Heriarchy Inheritance
class Human:
    def __init__(self):
        print("I'm a human")
        
    def Live(self):
        print("I live on earth")
        
class Name(Human):
    def Aryan(self):
        print("my name is Aryan")
        
class Gender(Human):
    def MyGender(self):
        print("Male")

g=Gender()
nam=Name()
nam.Aryan()
g.Live()
g.MyGender()


#Method Overriding
class Human:
    def __init__(self):
        print("I'm a human")
        
    def Live(self):
        print("I live on earth")
        
class Name(Human):
    def Aryan(self):
        super().Live()
        print("my name is Aryan")
        
nam=Name()
nam.Aryan()

 
#Method resolution
class Human:
    def __init__(self):
        print("I'm a human")
        
    def Live(self):
        print("I live on earth")
        
class Name():
    def Live(self):
        print("Hulu bulu")
        
    def Aryan(self):
        print("my name is Aryan")
#here names Live() is given preference over Human's Live() due to method resolution        
class Gender(Name,Human):
    def MyGender(self):
        super().Live
        print("Male")

g=Gender()
g.Live()
g.Aryan()
g.MyGender()

# mall demo using inheritence concept
import sys

class Mall:
    products={}
    def store_Product(self,name,price):   
        self.products[name]=price

        
class Worker(Mall):
    def add_product(self):
        print("Enter the product name: ")
        name=input()
        print("Enter the price: ")
        price=float(input())
        super().store_Product(name,price)

class Customer(Mall):
    def enquire(self):
        search=input("Enter the product you are looking for: ")
        if search in c.products:
            print(search," ",c.products[search])           
            

w=Worker()
c=Customer()
            
while (1):
    print("Enter your choice:",'\n',"1.Worker",'\n',"2.Customer")
    x=int(input())
    
    if x==1:
        w.add_product()
    
    elif x==2:
        c.enquire()
        
    else:
        sys.exit()      
'''
