target = 999
def multiples_sum(n):
	"""
	this function gives the multiples of 3 and 5 and adds them together
	"""
	p = target//n
	return n*(p * (p+1))/2
sum = multiples_sum(3) + multiples_sum(5) - multiples_sum(15)
print (sum)