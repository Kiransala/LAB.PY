d1={1:"Rohan",2:"Pranav",3:"Kiran"}
d2={4:"Shetty",5:"Godse",6:"Sala"}

print(d1)

d1.update(d2)
print(d1)

d1.pop(2)
print(d1)

d3 = d1.get(3, -1)
print(d3)

l1=[x for x in input("Enter city names: ").split()]
l2=[int(x) for x in input("Enter city zip code: ").split()]
z=zip(l1,l2)
d=dict(z)
print(d)
