#Prime Factors



def prime_factors():
    user_num = input("Enter a number: ")
    results = []
    n, i = user_num, 2
    while i * i < n:
        while n % i == 0:
            results.append(i)
            n = n / i
        i += 1
    return results
    
print prime_factors()
    
        
    



