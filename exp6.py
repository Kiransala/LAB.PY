user=False
while not user:
	choice=int(input("\n\n1.Create a key/value pair dictionary\n2.Concatenate and delete the item of the existing dictionary\n3.Find a key and print its value\n4.Map two list into a dictionary\n5.Exit\nEnter choice: "))
	if choice==1 :
	    l1=[int(x) for x in input("Enter dictionary 1 keys: ").split()]
	    l2=[x for x in input("Enter dictionary 1 values: ").split()]
	    z1=zip(l1,l2)
	    d1=dict(z1)
	    l3=[int(x) for x in input("Enter dictionary 2 keys: ").split()]
	    l4=[x for x in input("Enter dictionary 2 values: ").split()]
	    z2=zip(l3,l4)
	    d2=dict(z2)
	    print(f"Dictionary1- {d1}\nDictionary2- {d2}")
	    
	elif choice==2 :
		d1.update(d2)
		print(f"Concatenated Dictionary- {d1}")
		p = int(input("Delete the value at key: "))
		d1.pop(p)
		print(f"Updated Dictionary- {d1}")
	elif choice==3 :
	    l3=d1.keys()
	    s1 = int(input("Enter the key to be searched: "))
	    for x in l3:
	        if s1==x:
	            print("value at key {} is {}".format(s1,d1[s1]))
	elif choice==4 :
		l5=[int(x) for x in input("Enter zip code: ").split()]
		l6=[x for x in input("Enter city city names: ").split()]
		z3=zip(l5,l6)
		d3=dict(z3)
		print(f"Maped Dictionary is {d3}")
	elif choice==5 :
		user=True
	else :
		print("Invalid choice")
