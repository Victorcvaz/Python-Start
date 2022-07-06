

"""
metodo!
#print("Olá, mundo!")

nome = input('Digite seu nome: ')
print("É um prazer te conhecer, {}!".format(nome))
 #ex atual
print(f"É um prazer te conhecer, {nome}!")
"""
# Aula 6 - Tipos Primitivos e Saída de Dados

# Verificando o tipo de dado
##n1 = int(input("Digite um valor: "))
## print(type(n1))
# Bool sem valor = False, com valor = True

# confirmar se é possível transformar em tipo primitivo, print(n.isnumeric())
# variável.isnumeric()    Ex<<<<

#### Lista de estudos de is< verificar dados!!

"""
n = input("digite algo: ")
print('O tipo primitivo desse valor é:', type(n))

print(n.isascii())
print(n.isdecimal())
print(n.isdigit())
print(n.isidentifier())
print(n.isprintable())
print('É alfanúmerico?', n.isalnum())
print('É alfabético?', n.isalpha())
print('É um número?', n.isnumeric())
print('Está em minúsculas?', n.islower())
print('Está em maiúsculas?', n.isupper())
print('Só tem espaço?', n.isspace())
print('Está capitalizada?', n.istitle())
"""

# operadores binários
## +, -, *, /, **, //, %
### = e ==, recebe e igualdade(comparação)

# ordem de precedência
## 1º () 2º ** 3º *, /, //, % 4º +, -

# potência # pow(4,5)

# Calcular a raiz, método\/
## 81**(1/2) Raiz quadrada
## 25**(1/3) Raiz cúbica

# É possível multiplicar strings
## print('='*20)

# Como dar espaços entre um dado no print
## ('Prazer em te conhecer {:20}!, nome)
### podendo usar, <, >, ^, =^
#### < inicia a esquerda, > inicia a direita
#### ^ Centraliza, =^ Centraliza e preenche com a casa antes do ^

# Não quebrar a linha 
## print('A soma é {}, o produto é:'end = ' ')
### ' ' Dando um espaço, porém na mesma linha

# Nova linha, \n

#  Exercício 006 Raiz quadrada, método de cálculo

"""
num = int(input('Digite um número: '))

dobro = num + num
triplo = dobro + num
raiz = int(num**(1/2))
print(f'o número é: {num}, dobro é: {dobro}, o triplo é: {triplo}')
print('A raiz é:', raiz)

"""
# Exercício 007 Cálculo de média

"""
n1 = int(input('Digite a sua nota: '))
n2 = int(input('Digite a outra nota: '))

media = (n1 + n2) // 2
print(f'A sua média é: {media}')
"""

# Exercício 008 Cálculo de unidades de medidas

"""
m = int(input('Digite a quantidade de metros: '))

cm = m * 100
mili = cm * 10
print('Metros:', m)
print('Centímetros:', cm)
print("Milímetros:", mili) 
"""
# Exercício 009 Tabuada usando while

"""
tabuada = int(input("Digite um número: "))
i=1
while i<=10:
    print(tabuada, 'X', i, '=', tabuada*i)
    i += 1
"""

# Exercício 010 Conversão em dolar, divisão inteira/resto de divisão

"""
reais = float(input('Digite o valor em reais para converter em dol: '))

dol = 3.27
totdol = reais // dol
sobra = reais % dol

print(f'Você pode comprar: {totdol} Dólares\n total de: {reais} Reais\n troco: {sobra}')
"""

# Exercício 011 Área e calculo de dimensão, parede

"""
altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area = altura * largura
tintanecessaria = area / 2
# cada litro de tinta pinta uma área de 2m²
print(f'A dimensão da sua parede é {altura}x{largura} a área {area}m², vai ser necessário: {tintanecessaria}L de tinta.')
"""

# Exercício 012 Porcentagem

"""
preco = float(input('Digite o valor do produto: '))
desconto5 = preco * 0.95
desconto15 = preco * 0.85
print(f"O valor do produto é {preco}0R$, com desconto: {desconto5}0R$ e desconto por cartão C&A: {desconto15}0R$")
"""

# Exercício 013 Porcentagem

"""
salario = int(input('Digite o seu salário: '))

aumento = salario * 1.15
print(f'O seu aumento será = {aumento}R$')
"""

# Desafio 008 Calcular medidas
## medidas km, hm, dam, m, dm, cm, mm

""" 
medida = float(input('Uma distância em metros: '))

cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a {cm}cm e {mm}mm')
"""

# Desafio 014 Calcular temperatura
"""
c = float(input('Informe a temporatura em ºC: '))
f = 9 * c / 5 + 32
print(f'A temporatura de {c}ºC corresponde a {f}ºF!')
"""

# Desafio 015 Calcular km e custos

"""
km = float(input('Ditite a quantidade de km percorrido: '))
dias = int(input('Digite a quantidade de dias de uso: '))

custodia = dias * 60
custokm = km * 0.15
total = custodia + custokm
print(f'O custo em dias é {custodia:.2f}R$ e o custo em km é {custokm:.2f}')
print(f'Total: {total:.2f}R$')
"""

