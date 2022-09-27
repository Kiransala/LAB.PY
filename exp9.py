from exp92 import subtraction 
from x.exp91 import addition

print(addition(1,2,3))
print(addition(2,3))
print(addition(1))

print(subtraction(3,2))



def addition(a=None,b=None,c=None):
	if a!=None and b!=None and c!=None:
		return a+b+c
		
	elif a!=None and b!=None:
		return a+b
		
	else :
		return a
  
  
  def subtraction(a=None,b=None):
	if a!=None and b!=None:
		return a-b
