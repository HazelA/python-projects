# by Daniel O'Prey

def reverse_string():
    print(input('What text would you like to reverse? ')[::-1])
    reverse_string()

if __name__ == '__main__':
    reverse_string()
