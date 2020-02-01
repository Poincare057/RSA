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

#Extended Euclidean Algorithm that solves bx mod a = 1; returns (x,y) pair where ax + by = 1
def exteuc(a, b):
	A = [a, b]
	Q = [a//b]
	X = [0,0,1]
	Y=[0,1,-Q[0]]
	c = a%b
	A += [c]
	while c > 1:
		a, b = b, c
		Q += [a//b]
		c = a%b
		X += [X[len(X) - 2] - X[len(X)-1]*Q[len(X)-2]]
		Y += [Y[len(Y) - 2] - Y[len(Y)-1]*Q[len(Y)-2]]
	return [X[len(X)-1], Y[len(Y)-1]]

#RSA Encryption
def encrypt(x, n, e):
    return fastmodexp(x, e, n)

#RSA Decryption 
def decrypt(x, p, q, e):
	d = (exteuc((p-1)*(q-1), e)[1])%((p-1)*(q-1)) #a = (p-1)*(q-1), b = e. Have to take y from extended euclid mod (p-1)*(q-1) to get d. 
	return fastmodexp(x, d, p*q)

