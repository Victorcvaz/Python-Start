# Challenge 072 Tupla básic

"""
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Enter a number between 0 and 20: '))
    if num >= 0 and num <= 20:
        break
print(f'{tupla[num]}')
"""

# Challenge 073 
"""
tupleugly = ('palmeiras', 'santos', 'vasco da gama', 'gremio', 'flamengo', 'corinthians', 'internacional', 'cruzeiro', 'sao paulo', 'atletico mineiro', 'botafogo', 'fluminense', 'coritiba', 'bahia', 'goias', 'guarani', 'sport', 'portugesa', 'atletico paranaense', 'vitoria')

for c in range(0, len(tupleugly)):
    if c < 5:
        if c == 0:
            print('\033[1;36m=\033[m' * 30)
            print('{:^30}'.format('\033[1;36mTop 5\033[m'))
            print('\033[1;36m=\033[m' * 30)
        print(f'{tupleugly[c]}')
        
    if c > 15:
        if c == 16:
            print('\033[1;35m=\033[m' * 30)
            print('{:^30}'.format('\033[1;35mLast 4\033[m'))
            print('\033[1;35m=\033[m' * 30)
        print(f'{tupleugly[c]}')
    if c == 19:
        print('\033[1;31m=\033[m' * 30)
        print('{:^30}'.format('\033[1;31mSorted List\033[m'))
        print('\033[1;31m=\033[m' * 30)
        print(f'{sorted(tupleugly)}')
    if c == 19:
        idi = tupleugly.index('corinthians')
        print('\033[1;33m=\033[m' * 30)
        print('{:^30}'.format('\033[1;33mPosition\033[m'))
        print('\033[1;33m=\033[m' * 30)
        print(f'{tupleugly[idi]} is in {idi}ª position')
"""

### Second Resolution 073 ### 
     #Slap in the face#

"""
tupleugly = ('palmeiras', 'santos', 'vasco da gama', 'gremio', 'flamengo', 'corinthians', 'internacional', 'cruzeiro', 'sao paulo', 'atletico mineiro', 'botafogo', 'fluminense', 'coritiba', 'bahia', 'goias', 'guarani', 'sport', 'portugesa', 'atletico paranaense', 'vitoria')

print('-=' * 15)
print(f'List of times: {tupleugly} ')
print('-=' * 15)
print(f'The 5 first are {tupleugly[0:5]}')
print('-=' * 15)
print(f'The 4 last are {tupleugly[-4:]}')
print('-=' * 15)
print(f'Sorted tuple: {sorted(tupleugly)}')
print('-=' * 15)
print(f'The Cruzeiro is in the {tupleugly.index("cruzeiro")}ª position')
print('-=' * 15)
"""

# Challenge 074 

"""
from random import randint

n1 = randint(0,100)
n2 = randint(0,100)
n3 = randint(0,100)
n4 = randint(0,100)
n5 = randint(0,100)
tupla = (n1,n2,n3,n4,n5)
print(tupla)
sorttupla = sorted(tupla)
print(f'Biggest {sorttupla[-1]} and Smaller {sorttupla[0]}')

### Second resolution ###

tupla2 = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print(tupla2)
print(f'Biggest {max(tupla2)} and Smaller {min(tupla2)}')
"""

# Challenge 075

"""
n1 = int(input('Enter the 1º number: '))
n2 = int(input('Enter the 2º number: '))
n3 = int(input('Enter the 3º number: '))
n4 = int(input('Enter the 4º number: '))
tupla = ( n1, n2, n3, n4 )
countnine = 0
print(f'\033[1;97mYou typed the values: {tupla}\033[m')
index3 = tupla.index(3)
print('\033[1;34mThe numbers even in the tuple is: \033[m')
for c in tupla:
    if c % 2 == 0:
        print(f'\033[1;34m{c}\033[m', end=' <- ')
    if c == 9:
        countnine+=1
print('')
print('\033[1;31m-\033[m' * 30)
print(f'\033[1;35mThe number of times nine appears is {countnine}\033[m')
print(f'\033[1;33mThe first index that three appears is {index3}\033[m')
"""

### Second resolution 075 ###

"""
tuplainput = (
    int(input('Enter the 1º number: ')),
    int(input('Enter the 2º number: ')),
    int(input('Enter the 3º number: ')),
    int(input('Enter the 4º number: ')))
print(f'\033[1;97mYou typed the values: {tuplainput}\033[m')
print(f'\033[1;35mThe number of times nine appears is {tuplainput.count(9)}\033[m')
if 3 in tuplainput:
    print(f'\033[1;33mThe first index that three appears is {tuplainput.index(3)}ª index\033[m')
else:
    print(f"\033[1;33mThe value 3 don't found\033[m")
print('\033[1;34mThe numbers even in the tuple is: \033[m')
for c in tuplainput:
    if c % 2 == 0:
        print(f'\033[1;34m{c}\033[m', end=' <- ')
"""

# Challenge 076

"""
tupla = (
        'Smartphone', 2200,
        'Banana', 12.90, 
        'Desktop', 12000, 
        'Pancake', 44.50, 
        'Relationship', 29.90, 
        'Ball', 80)
print('_' * 45)
print(f'{"TABLE OF PRICES":^45}')
print('_' * 45)
print('-' * 45)
for c in range(0, len(tupla), 2):
    print(f'\033[1;35m| {tupla[c]:.<30}R$ {tupla[c+1]:.2f}\033[m')
print('-' * 45)


### Second Resolution 076 ###

tupla1 = (
        'Smartphone', 2200,
        'Banana', 12.90, 
        'Desktop', 12000, 
        'Pancake', 44.50, 
        'Relationship', 29.90, 
        'Ball', 80)
for pos in range(0, len(tupla1)):
    if pos % 2 == 0:
        print(f'{tupla1[pos]:.<30}', end='')
    else:
        print(f'R$ {tupla1[pos]:>7.2f}')
"""
# Challenge 077

"""
tupla = ('palavra', 'appears', 'happened', 'Typed', 'Developer', 'Python', 'Firstjob', 'Futuro', 'Work', 'Free')
print('\033[1;31m_\033[m' * 50)
print(f'\033[1;31m{"TEXT ANALYSIS":^50}\033[m')
print('\033[1;31m_\033[m' * 50)
for c in range(0, len(tupla)):
    print(f'in the word \033[1;34m{tupla[c].upper()}\033[m we have', end=' -> ')
    for p in range(0, len(tupla[c])):
        if tupla[c][p].lower() in 'aeiou':
            print(f"\033[1;35m{tupla[c][p].upper()}\033[m", end=' ')
    print('')
    print('_' * 50)
"""

        
