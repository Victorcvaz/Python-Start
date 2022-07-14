# First exemple

"""
from ModulesExample import routine

num = int(input("Enter a number: "))
fat = routine.factorial(num)
print(f"\033[1;36mThe factorial {num}! is {fat}\033[m")
print(f"\033[1;34mThe double of {num} is {routine.double(num)}\033[m")
"""

# Second example of modules

"""
from routine import factorial, double

# Import not indicated but is a simplified method

num = int(input("Enter a number: "))
fat = factorial(num)
print(f"\033[1;36mThe factorial {num}! is {fat}\033[m")
print(f"\033[1;34mThe double of {num} is {double(num)}\033[m")
"""

# Package example INCOMPLETE

"""
from Package import Numbers

num = int(input("Enter a number: "))
fat = Numbers.factorial(num)
print(f"\033[1;36mThe factorial {num}! is {fat}\033[m")
print(f"\033[1;34mThe double of {num} is {Numbers.double(num)}\033[m")
"""

# Challenge 107 created module
# Challenge 108 Reuse created module 
# Challenge 109 Reuse created module 
# Challenge 110 Reuse created module
# Challenge 111 Reuse created module 
 
from Package.Coin import coin

show = n = i = d = 0
while True:
    n = input("Enter the price: R$ ")
    if n.replace('.', '', 1).isdigit() or n.replace(',', '', 1).isdigit():
        n = float(n.replace(',', '.'))
        break
    print("\033[1;31mError! type a value number!\033[m")
while True:
    i = input("Enter the value you'll want to increase in percent: ")
    if i.replace('.', '', 1).isdigit() or i.replace(',', '', 1).isdigit():
        i = float(i.replace(',', '.'))
        break
    print("\033[1;31mError! type a value number!\033[m")
while True:
    d = input("Enter the value you'll want to decrease in percent: ")
    if d.replace('.', '', 1).isdigit() or d.replace(',', '', 1).isdigit():
        d = float(d.replace(',', '.'))
        break
    print("\033[1;31mError! type a value number!\033[m")
while True:
    show = str(input("Do you want to show formatted values? [Y/N] ")).upper().strip()[0]
    if show in "YN":
        break
    print("\033[1;31mError! type only [Y/N]!\033[m")
"""
print(f"\033[1;34mThe half of {coin.coin(n, show=show)} is {coin.half(n, show=show)}\033[m")
print(f"\033[1;36mThe double of {coin.coin(n, show=show)} is {coin.double(n, show=show)}\033[m")
print(f"\033[1;34mIncreasing {i}% we've {coin.increase(n, i, show=show)}\033[m")
print(f"\033[1;36mreducing {d}% we've {coin.decrease(n, d, show=show)}\033[m")
"""
print(coin.summary(num=n, percenti=i, percentd=d, show=show))

