# by Daniel O'Prey

from datetime import datetime

now = datetime.now()

def calculate_year(years):
    """
    Recursively calculates the year in which you will be older than half the average age of your parents
    """
    
    if ((mumage + dadage + years * 2) / 4) >= youage + years:
        calculate_year(years + 1)
    elif years == 0:
        print("You are already over half your parents' average age!")
    else:
        print("In {0} you will be {1} and your parents' average age will be {2}".format(now.year + years, (youage + years), int((mumage + dadage + years * 2) / 2)))

def inp_user():
    """
    Takes three inputs from the user, their age, their mum's age, and their dad's age then passes them to the calculate_year function
    """
    
    global youage
    global mumage
    global dadage
    
    try:
        youage = int(input('How old are you? '))
        mumage = int(input('How old is your mum? '))
        dadage = int(input('How old is your dad? '))
        
        if mumage <= youage or dadage <= youage:
            print('Your parents must be older than you!')
            inp_user()
        else:
            calculate_year(0)
    except ValueError:
        print('Ages must be integers')
        inp_user()
    except:
        exit()
        
if __name__ == '__main__':
    inp_user()
