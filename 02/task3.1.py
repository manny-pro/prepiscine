import math 

n = int(input('Donnez moi un nombre n : '))

def check_odd_even(n):
    if n % 2 == 0:
        return print("even")
    else:
        return print("odd")
    
check_odd_even(n)
