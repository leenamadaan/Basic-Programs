def show(*args, **kwargs):
	print(type(args))
	print(type(kwargs))
	print(args)
	print(kwargs['name'])
	
	

show(23,10,27,name='john',last='Ron')

def arg(*args, **kwargs):
	print(args)
	print(kwargs)
	
arg(10,20,30,k1='abc',kr='def')

def argsss(*args):
	for i in args:
		print(i)
	
argsss(10,20,30)

def argeee(**kwargs):
	for key, value in kwargs.items():
		print("%s==%d") %(key,value)
argeee(age=10, marks=100)












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







