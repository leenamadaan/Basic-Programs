import csv
csv_columns = ['Age','Name','Class','Marks', 'Maths','English', 'Science']
dict_data = [
{'Age': 15, 'Name': 'A', 'Class': 'Vth', 'Marks':{'Maths':70,'English':60,'Science':80}},
{'Age': 16, 'Name': 'B', 'Class': 'VIth', 'Marks':{'Maths':50,'English':60,'Science':80}},
{'Age': 15, 'Name': 'S', 'Class': 'IVth', 'Marks':{'Maths':30,'English':60,'Science':80}},
{'Age': 17, 'Name': 'T', 'Class': 'VIIth', 'Marks':{'Maths':40,'English':60,'Science':80}},
]


csv_file = "Student.csv"
try:
	
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        sum=0
        for data in dict_data:
            writer.writerow(data)
            '''for i in Marks.values():
				sum=sum+i
				print(sum)'''
				
            

       
except IOError:
    print("I/O error")  
    



