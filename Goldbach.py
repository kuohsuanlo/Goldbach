def isPrime(n):

    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def generatePrimeList(n,primelist):
    for i in range(n):
        if isPrime(i):
            primelist=primelist+[i]            
            #print i
            
    return primelist


def isComposedOf3Prime(n,primelist):
    max_prime_index=0    
    for i in range(len(primelist)):
        for j in range(len(primelist)):
            for k in range(len(primelist)):  
                if n ==primelist[i]+primelist[j]+primelist[k]:
                    return [i,j,k]
MAX_NUMBER = 100
primelist=[]
three_prime=[]
primelist = generatePrimeList(MAX_NUMBER,primelist)
for i in range(MAX_NUMBER):
    three_prime = isComposedOf3Prime(i,primelist)
    print three_prime[0]

#print primelist


