def show(*args, **kwargs):
	print(type(args))
	print(type(kwargs))
	print(args)
	print(kwargs['name'])
	
	

show(23,10,27,name='john',last='Ron')
