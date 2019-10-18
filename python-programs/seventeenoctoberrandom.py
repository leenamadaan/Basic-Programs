import random
print(random.randrange(5))

def elementexist(lis,search):
	for e in lis:
		if e==search:
			return True
	return False
		
l=[1,2,3,4,5,6]
if elementexist(l,4):
	print("Element Exist")
else:
	print("Element doesn't exist")
	

L=[]
L.append(random.randrange(5))
print(L)


'''
import random
import math

def checkelement():
	for i in range(0,5):
		a=[]
 
		a.append(random.randrange(5))
		if a in a:
			break
	else:
			print("Random numbers", a)
checkelement() 
'''
