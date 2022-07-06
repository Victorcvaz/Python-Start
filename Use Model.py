# Segunda Aba
# Módulos
###

# Primeira importação, biblioteca Math(Matemática)
# controlando casas decimais :.0f é igual á 0 float

"""
import math

num = int(input('Digite um número para saber a raiz: '))
raiz = math.sqrt(num)

print(f'A raiz de {num:.0f} é {raiz:.2f}')
"""

# Importando duas bibliotecas, treinando math e random... testes

"""
import math
import random
numram = random.random()
num = random.randint(1, 10)
print(num)
print(numram)
print(math.floor(numram))
print(math.ceil(numram))
"""

# Desafio 016 Usando a biblioteca math

"""
import math

numI = float(input('Digite um número real: '))

print(math.floor(numI))
print(math.trunc(numI))
print(int(numI))
print(f'Número: {numI} \nNúmero int {numI:.0f}')
"""

# Desafio 017 Geometria
# Não resolvido! Resolvido 06/04/2022

"""
import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)

### Exemplo que é possível usar int,float e etc nesse método
print(f'A hipotenusa é {int(hip)}')

hi = math.hypot(co, ca)
print(f'Hipotenusa {hi:.2f}')

"""


# Desafio 019 Geometria Sin, Cos, Tan, Radians
# 06/04/2022 = usando from e especificando 

"""

from math import radians, sin, cos, tan

an = float(input('Digite o angulo: '))

seno = sin(radians(an))
coseno = cos(radians(an))
tang = tan(radians(an))

print(f'Ângulo: {int(an)}º \nSeno: {seno:.2f}\nCos: {coseno:.2f}\nTan: {tang:.2f}')

"""

# Desafio 020 Biblioteca RANDOM

"""
import random

aluno1 = input('Digite o nome do 1º aluno: ')
print(aluno1)
aluno2 = input('Digite o nome do 2º aluno: ')
print('\n',aluno1,'\n', aluno2)
aluno3 = input('Digite o nome do 3º aluno: ')
print('\n',aluno1,'\n', aluno2,'\n', aluno3)
aluno4 = input('Digite o nome do 4º aluno: ')
print('\n',aluno1,'\n', aluno2,'\n', aluno3,'\n', aluno4)

choice = random.randint(1,4)

if choice == 1:
    print(f'{aluno1} Limpará o quadro')
elif choice == 2:
    print(f'{aluno2} Limpará o quadro')
elif choice == 3:
    print(f'{aluno3} Limpará o quadro')
else:
    print(f'{aluno4} Limpará o quadro')
"""
# Segunda resolução Ex 20
"""
import random

lista = [ '', '', '', '']
for i in range(4):  
    lista[i] = input(f'Digite o nome do aluno que participará do sorteio Aluno {int(i)}: ')
    
escolhido = random.choice(lista)   
print(f'O aluno escolhido foi: {escolhido}')
"""

# Desafio 021 Random

