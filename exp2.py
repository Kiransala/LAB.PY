def factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i    
    print(f"Factorial of {number} is: {factorial}")

def palindrome(string):  
  if(string==string[::-1]):  
      print("The letter is a palindrome")  
  else:  
      print("The letter is not a palindrome") 

user = False
while not user:
    choice = int(input("\n\n1.Factorial\n2.Palindrome\n3.Exit\nEnter your choice of operations : "))
    if choice == 1:
        number = int(input("Enter a number: "))  
        factorial(number)
    elif choice == 2:
        a_string = input("Enter a string: ")
        palindrome(a_string)
    elif choice == "exit":
        user = True
    else:
        print("Enter a valid choice.\n")
