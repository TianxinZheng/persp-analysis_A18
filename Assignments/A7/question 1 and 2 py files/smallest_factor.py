def smallest_factor(n):
	if n == 1: return 1
	for i in range(2, int(n**.5) + 1):
		if n % i == 0: return i
	return n