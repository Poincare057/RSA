def encrypt(x, n):
	return (x % n)
def solvemod(N, n):
	for i in range(n):
		if (N*i % n == 1):
			return i
	return 0
def decrypt(x, p, q):
	xp = x%p
	xq = x%q
	ap = solvemod(q,p)
	aq = solvemod(p,q)
	return (xp*q*ap + xq*p*aq)
