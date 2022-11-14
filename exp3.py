list1 = [int(x) for x in input("Enter odd values: ").split()]
list2 = [int(x) for x in input("Enter even values: ").split()]
print(f"Odd values: {list1} \nEven values: {list2}")

condition = False

while not condition:
    choice = int(input("\n\n1.Merge and Sort two list \n2.Update the first element x and delete the middle element\n3.Find max and min from the list\n4.Add elements into the list and check if python is present \n5.Exit\nEnter the choice: "))
    if choice == 1:
        list3 = list()
        list3 = list1 + list2
        print(f"The merged list is: {list3}")
        list3.sort()
        print(f"The sorted list is: {list3}")

    elif choice == 2:
        list3[0] = int(input("Enter the new value: "))
        mid = len(list3)//2
        list3.remove(list3[mid])
        print(list3)

    elif choice == 3:
        maximum = max(list3)
        minimum = min(list3)
        print(
            f"The maximum value is {maximum} and minimum value is {minimum}.")

    elif choice == 4:
        listn = [x for x in input("Enter the elements: ").split()]

        for n in listn:
            list3.append(n)

        if list3.count("python") > 0:
            print("Python is present.")
        else:
            print("Python is absent.")

    elif choice == 5:
        condition = True

    else:
        print("Invalid choice.")
