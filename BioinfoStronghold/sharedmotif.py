
text = open("rosalind_lcsm.txt", "rt")
data = text.readlines()
text.close


#create dictionary
keys = []        
values = []        
count = -1        
for line in data:        
    if line[0] == ">":        
        keys.append(line[1:].strip('\n'))        
        count += 1        
        values.append("")        
    if line[0] != ">":        
        values[count] += line.strip('\n')    


dict = dict(zip(keys,values))


def match(s,t):
    if s in t:
        return True
    else:
        return False
    
def getStr(s):
            
    res = [s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]
    return res
#Sort substrings by longest character    
keys = sorted(keys, key=len)
#loop through keys
key = keys[0]
#sort all substrings by length in reverse
sorted_res = sorted(getStr(dict[key]),key=len,reverse=True)
#loop through sorted substrings
    





for i in sorted_res:
    count = 0
    for otherkey in keys:
        if key != otherkey:
            if match(str(i), dict[otherkey]) == True:
                count +=1
                print("Matched")
    if count == len(keys)-1:
        print(i)
        break
                 

    
