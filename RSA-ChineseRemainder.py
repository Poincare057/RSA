def encrypt(x, n):
	return (x % n)
def solvemod(N, n):
	for i in range(n):
		if (N*i % n == 1):
			return i
	return 0

#Chinese Remainder
def decrypt(x, p, q):
	xp = x%p
	xq = x%q
	ap = solvemod(q,p)
	aq = solvemod(p,q)
	return (xp*q*ap + xq*p*aq)

#Euler's theorem
def decrypt(x, p, q, e):
	d = solvemod(e, (p-1)*(q-1))
	return (x**d)%(p*q)
