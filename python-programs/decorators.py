import random
import math

def elementExits(lis,search):
	for e in lis:
		if e == search:
			return True
	return False
					
				

l=[1,2,3,4,5,4,5]
if elementExits(l,14):
	print('Element Exits')
else:
	print('Elemet not found')



'''
L=[]
for i in range(0,5):
	L.append(random.randrange(5))
	print(L)
	
	
	
	for j in range(i+1,5):
		if L[j]==L[i]
		break
	print(L)

'''


'''for i in range(0,5):
	
	L.append(random.randrange(5))'''


