def DNAtoRNA(s):
    t=""
    for i in s:    
        if i != "T":    
            t+=i    
        else:    
            t+="U"    
    
    return t  
