def rabrec(n,k):

	arr = [None] * n
	arr[0] = 1
	arr[1] = 1
	for i in range(n):
		if i>1:
			arr[i] = arr[i-1] + k * arr[i-2]
	
	return arr


print(rabrec(32,5))
