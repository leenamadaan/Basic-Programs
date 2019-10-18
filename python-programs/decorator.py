'''
# decorator
def add_message(fun):
	def inner(radius):
		return 'Area of circle:' + str(fun(radius))
	return inner


	
	

@add_message
def calculateArea(r):
	return 2 * 3.14 * r



print(calculateArea(37))
'''

'''
# addition

def other_dec(a):
	print('2525252525252525')
	print a
	print('2525252525252525')
	def other(*args):
		return "Addition" + str(a(*args))
	return other


def new_dec(f):
	print('3434343434343434')
	print f
	print('3434343434343434')
	def inner(*args):
		return " numbers "+ str(f(*args))
	return inner
		

@other_dec
@new_dec
def addition(*args):
	c=1
	for i in args:
		print i
		c+=i
	return c
	

print(addition(2,4))
'''


def italic(func):
	print(func)
	def itta(*args):
		return "<content italic>" + str(func(*args))
	return itta
	


def bold(*args,**kwargs):
	print(args)
	print(kwargs)
	def argf(func):
		print(func)
		def inner(*args,**kwargs):
			print("in args" +str(args))
			print("in kwargs" +str( kwargs))
			'''return "content bold" +str(func(*args,**kwargs))'''
		return inner
	return argf
	
	

@italic
@bold(font_size='100px')
def paragraph(content):
	return '<p>' + content + '</p>'
	
	

print(paragraph('This is just a simple paragraph'))	


'''
@underline
@italic
'''







"""def hello(fun):
	print("first")
	fun()
	print("print fun")
	def inner():
		print("111")
		
	return inner

def function_to_be_used():
	print("Last")

a=hello(function_to_be_used)

a"""


	




