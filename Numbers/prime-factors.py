# by Daniel O'Prey

def list_prime_factors(num):
    """
    Find the prime factors of a number specified by the user
    """
    
    orig_num = num
    prime_factors = []
    
    for i in range(2, num):
        while num % i == 0:
            if i not in prime_factors:
                prime_factors.append(i)
            num /= i
            
    if prime_factors == []:
        print(orig_num, 'does not have any prime factors')
    else:
        print('The prime factors of', orig_num, 'are:', prime_factors)
        
    inp_user()

def inp_user():
    """
    Takes an input from the user, exception handles until its an integer and then calls list_prime_factors
    """

    try:
        list_prime_factors(int(input('What number would you like to find the prime factors of? ')))
    except ValueError:
        print('Please enter a number')
        inp_user()
    except:
        exit()
        
if __name__ == '__main__':
    inp_user()
