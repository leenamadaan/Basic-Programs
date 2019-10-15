print("dictionary type")
d={'Name':'Leena', 'Company':'Zapbuild', 'Age':21}
k = d
d['Age']=20;
print(k)


print("List type")
m=[1,2]
n=m 
m.append(3)
print(n)



print("dictionary with function")
def dictionary(ad):
	print(ad)
	new=dict(ad.items())
	ad.update({'Years':10})
	print("old Updated dictionary", ad)
	print("new dictionary", new)
	
dictionary(ad={'Name':'Zapbuild','Location':'Mohali'})


print("List with function")
def add(l):
	
	l.append(2)
	print(l)

k=[1]

add(k[:])
print(k)

print("Set")
s1={1,2,3}
s2=s1
s3={}
s3=s1.copy()
print(s3)
s1.add(4)
print(s2)







	




