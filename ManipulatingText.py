# Challenge 022 Manipulating Text

"""
nome = str(input('Digite o seu nome: ')).strip
fname = nome.split()
nospace = ''.join(fname)
print('Alalisando o seu nome...')
print(f'Olá {fname[0]}')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'A quantidade de letras do seu nome é {len(nospace)}')
print(f'Seu nome usando Join {nospace}')
print(f'Seu primeiro nome tem {len(fname[0])} Letras')
"""

### Second Resolution Challenge 022 ###

"""
n = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print(f'Seu nome em maiúscula é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
print(f'Seu nome tem ao todo {len(n) - n.count(" ")} letras')
print(f'Seu primeiro nome tem {n.find(" ")} Letras')

"""

# Challenge 023 Manipulating Text

"""
num = input('Digite um número de 0 á 9999: ')
if len(num) == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
elif len(num) == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')
elif len(num) == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
else:
    print(f'Unidade: {num[0]}')
"""

### Second Resolution Challenge 023 ###

"""
num = int(input('Digite um número de 0 á 9999: '))
u = num % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {int(u)}')
print(f'Dezena: {int(d)}')
print(f'Centena: {int(c)}')
print(f'Milhar: {int(m)}')
"""

# Challenge 024 Manipulating Text

"""
City = input('Digite o nome de uma Cidade: ')

question = City.upper().find('SANTO')
if question == 0:
    print('O nome da sua cidade começa com SANTO')
else:
    print('O nome da sua cidade não começa com SANTO')
"""

### Second Resolution Challenge 024 ###
"""

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

"""

# Challenge 025 Manipulating Text

"""
nomes = str(input('Digite o seu nome completo: ')).strip()
print('SILVA' in nomes.upper())
"""

# Challenge 025 Manipulating Text

"""
nomeS = input('Digite o seu nome completo: ')
t = len(nomeS) - 1
print('A quantidade de vezes que aparece A é', nomeS.upper().count('A'))
print('A primeira vez que o A aparece é no indice',nomeS.upper().find('A'))
while t > 0:
    if nomeS[t].upper() == 'A':
        print('A ultima posição em que A aparece é', t)
        break
    t -= 1
"""
### Second Resolution Challenge 025 ###

"""
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
"""

# Challenge 026 Manipulating Text

"""

nspt = input('Digite o seu nome: ')

lista = nspt.split()
print(f'Primeiro nome {lista[0]}')
print(f'Último nome {lista[-1]}')    

"""

### Second Resolution Challenge 026

"""
lista = str(input('Digite o seu nome: ')).strip()
lista = lista.split()
print(f'Muito prazer {lista[0]}')
print(f'Primeiro nome {lista[0]}')
print(f'Último nome {lista[-1]}')
"""


