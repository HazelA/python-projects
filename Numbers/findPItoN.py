#Find PI to the Nth digit
from math import pi

def find_PI(n):
    decimal_controller = "{0:."+str(n+1)+"}"
    answer = decimal_controller.format(pi)
    return answer

print find_PI(25)
    