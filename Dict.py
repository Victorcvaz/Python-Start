# Basic
"""
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade' : 22}
#print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k in pessoas.keys():
#    print(k)
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
"""

# Basic 2

"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['Sigla'])
"""

# Basic 3

"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# 1º print basic
# print(brasil)
## 2º print list
## for e in brasil:
##    print(e)
### 3º print dict
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
"""

# Challenge 090 Dict basic

"""
boletim = {}
boletim['name'] = str(input("name: ")).capitalize().strip()
boletim['average'] = float(input("average: "))
print(f"The name is: {boletim['name']}")
print(f"the average is: {boletim['average']}")
if boletim["average"] < 6:
    print("Reproved")
else:
    print("Approved")
"""

# Challenge 091 DOOOOOOOOOOOOOOOOOOOOOONE

"""
from time import sleep
from random import randint

roll = {}
listavalue = []
listaname = []
count = 1
for c in range(0,4):
    roll[f'Player{c+1}'] = randint(1,6)
for k, v in roll.items():
    sleep(1)
    print(f"\033[1;34m -->  {k} --> Roll {v}\033[m")
    listavalue.append(v)
    listaname.append(k)
for u in range(3, -1, -1):
    for j in range(0, u):
        if listavalue[j] < listavalue[j+1]:
            change = listavalue[j]
            listavalue[j] = listavalue[j+1]
            listavalue[j+1] = change
            change1 = listaname[j]
            listaname[j] = listaname[j+1]
            listaname[j+1] = change1
roll.clear()
print('-' * 30)
print(f"\033[1;35m{'Colocação':^30}\033[m")
print('-' * 30)
for s, g in enumerate(listavalue):
    roll[listaname[s]] = g
for k, v in roll.items():
    sleep(1)
    print(f"\033[1;97m {count}º Place -->  {k} ---> Dice {v}\033[m")
    count+=1
"""

### Second resolution 091 ###

"""
from random import randint
from time import sleep
from operator import itemgetter
game = {}   
rank = [] 
for c in range(0,4):
    game[f'Player{c+1}'] = randint(1,6) 
print('Drawn values:')
for k, v in game.items():
    print(f"{k} roll {v} in the dice")
    sleep(1)
rank = sorted(game.items(), key=itemgetter(1), reverse=True)
print("--" * 30)
print(" == RANkING PlAYERS == ")
for i, v in enumerate(rank):
    print(f"--> {i+1} place: {v[0]} with {v[1]}.")
    sleep(1)
"""
# Challenge 092 Done

"""
people = {}

people['name'] = str(input("Name: ")).strip().capitalize()
age = int(input("Your Age: "))
cpts = int(input("Work wallet number(enter 0 if you haven't): "))
people['birth'] = age
people['ctps'] = cpts
if cpts != 0 or cpts == '':
    contractyear = int(input("Your first contract year: "))
    people['year'] = contractyear   
    people['salary'] = float(input("Your salary: "))
    people['retirement'] = (35 + age) - (2022 - contractyear)
    for k, v in people.items():
        print(f"\033[1;34m{k} is {v}\033[m") 
else:   
    for c, l in people.items():
        print(f"\033[1;34m{c} is {l}\033[m")
"""

### Second Resolution 092 ###

"""
from datetime import datetime
datas = {}
datas['Name'] = str(input("Name: ")).strip().capitalize()
nas = int(input("Year of birth: "))
datas['Birth'] = datetime.now().year - nas
datas['Ctps'] = int(input("Work wallet number(enter 0 if you haven't): "))
if datas['Ctps'] != 0:
    datas['Contract'] = int(input("Contract year: "))
    datas['Salary'] = float(input("Your salary: "))
    datas['Retirement'] = datas['Birth'] + ((datas['Contract'] + 35) - datetime.now().year)
print('--' * 30)
for k, v in datas.items():
        print(f"\033[1;34m{k} is {v}\033[m") 
"""

# Challenge 093 dict + list


"""
gameplay = {}
kills = []
gameplay['Nome do personagem'] = str(input("Enter a character name: ")).capitalize().strip()
while gameplay["Nome do personagem"] == '':
    gameplay['Nome do personagem'] = str(input("Enter a character name: ")).capitalize().strip()
matches = int(input("Enter a matches plays with this character: "))
gameplay['Número de jogos'] = matches
for c in range(1, matches+1):
    count = int(input(f"Enter the number of kills you've had in the game {c}: "))
    kills.append(count)
gameplay['Número de mortes'] = kills
print(gameplay)
print('-' * 50)
for k, v in gameplay.items():
    print(f"The field {k} hav the value {v}")
('-' * 50)
print(f"The champion {gameplay['Nome do personagem']} played {gameplay['Número de jogos']} games")
for n, m in enumerate(kills):
    print(f"   -> In the game {n+1}, he made {m} kills")
print(f"Was a total of {sum(kills)} kills")
"""

# Challenge 094 

"""
people = []
person = {}
tot = 0
women = []
biggestofaverage = []
cad = int(input("How many people do you want check in: "))
for c in range(0, int(cad)):
    person['Nome'] = str(input("Name: ")).strip().capitalize()
    person['Sexo'] = str(input("Sex[M/F]: ")).strip().upper()[0]
    age =  int(input("Years old: "))
    tot += age
    person['Idade'] = age
    people.append(person.copy())
print(f"\033[1;35mThe total of people in list is: {len(people)}\033[m")
average = tot / cad
for g in people:
    for s, v in g.items():
        if s == 'Sexo' and v == 'F':
            women.append(g.copy())
        if s == 'Idade' and v > average:
            biggestofaverage.append(g.copy())
print('-' * 120)
print(f"\033[1;33mThe average years old is: {average:.1f}\033[m")
print('-' * 120)
for p, h in enumerate(women):
    for k, g in h.items():
            if k == 'Nome':
                print(f"\033[1;31mThe {p+1}º woman in the list is: {g}\033[m")
print('-' * 80)
for q, t in enumerate(biggestofaverage):
    print(f"\033[1;34m{q+1}º The list of people with years old biggest that average is: {t}\033[m")
print('-' * 120)


# Challenge 095  Last of dict?
# funcionar com vários campeões # FEITO!
# sistema de visualização #
# detalhes do aproveitamento #
"""

