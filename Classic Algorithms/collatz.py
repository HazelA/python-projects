# by Daniel O'Prey

def collatz(num, steps):
    """
    Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
    """
    
    if num == 1:
        print('Completed in', steps, 'steps')
        inp_user()
    
    if num % 2 == 0:
        print('Step', steps, ': ', int(num), 'is even, dividing by 2')
        num /= 2
        collatz(num, steps + 1)
    else:
        print('Step', steps, ': ', int(num), 'is odd, multiplying by 3 and adding 1')
        num = num * 3 + 1
        collatz(num, steps + 1)

def inp_user():
    """
    Takes an input from the user, exception handles until its an integer and then calls fib_digits
    """

    try:
        num = int(input('Please enter a number larger than 1: '))
        if num > 1:
            collatz(num, 1)
        else:
            print('The number must be larter than 1')
            inp_user()
    except ValueError:
        print('Please enter a number larger than 1')
        inp_user()
    except:
        exit()
        
if __name__ == '__main__':
    inp_user()
