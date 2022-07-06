colors = {
    'black': '\033[1;30;107m',
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'blue': '\033[1;34m',
    'magenta': '\033[1;35m',
    'cyano': '\033[1;36m',
    'gray': '\033[1;37m',
    'white': '\033[1;97m',
    'clean': '\033[m',
}
"""
print(cores['red'],"HelloWorld",cores['clean'])
print(cores['green'],"HelloWorld",cores['clean'])
print(cores['yellow'],"HelloWorld",cores['clean'])
print(cores['gray'],"HelloWorld",cores['clean'])
"""

# Challenge 036 Nested Condition

"""
from time import sleep

print('Enter the details for the loan')
house = float(input('Enter the house value: '))
salary = float(input('Enter your current salary: '))
year = float(input('Enter how many years you want to pay: '))
installment = year * 12
installment = house / installment
approval = salary * 0.3
print(f'This house value is {cores["red"]}{house:.2f}{cores["clean"]}, your salary is \033[1;30m{salary:.2f}\033[m and your payment time is \033[1;35m{year:.0f}\033[m Years')
print('\033[1;35mProcessing your request...\033[m')
sleep(5)
print(f'Your installment is R$\033[1;32m{installment:.2f}\033[m')
print(f'Your pass rate is R$\033[1;31m{approval:.2f}\033[m')

if installment < approval:
    print('Was successfully approved!')
else:
    print('Your request was not approved...')
"""

# Challenge 037

"""
num = int(input('Enter an integer number: '))
choice = ''
while choice != 'B' and choice != 'O' and choice != 'H':
    choice = str(input(
        'Enter conversion base Binary, Octal, Hexadecimal (B/O/H): ')).strip().upper()
    print(choice)
if choice == 'B':
    print(bin(num))
elif choice == 'O':
    print(oct(num))
else:
    print(hex(num))
"""

# Challenge 038

"""
n1 = int(input('Enter an number: '))
n2 = int(input('Enter an another number: '))

if n1>n2:
    print('The first number is bigger')
elif n2>n1:
    print('The second number is bigger')
else:
    print('Both numbers are the same')

"""

# Challenge 039

"""
age = int(input('Enter your age: '))

if age == 18:
    print("\033[1;32mIt's time to enlist in the military\033[m")
elif age < 18:
    lack = 18 - age
    print(f'\033[1;34mlack{lack} years to enlist military\033[m')
else:
    enlist = age - 18
    print(
        f'\033[1;31m{enlist} years have passed since enlistment time!!!\033[m')
"""

# Challenge 040

"""
m1 = float(input('Enter your note in math: '))
m2 = float(input('Enter your note in english: '))

middle = (m1+m2) / 2

if middle >= 7:
    print('\033[1;32;40mAproved\033[m')
elif middle >= 5:
    print('\033[1;33;40mRecuperation\033[m')
else:
    print('\033[1;31;40mDisapproved\033[m')
"""

# Challenge 041

"""
year = int(input('Enter your year of birth: '))
yourage = 2022 - year
if yourage < 10:
    print(cores['blue'],'Little',cores['clean'])
elif yourage < 15:
    print(cores['yellow'],'Childish',cores['clean'])
elif yourage < 20:
    print(cores['cyano'],'Junior',cores['clean'])
elif yourage == 20:
    print(cores['white'],'Senior', cores['clean'])
else:
    print(cores['red'],'Master',cores['clean'])
"""

# Challenge 042

"""
n1 = float(input('Enter the first side of a triangle: '))
n2 = float(input('Enter the second side of a triangle: '))
n3 = float (input('Enter a third side of a triangle: '))

if n1 < n2+n3 and n2 < n3+n1 and n3 < n1+n2:
    if n1 == n2 and n1 == n3 and n3 == n2:
        print('Equilteral')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('This is not a triangle')

"""

# Challenge 043

