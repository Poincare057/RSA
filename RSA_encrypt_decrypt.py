#O(log(a)^(log(3))*log(b)) modular exponentiation for a^b mod n
def fastmodexp(a, b, n):
	import numpy as np
	k = len(bin(b)) - 2
	l = np.empty((k+1))
	l[0] = a%n
	for i in range(1, k+1):
		l[i] = (l[i-1]**2)%n
	s = bin(b)[2:]
	s = s[-1::-1]
	p = 1
	for i in range(len(s)):
		if int(s[i]) == 1:
			p = (p*l[i])%n
	return int(p)

#Solution of linear congruence Nx mod n = 1
def solvemod(N, n):
    for i in range(n):
        if (N*i % n == 1):
          return i
    return 0

#RSA Encryption
def encrypt(x, n, e):
    return fastmodexp(x, e, n)

#RSA Decryption
def decrypt(x, p, q, e):
	d = solvemod(e, (p-1)*(q-1))
	return fastmodexp(x, d, p*q)
