class emp:
    def __init__ (self, id1, name1):
        self.id = id1
        self.name = name1
        
    def display(self):
        print(self.id)
        print(self.name)
        
    def setvalues(self,id1 ,name1):
        self.id = id1
        self.name = name1
        
l1 = list()

condition = False

while not condition:
    choice = int(input("\n\n1.Read employee \n2.Modify the employee \n3.Display the employees \n4.Delete an employee \n5.Exit \nEnter choice: "))
    if choice == 1:
        no_e = int(input("Enter the no of employees: "))
        for i in range(no_e):
            eid = int(input("Enter id: "))
            ename = input("Enter name: ")
            e1 = emp(eid, ename)
            l1.append(e1)
            
    elif choice == 2:
        upid = int(input("Enter the employee id: "))
        upname = input(f"Enter the new name of employee at id {upid}: ")
        for x in l1:
            if x.id == upid:
                x.setvalues(upid, upname)
                
    elif choice == 3:
        print("\n\n\tEMPLOYEES\t\t\n")
        for i in l1:
            print(f"\tId: {i.id} | Name: {i.name}")
            
    elif choice == 4:
        did = int(input("Enter the employee id to be deleted: "))
        for d in l1:
            if d.id == did:
                l1.remove(d)
                
    elif choice == 5:
        condition = True
        
    else:
        print("Invalid choice")
