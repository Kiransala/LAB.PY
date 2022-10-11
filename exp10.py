import random

class NumTooLargeError(Exception):
    def __init__(self,msg):
        self.msg=msg
class NumTooSmallError(Exception):
    def __init__(self,msg):
        self.msg=msg
    
num = random.randint(1,100)
count = 0
while True:
    count += 1
    try:
        inum = int(input("Enter a number: "))
        if inum < num:
            raise NumTooSmallError("Enter a Greater number")
            
        elif inum > num:
            raise NumTooLargeError("Enter a Smaller number")
        else:
            break
    except NumTooSmallError as me:
        print(me)
    except NumTooLargeError as me:
        print(me)

print(f"Correctly gussed the Number: {num} in Gusses: {count}")
