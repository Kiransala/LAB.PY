list1 =[int(x) for x in input("Enter odd numbers: ").split()]
list2 = [int(x) for x in input("Enter even numbers: ").split()]
print("Odd values: ", list1, "Even values: ", list2)
        
condition = False

while not condition:
    print("\n")
    choice = int(input("Choose one operation on lists: \n1.Merge and sort the two lists.\n2.Update the first element with X value and delete the middle element of the list.\n3.Find max and min elements from the list.\n4.Add N names into the existing number list and check if word python is present in the list.\n5.Exit.\nChoice: "))
    if choice == 1:
        list3 = list()
        list3 = list1 + list2
        print("Concatinated list is: ",list3)
        list3.sort()
        print("Sorted list is: ",list3)
        
    elif choice == 2:
        list3[0]= int(input("Update the first element with "))
        mid = len(list3)//2
        list3.remove(list3[mid])
        print(list3)

    elif choice == 3:
        maximum = max(list3)
        minimum = min(list3)
        print("Max = %d \nMin = %d\n" %(maximum,minimum))
        
    elif choice == 4:
        listn = [x for x in input("Enter names : ").split()]
    
        for n in listn:
            list3.append(n)
    
        if list3.count("python") > 0:
            print("Python is present.\n")
        else:
            print("Python is absent.\n")
        
    elif choice == 5:
        condition = True
    else:
        print("Enter a valid choice\n")
