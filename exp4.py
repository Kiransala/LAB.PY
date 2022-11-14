s = int(input("Enter the number off students: "))
lst1 = list()

for i in range(0,s):
    r = int(input("Enter the rollno: "))
    n = input("Enter the name: ")
    m1 = int(input("Marks of subject1: "))
    m2 = int(input("Marks of subject2: "))
    m3 = int(input("Marks of subject3: "))
    l1 = [r, n, m1, m2, m3]
    tpl = tuple(l1)
    lst1.append(tpl)
    
tpl = tuple(lst1)

condition = False

while not condition:
    choice = int(input("\n\n1.Print Tuple \n2.Tuple containing python \n3.Sorted Tuple \n4.Exit \nEnter choice: "))
    if choice == 1:
        print(f"Tuple: {tpl}")
    elif choice == 2:
        print("Tuple containing python: ")
        for t in tpl:
            if "python" in t:
                print(t)
    elif choice == 3:
        print("Sorted tuples according to names: ")
        print(sorted(tpl, key=lambda x: x[1]))
    elif choice == 4:
        condition = True
    else:
        print("Invalid choice.")
