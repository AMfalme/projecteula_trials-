def fib(n):
	a,b = 0,1;
	sum = 0
	while b < n:
		if (b % 2) == 0:
			sum +=b
		a, b = b, a + b
	return sum 


print (fib(10))