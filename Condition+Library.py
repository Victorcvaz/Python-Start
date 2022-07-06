# Challenge 028 Conditions compost/Random(randint)

"""
from random import randint

num = randint(0, 5)
print('Adivinhe o número de 0 á 5')
dado = int(input('Tente acertar: '))

if num == dado:
    print('Parabéns Você acertou!!!')
else:
    print('Você errou =/')
"""

### Second resolution Challenge 028 ###

"""
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
"""

# Challenge 029 simple conditions

"""
vel = int(input('Velocidade do carro Km/h: '))
print(f'A sua velocidade é {vel}Km/h')
multa = (vel - 80) * 7 
if vel > 80:
    print(f'Você foi multado, a multa vai custar R${multa:.2f}')
"""

### Second resolution challenge 029 ###

"""
vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    trafficticket = (vel-80) * 7
    print(f'Você deve pagar uma multa de R${trafficticket:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')

"""

# Challenge 030 criterion of divisibility 

"""
num = int(input('Digite um número: ')) 
if num % 2 == 0:
    print(f'{num:.0f} é Par')    
else: 
    print(f'{num:.0f} é Ímpar')
"""

# Challenge 031 Simple math calc

"""
dis = float(input('Digite distância percorrida: '))
print(f'A distância percorrida foi {dis:.2f}Km/h')
costverynear = dis * 0.50
costveryfar = dis * 0.45
if dis <= 200:
    print(f'O preço da viagem é R${costverynear:.2f}')
else:
    print(f'O preço da viagem é R${costveryfar:.2f}')
"""
    
# Challenge 032 Library func isleap

"""
from calendar import isleap

year = int(input('Digite um ano, Exemplo(1993): '))
if isleap(year):
    print(f'{year} É bissexto')
else:
    print(f'{year} Não é bissexto')
"""

# Challenge 033 Conditions Multiple


"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 > n3:
    if n2 > n3:
        print(f'O maior número é {n1} e o menor número é {n3}')
    else:
        print(f'O maior número é {n1} e o menor número é {n2}')
elif n2 > n3:
    if n3 > n1:
        print(f'O maior número é {n2} e o menor número é {n1}')
    else:
        print(f'O maior número é {n2} e o menor número é {n3}')
else: 
    if n2 > n1:
        print(f'O maior número é {n3} e o menor número é {n1}')
    else:
        print(f'O maior número é {n3} e o menor número é {n2}')
"""

### Second resolution Challenge 033 ###

"""
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor '))
c = int(input('Terceiro valor '))
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {int(menor)}')
print(f'O maior valor digitado foi {int(maior)}')
"""

# Challenge Math Simple

"""
salary = float(input('Digite o seu salário: '))
if salary > 1250.00:
    increase = salary*1.1
else:
    increase = salary*1.15
print(f'Seu salário é R${salary:.2f}, após o aumento será: R${increase:.2f}')
"""

# Challenge 035 Geometry

"""
r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))
tri = r1 + r2
print(f'R1: {r1}\nR2: {r2}\nR3: {r3}\nSoma R1+R2: {tri}')
if r1 + r2 > r3:
    print('É um triângulo')
else:
    print('Não é um triângulo')
"""

### Second resolution Challenge 035 ###

"""
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Podem formar um triângulo')
else:
    print('Não podem formar um triângulo')
"""