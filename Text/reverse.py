# by Daniel O'Prey

def reverse_string():
	"""
	Take a string the user entered and print it in reverse
	"""

    print(input('What text would you like to reverse? ')[::-1])
    reverse_string()

if __name__ == '__main__':
    reverse_string()
