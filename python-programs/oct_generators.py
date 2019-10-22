import time;


start_time=time.time()
print(start_time)


mylist = [ x for x in range(100000000)]
for i in range(10):
	print(mylist[i])
	
end_time=time.time()
print(end_time)
s=end_time-start_time;
print(s)

second_start_time=time.time()
print(second_start_time)
genlist = (x for x in range(100000000))
print(genlist)
for i in range(10):
	print(genlist.next())
second_end_time=time.time()
print(second_end_time)
n=second_end_time-second_start_time
print(n)


	

