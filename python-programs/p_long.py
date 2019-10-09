def permutation(n,r):
	print("value of n is" +str(n))
	print("value of r is" +str(r))
	c=n-r
	
	if(c==0):
		print("n-r is 0")
		p=1
		for i in range(1,n+1)
			p=p*i
		print("permutation is" str(p))
		
	elif(c==1):
		print("n-r is 1")
		p=1
		for i in range(1,n+1)
			p=p*i
		print("permutation is" str(p))
		
	elif(c>1):
		print("n-r is" str(c))
		num=1
		for i in range(1,n+1)
			num=num*i
		print(num)
		
		den=1
		for j in range(1,r+1)
			den=den*i
		print(den)
		
		print(num/den)
		
	
		
	else:
		print("Invalid numbers")
	

permutation(5,5)




	
