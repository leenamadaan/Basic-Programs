def new():
	n=0
	while True:
		yield n
		n+=2

g = new()
print(g.next())
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.next())
print(g.next())
print(g.next())





