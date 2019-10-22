

try:
	age=int(input("enter age :"))
	if(age<18):
		raise ValueError;
	else:
		print("Valid age")
except ValueError:
	print("you are not eligible for voting")
