# cmsc128-ay2015-16-assign002-py

###### Assign 002: Bioinformatics Library

###  01 Function: getHammingDistance(str1, str2)

What it does: Given two strings str1 and str2 of same length (length must never be 0 or
negative!), the Hamming Distance of those two strings are the number of inversions per
character need to transform str1 to str2 or vise-versa. Simply put, the Hamming Distance
of two strings is the number of characters that differ in ith position from position 1 to
strlen(str1).

##### Example:
* getHammingDistance(“AACCTT”,”GGCCTT”) returns 2
* getHammingDIstance(“TCGGA”,”AAAAG”) returns 5
* getHammingDistance(“A”,”AG”) returns “Error! Strings are not equal!”

###  02 Function: countSubstrPattern(original, pattern)
What it does: Given a string original and pattern, we will count the number of occurrence
of pattern in original.

##### Example:
* countSubstrPattern(“AATATATAGG”,”GG”) returns 1
* countSubstrPattern(“AATATATAGG”,”ATA”) returns 3
* countSubstrPattern(“AATATATAGG”,”ACTGACTGACTG”) returns 0

### 03 Function: isValidString(str, alphabet)

What it does: Given an alphabet string where all letters are assumed to be unique, this
function returns true if the string str is a valid string based on the letters of alphabet.

##### Example:
* isValidString(“AAGGCTATGC”,”ACGT”) returns true
* isValidString(“AAGGCTATGa”,”ACGT”) returns false
* isValidString(“ACGT”,”ACGT”) returns true
* isValidString(“ACGT101_”,”ACGT”) returns false
* isValidString(“091212345”,”0123456789”) returns true

### 04 Function: getSkew(str, n)

What it does: Given a genome str of some length q (where q>0), it returns the number of
Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero,
negative or positive. The first position is one (1) not zero(0) as we typically associate with
string implementations.

##### Example:
* getSkew(“GGCCAC”, 1) returns 1
* getSkew(“GGCCAC”, 2) returns 2
* getSkew(“GGCCAC”, 3) returns 1
* getSkew(“GGCCAC”, 4) returns 0
* getSkew(“GGCCAC”, 5) returns 0

### 05 Function: getMaxSkewN(str, n)
What it does: Given a genome str of some length q (where q>0), it returns the maximum
value of the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The
value can be zero, negative or positive. The first position is one (1) not zero(0) as we
typically associate with string implementations.

##### Example:
* getMaxSkewN(“GGCCAC”, 1) returns 1
* getMaxSkewN(“GGCCAC”, 2) returns 2
* getMaxSkewN(“GGCCAC”, 3) returns 2
* getMaxSkewN(“GGCCAC”, 4) returns 2
* getMaxSkewN(“GGCCAC”, 5) returns 2

### 06 Function: getMinSkewN(str, n)

What it does: Given a genome str of some length q (where q>0), it returns the minimum
value of the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The
value can be zero, negative or positive. The first position is one (1) not zero(0) as we
typically associate with string implementations.

##### Example:
* getMinSkewN(“GGCCAC”, 1) returns 1
* getMinSkewN(“GGCCAC”, 2) returns 1
* getMinSkewN(“GGCCAC”, 3) returns 1
* getMinSkewN(“GGCCAC”, 4) returns 0
* getMinSkewN(“GGCCAC”, 5) returns 0

## | RNC Recario | CMSC 128 | Second Programming Assignment |
