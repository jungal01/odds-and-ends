"""
I wrote this file in my first semester of my computer science degree. This file was an experiment to see how division worked. In the first
iteration of this, I didn't have the divide by zero catch, to see why mechanical calculators handled 0/1 the way they did. The plan for this 
file before abandonment was to do this sort of thing to all mathematical operators like multiplication, addition, subtraction, powers, etc.
I lost interest before I reached that point, however.
"""


print('divisor', chr(247), 'dividend')
divisor = int(input('divisor: '))
dividend = int(input("dividend: "))

quotient = 0

if divisor == 0:
    print("Cannot divide by 0")

else:
    while dividend - divisor >= 0:
        quotient += 1
        dividend -= divisor
    
    remainder = str(round(dividend % divisor))    
    print(str(quotient), 'R' + remainder)
    
