def factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial*i    
    print("Factorial %d is: %d." %(number,factorial))
    

def palindrome(string):
    reversed = ""
    for i in range(len(string), 0, -1):
        reversed += string[i-1]
    if string == reversed:
        print("It's a palindrome number.")
    else:
        print("It's not a palindrome number.")
        
        
user = False
while not user:
    choice = input("1.Palindrome\n2.Factorial\n3.stop\nEnter a choice to find?\n").lower()
    if choice == "factorial":
        number = int(input("Enter a number: "))  
        factorial(number)
        print("_____________________________________________\n")
    elif choice == "palindrome":
        a_string = input("Enter a string: ")
        palindrome(a_string)
        print("_____________________________________________\n")
    elif choice == "stop":
        user = True
    else:
        print("Enter a valid choice.\n")