class emp:
    def __init__ (self, id1, name1):
        self.id = id1
        self.name = name1
    def display(self):
        print(self.id)
        print(self.name)
    def setvalue(self, id1, name1):
        self.id = id1
        self.name = name1
        
l1= list()
    
user=False
while not user:
	choice=int(input("\n\n1.Read an employee\n2.Modify the emloyee\n3.Display employees\n4.Delete employee\n5.Exit\nEnter choice: "))
	if choice==1 :
	    no_e=int(input("Enter the no of employees: "))
	    for i in range(no_e):
	        eid = int(input("Employee id: "))
	        ename = input("Employee name: ")
	        e1 = emp(eid, ename)
	        l1.append(e1)
	        
	elif choice==2 :
	    upid=int(input("Enter employee id to be updated: "))
	    upname=input(f"Enter employee name at id {upid} to be updated: ")
	    for q in l1:
	        if q.id == upid:
	            q.setvalue(upid, upname)
	       
	elif choice==3 :
	    for i in l1:
	        print(f"Employee \nid: {i.id}  name: {i.name}")

	elif choice==4 :
	    did=int(input("Enter employee id to be deleted: "))
	    for d in l1:
	        if d.id == did:
	            l1.remove(d)
	    
	elif choice==5 :
		user=True
	else :
		print("Invalid choice")