"""
import random

aluno1 = input('Digite o nome do 1º aluno: ')
print(aluno1)
aluno2 = input('Digite o nome do 2º aluno: ')
print(f'{aluno1}, {aluno2}')
aluno3 = input('Digite o nome do 3º aluno: ')
print(f'{aluno1}, {aluno2}, {aluno3}')
aluno4 = input('Digite o nome do 4º aluno: ')
print(f'1º {aluno1}, 2º {aluno2}, 3º {aluno3}, 4º {aluno4}')


while True:
    choice1 = random.randint(1, 100)
    choice2 = random.randint(1, 100)
    choice3 = random.randint(1, 100)
    choice4 = random.randint(1, 100)
    if choice1 == choice2 or choice1 == choice3 or choice1 == choice4 or choice2 == choice3 or choice2 == choice4 or choice3 == choice4:
        choice1 = random.randint(1, 100)
        choice2 = random.randint(1, 100)
        choice3 = random.randint(1, 100)
        choice4 = random.randint(1, 100)
    else:
        break
print(f'{choice1}, {choice2}, {choice3}, {choice4}')
if choice1 > choice2 and choice1 > choice3 and choice1 > choice4:
    if choice2 > choice3 and choice2 > choice4:
        if choice3 > choice4:
            print(f'1º {aluno1}, 2º {aluno2}, 3º {aluno3}, 4º {aluno4}')
        else:
            print(f'1º {aluno1}, 2º {aluno2}, 3º {aluno4}, 4º {aluno3}')
    elif choice3 > choice2 and choice3 > choice4:
        if choice2 > choice4:
            print(f'1º {aluno1}, 2º {aluno3}, 3º {aluno2}, 4º {aluno4}')
        else:
            print(f'1º {aluno1}, 2º {aluno3}, 3º {aluno4}, 4º {aluno2}')
    else:
        if choice2 > choice3:
            print(f'1º {aluno1}, 2º {aluno4}, 3º {aluno2}, 4º {aluno3}')
        else:
            print(f'1º {aluno1}, 2º {aluno4}, 3º {aluno3}, 4º {aluno2}')

elif choice2 > choice3 and choice2 > choice4:
    if choice1 > choice3 and choice1 > choice4:
        if choice3 > choice4:
            print(f'1º {aluno2}, 2º {aluno1}, 3º {aluno3}, 4º {aluno4}')
        else:
            print(f'1º {aluno2}, 2º {aluno1}, 3º {aluno4}, 4º {aluno3}')
    elif choice3 > choice1 and choice3 > choice4:
        if choice1 > choice4:
            print(f'1º {aluno2}, 2º {aluno3}, 3º {aluno1}, 4º {aluno4}')
        else:
            print(f'1º {aluno2}, 2º {aluno3}, 3º {aluno4}, 4º {aluno1}')
    else:
        if choice1 > choice3:
            print(f'1º {aluno2}, 2º {aluno4}, 3º {aluno1}, 4º {aluno3}')
        else:
            print(f'1º {aluno2}, 2º {aluno4}, 3º {aluno3}, 4º {aluno1}')
elif choice3 > choice4:
    if choice1 > choice2 and choice1 > choice4:
        if choice2 > choice4:
            print(f'1º {aluno3}, 2º {aluno1}, 3º {aluno2}, 4º {aluno4}')
        else:
            print(f'1º {aluno3}, 2º {aluno1}, 3º {aluno4}, 4º {aluno2}')
    elif choice2 > choice1 and choice2 > choice4:
        if choice1 > choice4:
            print(f'1º {aluno3}, 2º {aluno2}, 3º {aluno1}, 4º {aluno4}')
        else:
            print(f'1º {aluno3}, 2º {aluno2}, 3º {aluno4}, 4º {aluno1}')
    else:
        if choice2 > choice3:
            print(f'1º {aluno3}, 2º {aluno4}, 3º {aluno2}, 4º {aluno3}')
        else:
            print(f'1º {aluno3}, 2º {aluno4}, 3º {aluno3}, 4º {aluno2}')
else: 
    if choice2 > choice3 and choice2 > choice1:
        if choice3 > choice1:
            print(f'1º {aluno4}, 2º {aluno2}, 3º {aluno3}, 4º {aluno1}')
        else:
            print(f'1º {aluno4}, 2º {aluno2}, 3º {aluno1}, 4º {aluno3}')
    elif choice3 > choice2 and choice3 > choice1:
        if choice2 > choice1:
            print(f'1º {aluno4}, 2º {aluno3}, 3º {aluno2}, 4º {aluno1}')
        else:
            print(f'1º {aluno4}, 2º {aluno3}, 3º {aluno1}, 4º {aluno2}')
    else:
        if choice2 > choice3:
            print(f'1º {aluno4}, 2º {aluno1}, 3º {aluno2}, 4º {aluno3}')
        else:
            print(f'1º {aluno4}, 2º {aluno1}, 3º {aluno3}, 4º {aluno2}')
            
"""

# Segunda resolução Ex 021

"""
import random

lista = [ '', '', '', '']
for i in range(4):  
    lista[i] = input(f'Digite o nome do aluno que participará do sorteio Aluno {int(i)}: ')
    
escolhido1 = random.choice(lista)
escolhido2 = random.choice(lista)
escolhido3 = random.choice(lista)
escolhido4 = random.choice(lista)
while escolhido2 == escolhido1:
    escolhido2 = random.choice(lista)
while escolhido3 == escolhido2 or escolhido3 == escolhido1:
    escolhido3 = random.choice(lista)
while escolhido4 == escolhido3 or escolhido4 == escolhido2 or escolhido4 == escolhido1:
    escolhido4 = random.choice(lista)
    
print(f'1º {escolhido1}')
print(f'2º {escolhido2}')
print(f'3º {escolhido3}')
print(f'4º {escolhido4}')
"""

# Terceira resolução Ex 021

"""
from random import shuffle

lista = [ '', '', '', '']
for i in range(4):  
    lista[i] = input(f'Digite o nome do aluno que participará do sorteio Aluno {int(i)}: ')

shuffle(lista)
print(lista)
"""

"""
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("zelda.mp3")
play(song)
"""

from playsound import playsound
playsound("zelda.mp3")

   



