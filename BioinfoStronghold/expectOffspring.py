#For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). 
#The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.
#As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms  that E(X)=∑6k=1k×Pr(X=k)=3.5.
#More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die 
#example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.




#reads in the rosalind data
text =  open("rosalind_iev.txt", "rt")
data = text.read()
text.close()

#splits the data into list of varibales
data = data.split(" ")


#can ignore last integer because no dominant phenotypes are produced between heterozygous recessive pair offspring
def Prob(a,b,c,d,e):
    sum = 0
    sum += a*2
    sum += b*2
    sum += c*2
    sum += d*1.5
    sum += e

    return sum

print(Prob(float(data[0]), float(data[1]),float(data[2]), float(data[3]), float(data[4])))
