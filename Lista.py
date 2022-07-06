"""
# Primeiro contato com lista

num = [2, 5, 9, 1]
num[3] = 5
num.append(7)
num.sort(reverse=True)
num.insert(2,12)
num.sort()
num.pop(2)
if 4 in num:
 num.remove(4)
else:
    print('Não encontrado')
print(len(num))
print(num)


# Segundo contato com listas
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'{c}º = {v}')
"""

# Challenge 078 Listas + input

"""
lista = []
for c in range(0,5):
    lista.append(int(input(f"\033[1;35mEnter a random number {c}º: \033[m")))
print(f'You typed these values: {lista}')
print(f"\033[1;34mThe biggest number you've typed is {max(lista)} and its index are \033[m")
for i, v in enumerate(lista):
    if v == max(lista):
        print(f"\033[1;34m{i} \033[m", end=' <- ')
print()
print(f"\033[1;31mThe smaller number you've typed is {min(lista)} and its index are \033[m")
for i, v in enumerate(lista):
    if v == min(lista):
        print(f"\033[1;31m{i} \033[m", end=' <- ')
"""


# Challenge 079 Lista + append

"""
lista = []
while True:
    ni = int(input('\033[1;36mEnter any number: [Enter 999 to stop] \033[m'))
    if ni == 999:
        break
    if ni in lista:
        print('\033[1;33mThis value is already in the list enter another number...\033[m')
    else:
        lista.append(ni)
print(f'\033[1;31mYou typed these values: {lista}\033[m')
lista.sort()
print(f'\033[1;31mYour values in sort are: {lista}\033[m')
"""

# Challenge 080 bubble sort?

"""
lista = []
for i in range(0,5):
    ni = lista.append(int(input('\033[1;36mEnter any number: \033[m')))
print(f'\033[1;31mYou typed these values: {lista}\033[m')
for g in range(4,-1, -1):
    for f in range(0,g):
        if lista[f] > lista[f+1]:
            change = lista[f]
            lista[f] = lista[f+1]
            lista[f+1] = change 
print(f'\033[1;31mThe values which you typed in order are: {lista}\033[m')
"""

### Second resolution 081 ###

"""
lista = []
for c in range(0, 5):
    n = int(input('\033[1;36mEnter any number: \033[m'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos +=1
print(f'\033[1;31mThe values which you typed in order are: {lista}\033[m')
"""

# Challenge 081 

"""
lista= []
while True: 
    lista.append(int(input("Enter any number: ")))
    stop = str(input("You want continue? [YES/NO]")).strip().upper()[0]
    if stop == "Y":
        break
print(f"The numbers you had typed are: {len(lista)}")
if 5 in lista:
    print(f"Five has found in list index {lista.index(5)}")
else:
    print(f"Five was not found in list")
lista.sort(reverse=True)
print(f"The list in order desc is: {lista}") 
"""

# Challenge 082 

"""
lista = []
listapair = []
listaodd = []
while True:
    ni = int(input("Enter any number: "))
    lista.append(ni)
    if ni % 2 == 0:
        listapair.append(ni)
    else:
        listaodd.append(ni)
    stop = str(input("You want continue? [YES/NO]")).strip().upper()[0]
    if stop == "Y":
        break
print(f"list all: {lista}")
print(f"list pair: {listapair}")
print(f"list odd: {listaodd}")
"""

# Challenge 083

"""
string = str(input("Enter any expression: ")).strip()
p1 = string.count('(')
p2 = string.count(')')
if p1 == p2:
    if "(" in string:
        if ")" in string[-1]:
            print(f"{string} is the in correct order")
        else:
            print(f"{string} It's not in the correct order")
    else:
        print(f"{string} It's not in the correct order")
else:
    print(f"{string} It's not in the correct order")
"""