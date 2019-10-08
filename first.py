print('hello world....')
a='Monday'

L1=['leena', '1996', 'IT']
print (L1)
print (L1[1])
print (L1[1:])
d= {1:'Zap', 2:'build', 3:'dot', 4:'com'}
print (d);
print(d.keys());
print(d.values);

"""
numb= int(input("enter the number:"));
if(numb%2==0):
	print("numb is even")
	
else:
	print("numb is odd")
	
	

i=20
for i in range(0,5):
	print("%d X %d = %d" %(numb,i, numb*i));

k=5
while k<=30:
	print (k);
	k=k+1;
	
m=2	
while m<=5:
	print(m);
	m=m+1;
	if(m==4):
		break;
	else:
		print("else loop"); 
		
	
		
p=1
while p<=7:
	print(p);
	p=p+1;
	if(p==5):
		continue;
		
		
		

		
"""
	
str="    octPo   Pber     "
str1="Novoeovomovboer{}"
age=21
company="  "

print(str *3)
print(str+str1)
print(str[3])
print(str[2:])
print('m' in str)
print("String is : %s" %(str1))
print(str.capitalize())

print(str1.format(age))
print(str1.count('o',0,4))

print(company.isspace())
print(str1.index('ovo', 0, 9))
print(str.islower())
print(str.lstrip())
print(len(str))
print(str.ljust(1,"$"))
print(str.rsplit())
table={97:103, 111:112, 117:None}
tab="Hello javatpoint"
print(tab.translate(table))
val="100"
val2="-200"
print(val.zfill(10))
print(val2.zfill(2))
part="Python is a programming python language"
print(part.rpartition("python"))
print(part.rpartition("Python"))
print(part.rpartition("language"))
Zap=["lEENA",21,"101"]
print(Zap[0])
print("Name is %s, Age is %d"%(Zap[0], Zap[1]))
Zap[1]="Madaan"
print(Zap)
for i in Zap:
	print(i);


build=[]
e=int(input("Enter the number of elements"));
for f in range(0,e):
	build.append(input("Enter the item"));
print("Printing the list items");
for f in build:
	print(f);

new=["A", "Z", 8]
print(new.append(build))
