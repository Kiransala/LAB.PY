"""THIS IS 'main.py' FILE"""

from exp92 import subtraction,multiply,divide
from x.exp91 import addition

user = False
while not user:
    choice = int(
        input("\n\n1.Addition\n2.Subtraction \n3.Mltiplication\n4.Division\n5.Exit\nEnter the choice: "))
    if choice == 1:
        n=int(input("No-of inputs: "))
        if n == 3:
          a=int(input("Enter a number a: "))
          b=int(input("Enter a number b: "))
          c=int(input("Enter a number c: "))
          print(f"Answer for Addition: {addition(a,b,c)}")
        elif n == 2:
          a=int(input("Enter a number a: "))
          b=int(input("Enter a number b: "))
          print(f"Answer for Addition: {addition(a,b)}")
        else:
          print("Enter a valid choice")

    elif choice == 2:
      a=int(input("Enter a number a: "))
      b=int(input("Enter a number b: "))
      print(f"Answer for Subtraction: {subtraction(a,b)}")


    elif choice == 3:
      a=int(input("Enter a number a: "))
      b=int(input("Enter a number b: "))
      print(f"Answer for Multiplication: {multiply(a,b)}")
        
    elif choice == 4:
      a=int(input("Enter a number a: "))
      b=int(input("Enter a number b: "))
      print(f"Answer for Division: {divide(a,b)}")

    elif choice == 5:
      print("Exited")
      user = True
        
    else:
        print("Enter a valid choice")
        
        
"""THIS IS 'exp91.py' INSIDE A FILE NAME 'x' """
def addition(a=None,b=None,c=None):
	if a!=None and b!=None and c!=None:
		return a+b+c
	elif a!=None and b!=None:
		return a+b

"""THIS IS 'exp92.py' FILE"""

def subtraction(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
