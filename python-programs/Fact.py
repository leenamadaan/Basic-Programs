def factorial(number):
	print("Number " +str(number))
	fact=1
	for i in range(1,number+1):
		fact=i*fact
	print("Factorial is " +str(fact))
	
factorial(5)

