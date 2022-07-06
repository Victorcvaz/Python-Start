# Challenge 066 Flag Break

"""
suM = count = 0
while True:
    num = int(input('\033[1;33mEnter a any number integer(Enter 999 to stop): \033[m'))
    if num == 999:
        break
    suM += num
    count +=1
print(f'\033[1;32mTotal of plays {count} and total of the sum {suM}\033[m')
"""

# Challenge 067 Break

"""
num = count = 0
print(f'\033[1;34mEnter a negative number for stop\033[m')
num = int(input('\033[1;31mEnter a first number: \033[m'))
while num < 0:
    print('-'*30)
    num = int(input('\033[1;31mEnter a first number: \033[m'))
    print('-'*20)
while count < 10:
    print(f'\033[1;33m[{num} x {count+1} = {num*(count+1)}]\033[m')
    if count == 9:
        print('-'*30)
        num = int(input('\033[1;31mEnter a new number: \033[m'))
        print('-'*30)
        count = -1
    if num < 0:
        break
    count += 1
"""

### Second resolution  067 ###

"""
while True:
    n = int(input('Quer ver a tabuada de qua valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Are Done!')
""" 
 
# Challenge 068 Game - break

"""
from random import randint
count = 0
print("\033[1;35mLet's play Even or Odd\033[m")
while True:
    desk = randint(0,100)
    player = int(input('\033[1;33mEnter your number to play: \033[m'))
    round1 = str(input('\033[1;34mChoice even or odd number: [E/O] \033[m')).strip().upper()[0]
    while round1 != 'E'and round1 != 'O':
        round1 = str(input('\033[1;34mChoice even or odd number: [E/O] \033[m')).strip().upper()[0]
    if round1 == 'E':
        if (player + desk) % 2 == 0:
            count +=1
            print(f'\033[1;31mDesktop play {desk} and Player play {player} --> {desk}+{player} = {desk+player} \033[m')
        else:
            break
    elif round1 == 'O':
        if (player + desk) % 2 == 0:
            break
        else:
            count+=1
            print(f'\033[1;31mDesktop play {desk} and Player play {player} --> {desk}+{player} = {desk+player} \033[m')
print(f'\033[1;35mYou win {count}x before losing!\033[m')
"""

# Challenge 069 

"""
count = 0
countm = 0
countwyearsold = 0
while True:
    print('\033[1;31m-\033[m' * 40)
    yearsold = int(input("\033[1;35mEnter how many years old your have \033[m"))
    print('\033[1;31m-\033[m' * 40)
    gender = str(input('\033[1;35mEnter your gender [M/F] \033[m')).strip().upper()[0]
    print('\033[1;31m-\033[m' * 40)
    while gender != 'M' and gender != 'F':
        gender = str(input('\033[1;35mEnter your gender [M/F] \033[m')).strip().upper()[0]
    if yearsold >18:
        count += 1
    if gender == 'M':
        countm += 1
    if gender == 'F' and yearsold < 20:
        countwyearsold += 1
    again = str(input('\033[1;35mDo you want to continue? [Yes/No] \033[m')).strip().upper()[0]
    while again != 'N' and again != 'Y':
        again = str(input('\033[1;35mDo you want to continue? [Yes/No] \033[m')).strip().upper()[0]
    if again == 'N':
        break
print('\033[1;34m-\033[m' * 55)
print(f'\033[1;32mPeople at biggest 18 years old {count}\033[m')
print(f'\033[1;32mtotal of men that were registered are {countm}\033[m')
print(f'\033[1;32mThe total of women what have 20 years old or smaller is {countwyearsold}\033[m')
print('\033[1;34m-\033[m' * 55)
"""

# Challenge 070 

"""
total = cost = cheap = 0
name = ''
print('''\033[1;35m
--------------------------------------
             Sale Cheap 
--------------------------------------       
      \033[m''')
while True:
    nam = str(input('\033[1;34mEnter the product name: \033[m')).strip().capitalize()
    price = float(input('\033[1;34mEnter the product price: \033[m'))
    total += price
    if price > 1000:
        cost += 1
    if cheap == 0:
        cheap = price
    else:
        if cheap > price:
            cheap = price
            name = nam
    stop = str(input('\033[1;34mDo you want to continue? [YES/NO] \033[m')).strip().upper()[0]
    if stop == 'N':
        break
print('''\033[1;35m
--------------------------------------
        Do you bought 
--------------------------------------       
      \033[m''')
print(f'\033[1;34mThe total spent on the purchase is {total:.2f}\033[m')
print(f'\033[1;34mThe Total of products which cost most of 1000R$ is {cost:.0f}\033[m')
print(f'\033[1;34mThe name of the product most cheap is {name} of {cheap:.2f}R$\033[m')    
"""

# Challenge 071

"""
note50 = note20 = note10 = note5 = note1 = 0
while True:
    print('''\033[1;35m
[------Cash Machine------]
    
    Available values:
        [ R$50 ]
        [ R$20 ]
        [ R$10 ]
        [ R$ 5 ]
        [ R$ 1 ]
    \033[m''')
    withdraw = int(input('\033[1;34mEnter the withdrawal amount: \033[m'))
    note50 = withdraw // 50
    note20 = (withdraw % 50) // 20
    note10 = withdraw % 50 % 20  // 10
    note5 =  withdraw % 50 % 20 % 10 // 5
    note1 = withdraw % 50 % 20 % 10 % 5 // 1
    print('\033[1;34m-\033[m' * 55)
    print(f'''\033[1;34m
    
        Note 50R$ {note50}   
        Note 20R$ {note20}      
        Note 10R$ {note10}   
        Note  5R$ {note5}    
        Note  1R$ {note1}    
        
           \033[m''')
    stop = str(input('\033[1;34mContinue? [YES/NO] \033[m')).upper().strip()[0]
    if stop == 'N':
        break 
print('\033[1;34m-\033[m' * 55)
print('''\033[1;35m
Are Done! 
Have a good day\033[m''')
"""

### Second resolution 071 ###

"""
print('=' * 30)
print('{:^30}'.format('BANCO DO VITÃO'))
print('=' * 30)
valor = int(input('Valor a sacar: R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total of {totced} cédulas of R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
"""
