# Example

"""
people = list()
data = list()
totmai = totmen = 0
for c in range(0, 3):
    data.append(str(input("Name: ")).capitalize().strip())
    data.append(int(input("Your age: ")))
    people.append(data[:])
    data.clear()
for p in people:
    if p[1] >= 21:
        print(f'{p[0]} Biggest of age')
        totmai+=1
    else:
        print(f"{p[0]} Smaller of age")
        totmen +=1
print(f'We have {totmai} biggest and {totmen} smaller of age.')
"""

# Challenge 084

"""
people = []
listpeople = []
biggestweight = []
smallerweight = []
while True:
    people.append(str(input("Name: ")).strip().capitalize())
    people.append(float(input("Weight: ")))
    listpeople.append(people[:])
    people.clear()
    stop = str(input("Want continue?: [YES] "))[0].upper().strip()
    if stop != 'Y':
        break
print(f"The number of people in the list is {len(listpeople)}")    
for c in listpeople:
    if c[1] > 80:
        if len(biggestweight) <= 2:
            biggestweight.append(c[0])
            biggestweight.append(c[1])          
    if c[1] < 70:
        if len(biggestweight) <= 2:
            smallerweight.append(c[0])
            smallerweight.append(c[1])
print(f"biggest weight peoples are {biggestweight}")
print(f"smaller weight peoples are {smallerweight}")
"""

### Second resolution 084 ###

"""
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("nome: ")).capitalize().strip())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break
print('-_' * 30)
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai:.2f}kg')
print(f'O menor peso foi de {men:.2f}kg')
"""

# Challenge 085

"""
lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-' * 30)
lista[0].sort()
lista[1].sort()
print(f"The values pair typed were: {lista[0]}")
print(f"The values odd typed were: {lista[1]}")
"""



# Challenge 086 and 087 Matriz

"""
lista = [ [0,0,0] , [0,0,0] , [0,0,0] ]
soma = 0
column = 0
bigrow = 0
for g in range(0,3):
    for p in range(0, 3):
        lista[g][p] = int(input(f"Enter any number for [{g}, {p}]: "))  
for i in range(0, 3):
    for c in range(0, 3):
        if lista[i][c] % 2 == 0:
            soma += lista[i][c]
        if c == 2:
           column += lista[i][c] 
        if i == 1:
            if c == 0:
                bigrow = lista[i][c]
            if lista[i][c] > bigrow:
                bigrow = lista[i][c]
        print(f"\033[1;35m[ {lista[i][c]} ]\033[m", end='')
    print()
print(f"The sum of the values pair is: {soma}")
print(f"The sum of the values  of third column is: {column}")
print(f"The biggest value of second line is: {bigrow}")
"""

# Challenge 088

"""
from random import randint
lista = []
plista = []
games = int(input("Enter the number of times you going play: "))
for c in range(0, games):
    for g in range(0, 6):
        v = randint(1,60)
        while v in plista:
            v = randint(1,60)
        plista.append(v)
    plista.sort()
    lista.append(plista[:])
    plista.clear()
for b, i in enumerate(lista):
    print(f"\033[1;34mJogo {b+1}: {i}\033[m")
"""

# Challenge 089 

"""
lista = []
while True:
    
    name = str(input("Enter your name: ")).capitalize().strip()
    n1 = float(input("Enter your 1º average: "))
    n2 = float(input("Enter your 2º average: "))
    lista.append([name, n1, n2])
    stop = str(input("Enter [Y] to stop or type anything to continue! ")).strip().upper()[0]
    if stop in 'Yy':
        break
print("-" * 30)
print(f"{'No.':<4}{'NAME':<10}{'AVERAGE':>10}")
print("-" * 30)
for b, i in enumerate(lista): 
    print(f"\033[1;33m{b:<4}{i[0]:<10}{(i[1]+i[2]) / 2:>8.1f}\033[m")
while True:
    print('''
    [1] Show all datas
    [2] Show one student notes    
    [3] To out
        ''')
    s = int(input('Enter your option: '))
    if s == 1:
        print("-" * 30)
        print(f"{'No.':<4}{'NAME':<10}{'AVERAGE':>10}")
        print("-" * 30)
        for b, i in enumerate(lista): 
            print(f"\033[1;34m{b:<4}{i[0]:<10}{(i[1]+i[2]) / 2:>8.1f}\033[m")
    if s == 2:  
        code = int(input("Enter student code: "))
        print(f"\033[1;31m{lista[code][0]}  1º {lista[code][1]} 2º {lista[code][2]}\033[m")
    if s == 3:
        print('Shutting down')
        break
print("check back often")
"""
        
            



    