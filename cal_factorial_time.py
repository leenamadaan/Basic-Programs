import timeit

code_to_test="""

def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=i*fact
		print(fact)

factorial(5)
"""
	
elapsed_time= timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)




