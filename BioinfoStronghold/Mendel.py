


def getProbDom(k,m,n):
	sum = k + m + n
	pK = k/sum
	pM = m/sum
	pN = n/sum


	probDom = pK + (pM * ((k/(sum-1)) + ((m-1)/(sum-1))*3/4 + (n/(sum-1)*1/2))) + (pN* ((k/(sum-1))+ (m/(sum-1))*1/2 )) 
	return probDom



print(getProbDom(21,23,30))



