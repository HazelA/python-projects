from sympy.mpmath import mp
from sys import exit

def pi_digits():
    """
    Print pi to the number of digits specified by the user
    """

    try:
        mp.dps = int(input('How many digits? '))
        print(mp.pi)
    except NameError:
        print('Please enter a number')
    except:
        exit()

    pi_digits()

pi_digits()
