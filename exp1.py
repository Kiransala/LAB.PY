import sys

a = (sys.argv[1])
b = (sys.argv[2])

print("Before swapping")
print('a=' + a)
print('b=' + b)

print("after swapping")
temp = a
a = b
b = temp
print('a= ' + a)
print('b= ' + b)

a = int(a)
if a>0:
    print("a is positive number")
elif a<0:
    print("a is negative number")
else:
    print("a is zero")
