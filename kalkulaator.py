#Varuskin IS22

import math

class Calculator:
   def __init__(self, num1, num2):
       self.num1 = num1
       self.num2 = num2


   def add(self): # liitmine
       return self.num1 + self.num2


   def subtract(self): # lahutamine
       return self.num1 - self.num2


   def multiply(self): # korrutamine
       return self.num1 * self.num2


   def divide(self): # jagamine
       return self.num1 / self.num2


   def exponent(self): # eksponent
       return self.num1 ** self.num2


   def residue(self): # jääk
       return self.num1 % self.num2



# Küsib kasutajalt arvutatavat
num1 = float(input("Sisesta esimene number: "))
num2 = float(input("Sisesta teine number: "))


# Tekitab kalkulaatori objekti sisestatud numbritega
calculator = Calculator(num1, num2)


# Annab kasutajale valikud tehte tegemiseks
print("1. Liitmine")
print("2. Lahutamine")
print("3. Kordamine")
print("4. Jagamine")
print("5. Eksponent")
print("6. jääk")


# Küsib kasutajalt millist varianti soovib
choice = int(input("Vali sobiv (1,2,3,4,5,6): "))


# Teeb tehte kasutaja valitud variandile vastavalt
if choice == 1:
   result = calculator.add()
elif choice == 2:
   result = calculator.subtract()
elif choice == 3:
   result = calculator.multiply()
elif choice == 4:
   result = calculator.divide()
elif choice == 5:
   result = calculator.exponent()
elif choice == 6:
   result = calculator.residue()
# Prindib "Viga" kui kasutaja midagi muud peale 1-6 sisestab
else:
   print("Viga")
   result = None


# Prindib kasutajale vastuse
if result is not None:
   print("Vastus:", result)