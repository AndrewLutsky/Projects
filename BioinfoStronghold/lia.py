import numpy as np
text = open("rosalind_lia.txt","rt")
data = text.read()
text.close()

n = int(data[0])
k = int(data[2])




#since the probality of producing AaBb with any offspring and AaBb is equal to 0.25
#We just need to find number of trials

#finds number of trials
trials = 2**n
#total probability of events
prob = 1
#subtracts P(x=k) from total probability
for i in range(0, k):
    prob -= ((np.math.factorial(trials)/((np.math.factorial(trials-i)*np.math.factorial(i)))) * (0.25**i)* (0.75**(trials-i)))



print(prob)
