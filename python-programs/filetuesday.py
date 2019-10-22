import os;
import re;
print(os.getcwd())




'''
fileobj=open("src.txt","r")
print("filepointer is at byte",fileobj.tell())
fileobj.seek(10)
print("after fileptr",fileobj.tell())
fileobj.close();
'''

'''
fileptr=open("new.txt","r");
print(fileptr.seek(19));
for i in fileptr:
	print i


'''
	
fileptr=open("new.txt","r");
newfptr=open("newfile.csv","w"); 
phone=fileptr.read()	
a=" "
r=re.compile(r'(\d{3}[-]\d{3}[-]\d{4})')
result=r.findall(phone)
a=str(result)
print(a)
print(newfptr.write(a));
newfptr.flush();



