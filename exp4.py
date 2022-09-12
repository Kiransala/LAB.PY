n = int(input("Enter the number of students: "))
lst1 = list()

for i in range(0, n):
    r = int(input("Enter roll number: "))
    n1 = input("Enter a name: ")
    m1 = int(input("Enter marks of subject1: "))
    m2 = int(input("Enter marks of subject2: "))
    m3 = int(input("Enter marks of subject3: "))
    l1 = [r, n1, m1, m2, m3]
    tpl = tuple(l1)
    lst1.append(tpl)
    
tpl = tuple(lst1)

user = False
while not user:
    choice = int(
        input("1.Print Tuple \n2.Tuple containing python \n3.Sorted tuple \n4.Exit\nEnter the choice: "))
    if choice == 1:
        print("Tuple: ")
        print(tpl)
    elif choice == 2:
        print("Tuple containing python: ")
        for t in tpl:
            if "python" in t:
                print(t)
    elif choice == 3:
        print("Sorted tuple according to names: ")
        print(sorted(tpl, key=lambda x: x[1]))

    elif choice == 4:
        print("Exited")
        user = True
    else:
        print("Enter a valid choice")
