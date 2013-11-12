# by Daniel O'Prey

def collatz(num):
    return None

def inp_user():
    """
    Takes an input from the user, exception handles until its an integer and then calls fib_digits
    """

    num = input('How many digits? ')
    if type(num) == int and num > 1:
        collatz(num)
    else:
        print('Please input an integer which is larger than one')
        inp_user()
        
if __name__ == '__main__':
    inp_user()
