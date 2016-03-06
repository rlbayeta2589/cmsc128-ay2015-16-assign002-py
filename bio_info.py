################################################################################################/
#
#   bio_info.py
#
#   Author : Bayeta Reynaldo, III
#            CMSC128 AB-1L
#            https://github.com/rlbayeta2589
#
#################################################################################################/

def getHammingDistance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dist = 0

    if (len1 <= 0 or len2 <= 0): 
        return 'Error! Length must never be 0 or negative!'
    if len1 != len2:
        return 'Error! Strings are not equal!'

    for i in range(len1):
        if str1[i] != str2[i]:                  # increment distance value
            dist += 1                           # if chars is not equal

    return dist

def countSubstrPattern(original, pattern):
    orig_len = len(original)
    ptrn_len = len(pattern)
    count = index = 0

    if (orig_len <= 0 or ptrn_len <= 0): 
        return 'Error! Length must never be 0 or negative!'
    
    for i in range(orig_len):
        index = i + ptrn_len
        if orig_len < index:                    # if the length of the index
            return count                        # exceeds the length of orig
        elif original[i:index]==pattern:
            count += 1                          # if the substring is equal to
                                                # the pattern
def isValidString(str, alphabet):
    strlen = len(str)
    if (strlen <= 0): 
        return 'Error! Length must never be 0 or negative!'
    
    for i in range(strlen):
        if alphabet.find(str[i])==-1:           # .find function returns -1
            return False                        #  if substring is not found

    return True

def getSkew(str, n):
    if n <= 0 or n > len(str):
        return 'Error! Invalid index!'          # returns the count of 'G' minus
                                                #   the count of 'C'
    return (str.count('G',0,n) - str.count('C',0,n))

def getMaxSkewN(str, n):
    skews = []

    if n <= 0 or n > len(str):
        return 'Error! Invalid index!'

    for i in range(n):                          #  call getSkew function 'n' times
        skews.append(getSkew(str, i+1))         #      and put the values in an array

    return max(skews)                           #  return the max in the array of skews 

def getMinSkewN(str, n):
    skews = []

    if n <= 0 or n > len(str):                  #  call getSkew function 'n' times
        return 'Error! Invalid index!'          #      and put the values in an array 

    for i in range(n):
        skews.append(getSkew(str, i+1))

    return min(skews)                           #  return the min in the array of skews 


