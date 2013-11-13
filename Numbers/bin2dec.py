# by Daniel O'Prey

def dec2bin(mod):
    bits = []
    
    while mod >= 1:
        bits.append(str(int(mod % 2)))
        mod = (mod - (mod % 2)) / 2
        
    return ''.join(bits)[::-1]

def bin2dec(mod):
    result = val
    print(val, 'in binary is', result)
    inp_user()

def inp_user():
    """
    Takes two inputs from the user, a value and which base that value is in then calls the appropriate helper function to convert it
    """
    
    global val
    
    if 'val' not in globals():
        try:
            val = int(input('What value would you like to convert? '))
        except ValueError:
            print('Value must be an integer')
            inp_user()
        except:
            exit()
    
    base = input('Would you like to convert to (d)ecimal or (b)inary? ')

    if base[:1].lower() == 'd': # could add check to see if val input contains anything other than 1s or 0s
        print(val, 'in decimal is', bin2dec(val))
        del val
        inp_user()
    elif base[:1].lower() == 'b':
        print(val, 'in binary is', dec2bin(val))
        del val
        inp_user()
    else:
        print('Please enter "d" for decimal to binary conversion and "b" for binary to decimal conversion')
        inp_user()
        
if __name__ == '__main__':
    inp_user()
