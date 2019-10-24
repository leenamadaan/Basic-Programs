import csv
csv_columns = ['Age','Name','Class','Marks', 'Maths','English', 'Science']
dict_data = [
{'Age': 15, 'Name': 'A', 'Class': 'Vth', 'Marks':{'Maths':70,'English':60,'Science':80}},
{'Age': 16, 'Name': 'B', 'Class': 'VIth', 'Marks':{'Maths':50,'English':60,'Science':80}},
{'Age': 15, 'Name': 'S', 'Class': 'IVth', 'Marks':{'Maths':30,'English':60,'Science':80}},
{'Age': 17, 'Name': 'T', 'Class': 'VIIth', 'Marks':{'Maths':40,'English':60,'Science':80}},
]

def School(dict_data):
	csv_file ="Student.csv"
	try:
		with open(csv_file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
			print(writer.writeheader())
			sum=0
			for student in dict_data:
				for key,value in student.items():
					print(key,value)
					print('check value')
					if isinstance(value,dict):
						for subject,marks in value.items():
							print(subject,marks)
							sum=sum+marks
							print(sum)
	except Exception as e:
		print("Exception", e)

School(dict_data)
