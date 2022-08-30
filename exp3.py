list1 =[int(x) for x in input("Enter odd numbers : ").split()]
list2 = [int(x) for x in input("Enter even numbers : ").split()]

print("odd values ", list1 , "even values", list2 )

list3 = list()
list3 = list1 + list2
print("orignal list is ",list3)
list3.sort()
print("sorted elemnents in list are ",list3)

list3[0]= int(input("enter number at index 0 "))
print(list3)

mid = len(list3)//2
list3.remove(list3[mid])
print(list3)

listn = [x for x in input("Names : ").split()]

for n in listn:
    list3.append(n)

if list3.count("python")>0 :
    print("present")
else:
    print("absent")
