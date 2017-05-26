def gcd(m, n):
	assert m > 0 and n > 0, 'error message'
	if m < n:
		return gcd(n, m)
	if m % n == 0:
		return n
	else:
		return gcd(n, m % n)
		
print gcd(35, 21)