import random

lst = []
while True:
	r = random.randrange(10)
	if r not in lst:
		lst.append(r)
	if len(lst) == 10:
		break
		
print(lst)


'''
def checkelement():
	for i in range(0,5):
		a=[]
		r=random.randrange(5)
		if r not in a:
			a.append(r)
			print(a)
		
	
checkelement() 
'''


def h1(a):
	return '<h1>'+ a 
	

def wrapDiv(fun):
	return '<div>' + fun() + '</div>'

print(wrapDiv(h1))

	

			
		
	
	
	



	
