# Iterative exponent calc
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp != 0:
        result = base
        while exp > 1:
            exp -=1
            result *= base
        return result
    else:
        result = 1.0000
        return result
        
# recursive exponent calc        
def recurPower(base, exp):
    if exp != 0:    
        if exp == 1:
            return base
        else:
            return base * recurPower(base, exp -     1)
    else:
        result = 1.0000
        return result
        
# recursive exponent with rules       
def recurPowerNew(base, exp):
    if exp > 0 and exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    elif exp > 0 and exp % 2 == 1:
        return base * recurPowerNew(base, exp -1)
    else: 
        return 1
        
# Iterative Greatest common devisor        
def gcdIter(a, b):
    mn = min(a,b)
    mx = max(a,b)
    while mx%mn !=0 or a%mn !=0 or b%mn !=0:
        mn -=1
    return mn
    
    
# GCD due to Euclid
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
        
        
# Iter Count string
def lenIter(aStr):
    count = 0
    for i in aStr:
        count += 1
    return count
    
    
# Recur count string
def lenRecur(aStr):
    if aStr:
        return 1+ lenRecur(aStr[1:])    
    else:
        return 0    


# Recur check char in string
def isIn(char, aStr):
    length = len(aStr)
    if char == aStr:
        return True
    if length <= 1:
        return False
    mid = aStr[length/2]
    if char > mid:
        return isIn(char, aStr[length/2:])
    elif char < mid:
        return isIn(char, aStr[0:length/2])
    else:
        return True 
        
        
# Recur check if semordnilap
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    elif len(str1) == 1 and len(str2) == 1:
        return (str1 == str2)
    return (str1[0] == str2[-1]) and (semordnilap(str1[1:], str2[:-1]))