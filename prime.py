#I plegde this assignment was done by myself
num=int(input("Enter a number: "))
print(" ")
print(f"Prime numbers below {num} are")
def prime_num():
    count_prime=0
    sum=0
    for n in range(2,num):
            for i in range (2,n):        
                if n%i==0:
                    break
            else:
                print(n)
                count_prime+=1
                sum+=n
    average=sum/count_prime
    print(" ")
    print(f"Prime numbers printed below {num} are",count_prime)
    print(" ")
    print("The sum of the prime numbers printed is",sum)
    print(" ")
    print("The average of the prime numbers is",average)
    
prime_num()
    
        
    
                
        
                
                
