def fibonacci(n):
	l = [0,1]
	for i in range(0, n+1):
		if i > 1:
			l.append(l[i-1] + l[i-2])
		print(l[i])

def test():
	fibonacci(5)

test()