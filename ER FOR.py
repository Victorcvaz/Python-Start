# Challenge 046

"""
from time import sleep 

for i in range(10, -1, -1):
    print('\033[1;31m',i,'\033[m')
    sleep(1)
"""
# Challenge 047

"""
from time import sleep

for p in range(1, 51):
    if p % 2 == 0:
        print('\033[1;34m',p,'\033[m')
        sleep(1)
"""
"""
### second resolution 047 ### poupar processamento
# metade do custo de processamento
for p in range(2, 51, 2):
    print('\033[1;34m',p,'\033[m')
"""

# Challenge 048

"""
soma = 0
count = 0
for j in range(1, 501, 2):
    if j % 3 == 0:
        count+=1
        soma += j
print('\033[1;32m',soma,'\033[m')
print('\033[1;31m', count , '\033[m')
"""

# Challenge 049

"""
mt = int(input('Enter a number for a Multiplication table: '))
for t in range(1, 11):
    mtable = t * mt
    print(f'\033[1;31m{mt}X{t}\033[m = \033[1;34m{mtable}\033[m')
"""

# Challenge 050

""" 
sumE = 0
for six in range(0,6):
    odd = int(input('Enter a number: '))
    if odd % 2 == 0:
        sumE += odd
    
print('\033[1;31m',sumE,'\033[m')   
"""

# Challenge 051 PA(Progressão Aritmética)

"""
firsterm = int(input('Type a first term: '))
reason = int(input('type a reason: '))
for c in range(1, 11):
    print('\033[1;34m',firsterm,'\033[m')
    firsterm += reason
"""

### Second resolution 051 ###

"""
firstterm = int(input('Enter first term: '))
razão = int(input('Enter reason: '))
décimo = firstterm + (10-1) * razão
for c in range(firstterm, décimo + razão, razão):
    print(f'{c}', end=' => ')
print('Are done!')
"""

# Challenge 052 Primo

"""
primo = int(input('Enter a prime number: '))
divider = 0
for p in range(1, primo+1):
    if primo % p == 0:
        divider += 1
if divider == 2:
    print('\033[1;35mHe is a prime number\033[m') 
else:
    print('\033[1;31mHe is not a prime number\033[m')
"""

# Challenge 053 Palíndromo

"""
pali = str(input('Enter a word: ')).strip().upper().split()
pali = ''.join(pali)
ln = len(pali)-1
e = 0
for st in range(ln, -1, -1): 
    if pali[st] != pali[e]:
        print('This word a not a palindrome')
        break
    if e == len(pali)-1:
        print('This word is a Palindrome')
    e += 1
"""

### Second resolution 053 ### Tratamento de String

"""
phrase = str(input('Enter a phrase: ')).strip().upper().split()
junto = ''.join(phrase)
inverso = junto[::-1]
print(f'\033[1;31mThe inverse of {junto} is {inverso}\033[m')
if inverso == junto:
    print('\033[1;33mWe have a Palindrome\033[m')
else:
    print("\033[1;32mWe don't have a Palindrome\033[m")
"""

# Challenge 054 

"""
smaller = 0
larger = 0
for i in range(1, 8):
    birth = int(input(f'Enter birth year witch the {i}ª person was born: '))
    if 2022 - birth > 20:
        larger += 1
    else:
        smaller += 1
print(f'\033[1;34m{smaller} peoples do not reach the age of majority\033[m')
print(f'\033[1;31m{larger} peoples are of age majority')
"""

### Second resolution 054 ### Time/Date

"""
from datetime import date
atual = date.today().year
smaller = 0
larger = 0
for i in range(1, 8):
    birth = int(input(f'Enter birth year witch the {i}ª person was born: '))
    if atual - birth > 20:
        larger += 1
    else:
        smaller += 1 
print(f'\033[1;34m{smaller} peoples do not reach the age of majority\033[m')
print(f'\033[1;31m{larger} peoples are of age majority')
"""

# Challenge 055 BubbleSort

"""
lista = [ 0, 0, 0, 0, 0 ]
for c in range(0, 5):
    lista[c] = float(input('Enter your weight: '))
for i in range(4, -1, -1):
    for g in range(0, i):
        if lista[g] > lista[g+1]:
            change = lista[g]
            lista[g] = lista[g+1]
            lista[g+1] = change

print(lista)
print(f'\033[1;31m{lista[len(lista)-1]:.2f}Kg was the larger weight of the list\033[m')
print(f'\033[1;97m{lista[0]:.2f}Kg was the smaller weight of the list\033[m')
"""
### Second resolution ### Maior e menor em lista

"""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Enter the weight of the {p}ª Person: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\033[1;31m{maior:.2f}Kg was the larger weight of the list\033[m')
print(f'\033[1;97m{menor:.2f}Kg was the smaller weight of the list\033[m')
"""
# Challenge 056 

"""
namelist = [0,0,0,0]
agelist = [0,0,0,0]
sexlist = [0,0,0,0]
middleage = 0
countwoman = 0
for c in range(0, 4):
    print(f'\033[1;36m---- {c+1}ª PESSOA ----\033[m')
    namelist[c] = str(input('Name: ')).strip().lower().title()
    agelist[c] = int(input('Birth date: '))
    sexlist[c] = str(input('Sex(M/F): ')).strip().upper()
for i in range(0,4):
    middleage += 2022 - agelist[i]
middleage /= 4
for g in range(0,4):
    for p in range(0,g):
        if agelist[p] > agelist[p+1]:
            change = agelist[p]
            agelist[p] = agelist[p+1]
            agelist[p+1] = change
            changen = namelist[p]
            namelist[p] = namelist[p+1]
            namelist[p+1] = changen
            changes = sexlist[p]
            sexlist[p] = sexlist[p+1]
            sexlist[p+1] = changes
for w in range(0,4):
    if sexlist[w] == 'F':
        if 2022 - agelist[w] < 20:
            countwoman += 1
print(f'\033[1;35mThe mean age of this group is {middleage}\033[m')
if sexlist[0] == 'M':
    print(f'\033[1;34mThe name of the eldest man is {namelist[0]}\033[m')
else:
    print(f'\033[1;34mThe name of the eldest woman is {namelist[0]}\033[m')
print(f'\033[1;36mThe result of women with smaller age of 20 years or less is {countwoman}\033[m')
print('\033[1;31m',namelist,'\033[m')
print('\033[1;31m',agelist,'\033[m')
print('\033[1;31m',sexlist,'\033[m')
"""
### Second resolution 056 ### 

"""
sumbirthage = 0
averageofbirthage = 0
largerageman = 0
nameold = ''
totalwoman = 0
for p in range(0,4):
    print(f'----- {p+1}ª PESSOA -----')
    name = str(input('Nome: ')).strip().title()
    theage = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    sumbirthage += theage
    if p == 0 and sex in 'M':
        largerageman = theage
        nameold = name
    if sex in 'M' and theage > largerageman:
        largerageman = theage
        nameold = name
    if sex in 'F' and theage < 20:
        totalwoman +=1
averageofbirthage = sumbirthage / 4
print(f'The average age of the group is of {averageofbirthage} years')
print(f'The oldest man has {largerageman} years old and his name is {nameold}')
if totalwoman < 1:
    print(f'We do not have women with 20 years old or less on the list')
elif totalwoman == 1:
    print(f'We have on list {totalwoman} woman which 20 years old or less')
else: 
    print(f'We have on list {totalwoman} women which 20 years old or less')
"""

