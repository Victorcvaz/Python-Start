# Challenge 057 Simple while

"""
sex = str(input('\033[1;32mEnter your sex [M|F]: \033[m')).strip().upper()
while sex != 'S' and sex != 'M':
    print('\033[1;31mVerify your writing and type again\033[m')
    sex = str(input('\033[1;36mEnter your sex [M|F]: \033[m')).strip().upper()
"""

### Second resolution 057 ###

"""
sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Dados Inválidos. Informe Seu sexo: ')).strip().upper()[0]
print(f'Sex {sex} registrado com sucesso')
"""

# Challenge 058 Random Choice

"""
from random import randint
print('\033[1;34mI'm your computer and I dominate everything, if you don't get the number right I will destroy the world! MUAHAHA\033[m')
machine = randint(0, 10)
player = int(input('\033[1;32mWhat number did I think? \033[m'))
plays = 1
while player != machine:
    print('\033[1;31mTry Again\033[m')
    player = int(input('\033[1;32mWhat number did I think? \033[m'))
    plays += 1
print(f'\033[1;33mYou have used {plays} plays in this game\033[m')
print(f'\033[1;36m======= Congratulations, you win! I thought {machine} and you {player} =======\033[m')
"""

# Challenge 059 Calculator While

"""
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
operator = ''
while operator != 'LOUT':
    operator = str(input('\033[1;31mEnter an operator for: Sum, Multiply, Larger Number, New Numbers, Leave\033[m\033[1;36m[Sum/Mul/LN/NN/LOUT]: \033[m')).strip().upper()
    if operator == 'SUM':
        print(f'\033[1;34;41m{n1}+{n2} = {n1+n2}\033[m')
    if operator == 'MUL':
        print(f'\033[1;32;107mMul {n1}*{n2} = {n1*n2}\033[m')
    if operator == 'LN':
        if n1 > n2:
            print(f'\033[1;97;43m{n1} it larger than {n2}\033[m')
        else:
            print(f'\033[1;97;43m{n2} it larger than {n1}\033[m')
    if operator == 'NN':
        n1 = float(input('Enter the new first number: '))
        n2 = float(input('Enter the new second number: '))
        print(f'The new numbers are 1º{n1} and 2º{n2}')
"""

### Second resolution 059 ###

"""
n1 = int(input('First value: '))
n2 = int(input('Second Value: '))
option = 0
while option != 5:
    print('''\033[1;35m
[ 1 ] Sum
[ 2 ] Multiply
[ 3 ] Biggest
[ 4 ] New Numbers
[ 5 ] Leave
          \033[m''')
    option = int(input('\033[1;31m--> Enter option: <--\033[m'))
    if option == 1:
        print(f'\033[1;34;107m{n1}+{n2} = {n1+n2}\033[m')
    elif option == 2:
        print(f'\033[1;32;107mMul {n1}*{n2} = {n1*n2}\033[m')
    elif option == 3:
        if n1 > n2:
            print(f'\033[1;97;107m{n1} it biggest than {n2}\033[m')
        else:
            print(f'\033[1;97;107m{n2} it larger than {n1}\033[m')
    elif option == 4:
        print('\033[1;97mEnter the new numbers\033[m')
        n1 = int(input('\033[1;97mFirst number: \033[m'))
        n2 = int(input('\033[1;97mSecond number: \033[m'))
        print(f'\033[1;97mThe new numbers are 1º{n1} and 2º{n2}\033[m')
    elif option == 5:
        print('\033[1;34mGoing out...\033[m')
    else:
        print('Error! Try Again')
"""

# Challenge 060 Fatorial
 
"""
fat = int(input('Enter a number for the calculator factorial: ')) 
count = fat - 1
result = fat
while count > 1:
    result *= count 
    count -= 1
print(f'\033[1;35m{fat}! = {result}\033[m')
"""

### Second resolution ### Manipulate prints in lines

"""
fat = int(input('Enter a number for the calculator factorial: ')) 
c = fat
f = 1
print(f'Calculate {fat}! = ', end='')
while c > 0:
    print(f'{c}',end='')
    print(f' x ' if  c>1 else ' = ', end='')
    f *=c
    c-=1
print(f'{f}')
"""

# Challenge 061 PA While

"""
firstt = int(input('Enter a first term of PA: '))
reason = int(input('Enter a reason of PA: '))
count = 0
while count < 10:
    print(f'\033[1;34m{firstt}\033[m', end=' => ')
    firstt += reason
    count +=1
print('\033[1;31mAre Done!\033[m')
"""

# Challenge 062 PA While + Condition

"""
firstt = int(input('Enter a first term of PA: '))
reason = int(input('Enter a reason of PA: '))
count = 0
terms = 10
while count <= terms:
    print(f'\033[1;34m{firstt}\033[m', end=' => ')
    firstt += reason
    if count == terms:
        print('End')
        condition = str(input('\033[1;33mYou want to show more terms? \033[1;31m[Y/N]:\033[m \033[m')).strip().upper()
        if condition != 'N':
            terms += int(input('\033[1;31mEnter a number of terms to add: \033[m'))
    count +=1
print('\033[1;31mAre Done!\033[m')
print(f'\033[1;31m{count}\033[m')
"""

# Challenge 063 Fibonacci 
    
"""
fibo = int(input('\033[1;31mEnter terms of fibonacci: \033[m'))
fibo1 = 0
fibo2 = 1
fibo3 = 0
print('\033[1;34m0 -> 1 -> \033[m', end='')
while fibo >= 3:
    fibo3 = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo3
    print(f'\033[1;34m{fibo3}', end=' -> \033[m')
    fibo -=1
print('\033[1;33mEnd!\033[m')
"""

# Challenge 064 

"""
soma = count = response = 0
response = int(input(f'\033[1;35mEnter a number integer: \033[m'))
while response != 999:
    print('\033[1;34mEnter 999 to stop\033[m')
    count += 1
    soma += response
    response = int(input(f'\033[1;35mEnter a number integer: \033[m'))
print(f'\033[1;34mThe total is {soma} and the count of times your played is {count}\033[m')
"""
### Flag(condição de parada e não conta na contagem)

# Challenge 065


sumI = count = larger = smaller = average = 0
stop = ''
while stop != 'Y':
    response = int(input('\033[1;31mEnter an integer number: \033[m'))
    if count == 0:
        larger = response
        smaller = response
    else:
        if response > larger:
            larger = response
        if response < smaller:
            smaller = response
    count += 1
    sumI += response
    stop = str(input('\033[1;36mYou want stop? \033[1;35m[Y/N] \033[m\033[m')).strip().upper()[0]
average = sumI / count
print(f'\033[1;33mThe biggest number was {larger}\033[m')
print(f'\033[1;35mThe smaller number was {smaller}\033[m')
print(f'\033[1;34mThe average of numbers was {average:.2f}\033[m')    
