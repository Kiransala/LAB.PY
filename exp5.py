s1={x for x in input("Enter string 1: ")}
s2={x for x in input("Enter string 2: ")}
print("String is: ", s1 ,"::", s2)

user=False
while not user:
	choice=int(input("\n\n1.Display Common \n2.Display difference\n3.Display union\n4.Dispay Symmetric difference\n5.Exit\nEnter choice: "))
	if choice==1 :
		print(s1.intersection(s2))
	elif choice==2 :
		print(s1.difference(s2))
	elif choice==3 :
		print(s1.union(s2))
	elif choice==4 :
		print(s1.symmetric_difference(s2))
	elif choice==5 :
		user=True
	else :
		print("Invalid choice")
