# by Daniel O'Prey

from sys import exit

def fib_digits(digits, seq, n1, n2):
    """
    Print the Fibonacci sequence to the number of digits specified by the user
    """

    if digits > 0:
        n0 = n1 + n2
        n2 = n1
        n1 = n0
        seq += str(n0) + ", "
        fib_digits(digits - 1, seq, n1, n2)
    else:
        print(seq[:-2])
        inp_user()

def inp_user():
    """
    Takes an input from the user, exception handles until its an integer and then calls fib_digits
    """

    try:
        fib_digits(int(input('How many digits? ')), "", 1, 0)
    except ValueError:
        print('Please enter a number')
        inp_user()
    except:
        exit()
        
if __name__ == '__main__':
    inp_user()