### Second Resolution 094 ###

"""
Person = {}
People = []
Sum = Avg = 0
while True:
    Person.clear()
    Person['Name'] = str(input('Nome: ')).strip().capitalize()
    while True:
        Person['Sex'] = str(input('Sex: [M/F] ')).upper()[0]
        if Person['Sex'] in 'MF':
            break
        print("Error! type correct caracters: [M/F]")
    Person['Birth'] = int(input('Birth: '))
    Sum += Person['Birth']
    People.append(Person.copy())
    while True:
        resp = str(input('You want to continue? [Y/N] ')).upper()[0]
        if resp  in 'YN':
            break
        print("Error! type correct caracters: [Y/N]")
    if resp == 'N':
        break
print('--' *30)
print(f"The total of people are {len(People)} in the list")
print('--' *30)
Avg = Sum / len(People)
print(f"The average of birth is of {Avg:5.2f} years")
print('--' *30)
print('The womans registered were ', end='')
print('--' *30)
for p in People:
    if p['Sex'] in 'Ff':
        print(f'{p["Name"]} <--', end='')
print()
print('--' *30)
print('List of people with age above the average')
for p in People:
    if p['Birth'] >= Avg:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('End, thank you for coming')

"""

# Challenge 095 

"""
from time import sleep
champs = []
champ = {}
KDA = []
averageKDA = []
Total = []
kills = dead = assist = 0
while True:
    champ['Champion'] = str(input(f"\033[1;97mChampion: \033[m")).strip().capitalize()
    Games = int(input("\033[1;35mHow many games do your play'd with this champion: \033[m"))
    champ['Games'] = Games
    for g in range(0, Games):
        print(f"\033[1;31mEnter Your Score in the Game [Kills/Dead/Assist]\033[m")
        KDA.append([int(input(f"\033[1;34m{g+1}º Game Kills: \033[m")),
                    int(input(f"\033[1;31m{g+1}º Game Dead: \033[m")),
                    int(input(f"\033[1;36m{g+1}º Game Assist: \033[m"))]) 
    for o, h in enumerate(KDA):
        kills += h[0]
        dead += h[1]
        assist += h[2]
    averageKDA.append([int(kills / len(KDA)), int(dead / len(KDA)), int(assist / len(KDA))])
    Total.append([kills, dead, assist])
    champ['KDA'] = KDA[:]
    champ['Average KDA'] = averageKDA[:]
    champ['Total'] = Total[:]
    kills = dead = assist = 0
    Total.clear()
    averageKDA.clear()
    KDA.clear()
    champs.append(champ.copy())
    champ.clear()
    stop = str(input("\033[1;31m [Enter/Espace] to Continue or anything for stop: \033[m"))
    if stop != '':
        break
while True:
    print('''\033[1;35m
        __________________________________
        |            Menu                |
        |--------------------------------|
        |   [1] View all Registers       | 
        |   [2] Best Scores              |
        |   [3] View the history of one  |
        |   [0] End                      |
        |________________________________|
        \033[m''')
    option = int(input(f"\033[1;33m[Enter a option]: \033[m"))
    if option == 0:
        break
    if option == 1:
        for l, i in enumerate(champs):
            print('______________________________')
            for k, v in i.items():
                print(f"\033[1;34m{k}: {v}\033[m")
                sleep(1)
    if option == 2:
        for le, li in enumerate(champs):
            for e, w in li.items():
                if li['Average KDA'][0][0] > li['Average KDA'][0][1]:
                    print(f"\033[1;31m{e}: {w}\033[m")
            sleep(5)    
    if option == 3:
        while True:
            print('\033[1;31m_\033[m'* 50)
            print(f"\033[1;31m{'Cod':<4}{'Name':<10}{'Avg KDA':^18}{'Total':^18}\033[m")
            print('\033[1;31m_\033[m'* 50)
            for ei, eu in enumerate(champs):
                print(f"\033[1;34m{ei:^4}{eu['Champion']:<10}{str(eu['Average KDA'][0]):^18}{str(eu['Total'][0]):^18}\033[m")
                print('\033[1;35m_\033[m'* 50)
            resp = int(input("\033[1;34mEnter a champion you want see or [-1] TO LEAVE]: \033[m"))
            while resp > len(champs)-1 or resp < -1:
                resp = int(input(f"\033[1;31mNot exist Champion with code {resp}! Try Again:[-1] TO LEAVE] \033[m"))
            if resp == -1:
                break
            for qi in range(0, champs[resp]['Games']):
                print('\033[1;33m_\033[m'* 50)
                print(f"\033[1;33m{champs[resp]['Champion']} in the Game {qi+1} did {champs[resp]['KDA'][qi]}.\033[m")
                print('\033[1;33m_\033[m'* 50)
                sleep(3)
print("\033[1;34mThank you for using this APP!\033[m")
print("\033[1;34mHave a good day!\033[m")
"""

### Second resolution 095 ###

"""
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na partida {c}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas [S/N].')
    if resp == 'N':
        break
print("-" * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- Levantamento do jogador {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No jogo {i+1} fez {g} gols.")
        print('-' * 40)
print("Volte Sempre")
"""