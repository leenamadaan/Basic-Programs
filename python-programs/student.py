# Dictionary
import csv;
col_name=['Age','Name','Class','Total Marks']
s=[
{'Age': 15, 'Name': 'A', 'Class': 'Vth', 'Marks':{'Maths':70,'English':60,'Science':80}},
{'Age': 16, 'Name': 'B', 'Class': 'VIth', 'Marks':{'Maths':50,'English':60,'Science':80}},
{'Age': 15, 'Name': 'S', 'Class': 'IVth', 'Marks':{'Maths':30,'English':60,'Science':80}},
{'Age': 17, 'Name': 'T', 'Class': 'VIIth', 'Marks':{'Maths':40,'English':60,'Science':80}},
]
fields=(s.keys())
print(fields)
data=(s.values())

print(data)

new=""
fil=open("dictfile.csv","w");
new=str(fields)
print(fil.write(new + "\n"))
val=str(data)
print(fil.write(val))

'''
try:
	if none in s:
		print("null")
except ValueError:
	print("Value error")'''

fil.close()


