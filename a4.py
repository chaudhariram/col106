import random
import math

# assuming that basic arithmetic operations on b-bit numbers take Θ(b)  time.


# for time complexity in this assignment we multiply the number of operations by log(q) because each operation is happening in q bits because I have used mod q before each operation.
# similarly to store any variable with value n we use log(n) bits so space will be O(log(n)).
# for each operation in hashing we have used q bits so we can limit the time and space of the assignment to log(q) order.



def power26(n, q):     # helper function which return 26^n in modulo terms. time complexity O(nlog(q)). space O(log(q)).
    ans = 1
    for  i in range(n):
        ans = ((ans)*(26%q))%q
    return ans



class hasher:                             # class hasher creates an object with value attribute which gives value of hash for part of string from i to j index.
    def __init__(self, string, i, j, q):
        self.q = q
        self.initindex = i
        self.finalindex = j
        self.patternlength = j-i + 1
        self.reapeatvalue = power26(self.patternlength-1, q)                      # for init time O(mlog(q)) and space O(log(q))
        self.value = 0
        self.string = string
        k = j
        n = 1
        while k > i-1:
            if self.string[k] == "?":
                self.value += 0
            else:
                self.value = self.value%q + (((ord(self.string[k])%q - ord("A")%q)%q)*(n))%q
            n *= 26%q
            k -= 1
        self.value = self.value%self.q
        
    def get_value(self):            # returns value of hash
        return self.value
    def move(self):                 # shifts the hash pattern to next index.
        if len(self.string)-1 > self.finalindex:
            self.value -= (((ord(self.string[self.initindex])%self.q - ord("A")%self.q)%self.q)*(self.reapeatvalue%self.q))%self.q
            self.value = self.value%self.q                                      # for move time O(log(q)) space O(log(q))
            self.value *= 26%self.q
            self.value = self.value%self.q
            self.value += ((ord(self.string[self.finalindex+1])%self.q - ord("A")%self.q)%self.q)%self.q
            self.value = self.value%self.q
            self.initindex += 1
            self.finalindex += 1






def modPatternMatch(q, p, x):  # q is some prime p is pattern string and x is the document string.
    if p == "" or x == "":
        return []                           # boundary conditions
    if len(p) > len(x):
        return []


    pattern_hash = hasher(p, 0, len(p)-1, q) #O(mlog(q)) time
    text_hash = hasher(x, 0, len(p)-1, q)    #O(mlog(q)) time                                 # for whole function time O((n+m)log(q)) space O(logn+logq)
    ans = []
    n = len(x)
    m = len(p)
    i = 0
    while i < n-m +1:                                        # space O((logn) + log(q))
        if text_hash.get_value() == pattern_hash.get_value():#
            ans.append(i)                                    #O(nlog(q)) time for loop
        text_hash.move()                                     #
        i += 1                                               #
    return ans

# print(modPatternMatch(1000000007, "CD", "ABCDE"))
# print(modPatternMatch(1000000007, "AA", "AAAAA"))
# print(modPatternMatch(2, "AA", "ACEGI"))






def modPatternMatchWildcard(q, p, x):
    if p == "" or x == "":
        return []              # boundary conditions
    if len(p) > len(x):
        return []
    
    for i in range(len(p)):
        if p[i] == "?":      # O(mlog(q)) time
            l = i
            break
    if len(p) == 1:
        ans = []
        for k in range(len(x)):
            ans.append(i)                                                      # for whole function time O((n+m)log(q)) space O(logn+logq)
        return ans
    coefficient = power26(len(p)-l-1, q) # O(mlog(q)) time # space O(logq)
    pattern_hash = hasher(p, 0, len(p)-1, q) # O(mlog(q)) time # space O(logq)
    text_hash = hasher(x, 0, len(p)-1, q)  # O(mlog(q)) time # space O(logq)
    ans = []
    n = len(x)
    m = len(p)
    k = 0
    list = []
    while k < n-m +1: #  O(nlog(q)) time # space O((logn)+log(q))
        if (text_hash.get_value() - (((ord(x[k + l])%q - ord("A")%q)%q)*(coefficient%q))%q)%q == pattern_hash.get_value():
            ans.append(k)
        text_hash.move()
        k += 1
    return ans



# print(modPatternMatchWildcard(3, "AB?D", "ABCDEFFEABEDEFFE"))
# print(modPatternMatchWildcard(1000000007, "?A", "ABCDE"))
# print(modPatternMatchWildcard(1000000007, "D?", "ABCDE"))
# print(modPatternMatchWildcard(13,"AM?HAIYA","BAMBHAIYAMBHAIYA"))
# print(modPatternMatchWildcard(19, "JA?S", "AMADBOXERSHOTQUICKGLOVEDJABSTOTHEJAWSOFHISDIZZYOPPONENTATTHEJAMSROCKSHUFFLE"))
# print(modPatternMatchWildcard(79, "JA?S", "AMADBOXERSHOTQUICKGLOVEDJABSTOTHEJAWSOFHISDIZZYOPPONENTATTHEJAMSROCKSHUFFLE"))


# we can find N by using the two results given in the pdf.
# for patt != text_part we have probability eps such that patt%q = text_part%q
# (patt-text_part)%q = 0
# S%q = 0
# so q must be prime factor of S which is order mlog26 bits. So replace pi(N) in result 2 by mlog26/eps and solving inequality by replacing log(N) by root(N) we get
# N = int(math.pow((2*math.log(26, 2)*(m/eps)), 2))
def findN(eps,m):
    return int(math.pow((2*math.log(26, 2)*(m/eps)), 2))


def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if isPrime(q):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]


def isPrime(q):
	if q > 1:
		for i in range(2, int(math.sqrt(q)) + 1):
			if  q % i == 0:
				return False
		return True
	else:
		return False

# Time complexity here will be similar to its mod counterpart but here q will be max N so it will be replaced by log(m/eps) because N comes out be that order. 
# similarly we can find space complexity of this function by replacing q with order of N.
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)
# Time complexity here will be similar to its mod counterpart but here q will be max N so it will be replaced by log(m/eps) because N comes out be that order. 
# similarly we can find space complexity of this function by replacing q with order of N.
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)
        


# final