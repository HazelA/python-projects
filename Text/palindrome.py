# by Daniel O'Prey

def is_palindrome():
    """
    Take a string the user entered and print it in reverse
    """

    string = input('What text would you like to reverse? ')
    
    if string.lower() == string[::-1].lower():
        print('Yes, "', string, '" is a palindrome')
    else:
        print('No, "', string, '" backwards is "', string[::-1], '"')

    is_palindrome()

if __name__ == '__main__':
    is_palindrome()