"""
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))
imc = weight / height**2

if imc < 18.5:
    print(f"{cores['red']}Low of weight IMC {imc:.2f}{cores['clean']}")
elif imc <= 25:
    print(f"{cores['green']}Ideal weight IMC {imc:.2f}{cores['clean']}")
elif imc <= 30:
    print(f"{cores['magenta']}Overweight IMC {imc:.2f}{cores['clean']}")
elif imc <= 40:
    print(f"{cores['yellow']}Obesity IMC {imc:.2f}{cores['clean']}")
else:
    print(f"{cores['red']}Morbid obesity IMC {imc:.2f}{cores['clean']}")
"""

# Challenge 044

"""
cost = float(input('Enter product price: '))
costten = cost * 0.9
costfive = cost * 0.95
costtwenty = cost * 1.2
print(f'{cores["yellow"]}Payment form{cores["clean"]}: ')
print(f'Money = price -10%: R${costten:.2f}')
print(f'Credit 1x = price -5%: R${costfive:.2f}')
print(f'Credit 2x = Normal price: R${cost:.2f}')
print(f'Credit 3x or more = +20%: R${costtwenty:.2f}')
paymentform = str(input(
    'Enter the payment form: \033[1;34m(Money/Credit)\033[m ')).strip().upper()
if paymentform == 'MONEY':
    print(
        f'Payment form: Money {cores["green"]}R${costten:.2f}{cores["clean"]}')
elif paymentform == 'CREDIT':
    creditpaymentform = str(input(
    'Enter the installment method: (1x/2x/3x) ')).strip().upper()
    if creditpaymentform == '1X':
        print(f'Payment form: Credit 1x {cores["green"]}R${costfive:.2f}{cores["clean"]}')
    elif creditpaymentform == '2X':
        print(f'Payment form: Credit 2x {cores["green"]}R${cost:.2f}{cores["clean"]}')
    elif creditpaymentform == '3X':
        print(f'Payment form: Credit 3x {cores["green"]}R${costtwenty:.2f}{cores["clean"]}')
"""

# Challenge 046 Jokenpô

"""
from random import randint

machine = randint(1,3)
print(f'{colors["white"]}JOKENPÔ{colors["clean"]}')
scissor = 'Scissor'
stone = 'Stone'
paper = 'Paper'
print(f'{colors["red"]}Try to beat me{colors["clean"]}')

if machine == 1:
    player = str(input('\033[1;33mEnter your play, Paper/Stone/Scissor: \033[m')).strip().upper()
    if player == 'PAPER':
        print(f'{colors["red"]}You lose! MUAHAHAHA, I play {scissor} and you play {paper}{colors["clean"]}!')
    elif player == 'STONE':
        print(f'{colors["green"]}You beat me! I play {scissor} and you play {stone}{colors["clean"]}!')
    elif player == 'SCISSOR':
        print(f'{colors["white"]}Draw! I play {scissor} and you play {stone}{colors["clean"]}!')
if machine == 2:
    player = str(input('\033[1;33mEnter your play, Paper/Stone/Scissor: \033[m')).strip().upper()
    if player == 'STONE':
        print(f'{colors["red"]}You lose! MUAHAHAHA, I play {paper} and you play {stone}{colors["clean"]}!')
    elif player == 'SCISSOR':
        print(f'{colors["green"]}You beat me! I play {paper} and you play {scissor}{colors["clean"]}!')
    elif player == 'PAPER':
        print(f'{colors["yellow"]}Draw! I play {paper} and you play {paper}{colors["clean"]}!')
if machine == 3:
    player = str(input('\033[1;33mEnter your play, Paper/Stone/Scissor: \033[m')).strip().upper()
    if player == 'SCISSOR':
        print(f'{colors["red"]}You lose! MUAHAHAHA, I play {stone} and you play {scissor}{colors["clean"]}!')
    elif player == 'PAPER':
        print(f'{colors["green"]}You beat me! I play {stone} and you play {paper}{colors["clean"]}!')
    elif player == 'STONE':
        print(f'{colors["yellow"]}Draw! I play {stone} and you play {stone}{colors["clean"]}!')     
"""


