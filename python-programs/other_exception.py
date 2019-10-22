def newexce(a,b):
	try:
		c=a/b;
		print(c)
		
	except ZeroDivisionError:
		print("zero division error")
	
	except Exception:
		print("Exception")
	else:
		print("Else code exceuted")

	finally:
		print("Must executable code")


newexce(2,1)

		



