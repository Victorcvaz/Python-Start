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
# Challenge 112 Reuse created module and validation
#  
from Package.Coin import coin
from Package.Dice import datas

show = n = i = d = 0

n = datas.format("Enter the price: R$ ")
i = datas.format("Enter the value you'll want to increase in percent: ")
d = datas.format("Enter the value you'll want to decrease in percent: ")
show = datas.validation("Do you want to show formatted values? [Y/N] ")
coin.summary(num=n, percenti=i, percentd=d, show=show)


