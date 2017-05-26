import time

def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

t = time.clock()
print fib(5)
print time.clock() - t