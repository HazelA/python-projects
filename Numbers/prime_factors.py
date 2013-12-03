#Prime Factors

def prime_factors():
    user_num = input("Enter a number: ")
    results = []
    n, i = user_num, 2
    for i in range(2, n):
        while n % i == 0:
            results.append(i)
            n /= i
    return results
    
print prime_factors()
    
        
    



