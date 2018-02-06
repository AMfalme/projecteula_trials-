def multiples_sum_3_5(n):
	"""
		this function will give the sum of all
		the multiples of 3 and 5 nelow the number n
	"""
	sum = 0
	for x in range(1,n):
		if (x%3==0) or (x%5==0):
			sum += x
	return sum
print (multiples_sum_3_5(1000))