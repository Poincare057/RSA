def encrypt(x, n):
	return (x % n)
def solvemod(N, n):
	for i in range(n):
		if (N*i % n == 1):
			return i
	return 0
def decrypt(x,p,q):
	xp = x%p
	xq = x%q
	np = q
	nq = p
	ap = solvemod(np, p)
	aq = solvemod(nq, q)
	return xq*ap*nq + xp*aq*np
