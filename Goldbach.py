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
    	if i%(n/100)==0:
			print 'Constructing Prime List : ',i*100/n+1,'%'
	
			
    return primelist


def isComposedOf3Prime(n,primelist):
    max_prime_index=0    
    prime_tuple_list=[]
    
    for i in range(len(primelist)):#0~499
    	if(n>primelist[i]):
    		max_prime_index=i
    		
    #print 'mpi : ',max_prime_index
    	
    for i in range(max_prime_index):
        for j in range(max_prime_index):
            for k in range(max_prime_index):  
                if n ==primelist[i]+primelist[j]+primelist[k]:
                    prime_tuple_list=prime_tuple_list+[(primelist[i],primelist[j],primelist[k])]
    return prime_tuple_list               
                 
                   
MAX_NUMBER = 50000
primelist=[]
three_prime=[0]

primelist = generatePrimeList(MAX_NUMBER,primelist)
print 'Number of Prime',len(primelist)
for i in range(MAX_NUMBER):
	if(i>5):
	    three_prime =isComposedOf3Prime(i,primelist)
	    print 'Number of 3Prime solutions of N=',i,' : ',len(three_prime)
	    #print three_prime[0] #Output first solution.
		
#print primelist


