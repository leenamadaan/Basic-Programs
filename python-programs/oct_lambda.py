from functools import reduce
'''
name=["John","Army"]

k=map(lambda h:h.upper(),name)
print(k)

firstlist=["abc","hjk"]
lastlist=["def","uio"]
g=map(lambda g,h:g+h,firstlist,lastlist)
print(g)


new_li=[2.5,3,4.1,10]

sum=reduce(lambda j,k:j+k,new_li)
print(sum)
print(type(sum))

new_str=["rat","hat","map"]
s=reduce(lambda s,t:s+t,new_str)
print(s)
print(type(s))

fww=[1,2,3,4]
e=reduce(lambda i,j:i+j,fww)
print(e)
'''

'''

a=lambda b:b*b
print(a(2))


li=[5,9,2,4,8]
n=filter(lambda n:(n%2==0),li)
print(n)
print(type(n))



p=map(lambda n:(n%2==0),li)
print(p)
print(type(p))


m=map(lambda i:(i*2),li)
print(m)
print(type(m))

new_li=[2,3,4,10]
sum=reduce(lambda j,k:j+k,new_li)
print(sum)
print(type(sum))


def new_fun(a):
	x=a%2
	if x==0:
		print(a)
new_fun(4)





def func(a):
	------
	-------
	------
	------
	return fact
	
	
list = [1,2,4,5,6]
fact_list = []
for i in list:
	fact_list.append(func(i))
	
	
vs
'''

def upper_fun(s):
	return str(s.upper())

print(upper_fun("hjj"))



	
	
	
	
	
	
		
	


