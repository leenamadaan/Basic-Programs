'''class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
'''

'''
class Myclass:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def newfunc(abc):
		print("ddd" + abc.name)

c=Myclass("Leena", 23)
c.age=30
print(c.age)
''' 


class Parent():
	def __init__(self,fname,lname):
		self.firstname=fname
		self.lastname=lname
	
	def anotherfunc(abc):
		print(abc.firstname + abc.lastname)
		

class Child(Parent):
	def __init__(self,f,l):
		Parent.__init__(self,f,l)
			
x=Child("Leena","Madaan")
x.anotherfunc()
	
