# Funtion basic
"""
def Sum(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")

# Main Program
Sum(4, 5)
Sum(8, 9)
Sum(2, 1)
Sum(a=2, b=3)
Sum(b=13, a=7)
"""
## Mandatory both parameters
### Is it possible to alter this arguments order

###########################################################

# Function basic 2
"""
def Contador(*num):
    print(f"number of Numbers: {len(num)}")
    for valor in num:
        print(f"{valor} ", end='')
    print('FIM!')
    

# Main Program
Contador(2, 1, 7)
Contador(8, 0)
Contador(4, 4, 7, 6, 2)
"""
## *num transform the parameters in tuple, is it possible to send multi parameters
###

###########################################################

# Function basic 3
"""
def double(db):
    print(sum(db))
    for p in range(0, len(db)):
        db[p] *=2
    print(sum(db))

# Main Program
valores = [6, 3, 9, 1, 0, 2]
print(valores)
double(valores)
print(valores)
"""

###########################################################

# Function basic 4
"""
def Sum(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Sum of the values {valores} we've {s}")
    print(f"Sum of the values {valores} we've {sum(valores)}")
Sum(5, 2)
Sum(2, 9, 4)
"""

# Challenge 096 Function 

"""
def area(l, c):
    print(f"\033[1;34mThis land has {l * c}m²\033[m")

area(14, 25)
area(20, 25)
"""

# Challenge 097 

"""
def write(text):
    print('\033[1;33m~\033[m' * (len(text)+2))
    print(f"\033[1;34m{text:^{len(text)+2}}\033[m")
    print('\033[1;33m~\033[m' * (len(text)+2))
    
while True:
    write(str(input("Enter a any frase: ")).title())
    response = str(input("You want to continue? [Y/N] ")).strip().upper()[0]
    if response == 'N':
        break
"""

# Challenge 098 

"""
print('\033[4;33m~\033[m' * 60)
for c in range(1, 11):
    print(f"\033[1;32m{c}\033[m", end=' <- ')
print('')
print('\033[4;33m~\033[m' * 60)
for c in range(10, -1, -2):
    print(f"\033[1;37m{c}\033[m", end=' <- ')
print('')
print('\033[4;34m~\033[m' * 60)
print("Now is your time to customize the count")
print('\033[4;34m~\033[m' * 60)
def count(init, end, step):
    for g in range(init, end+1, step):
        print(f"\033[1;36m{g}\033[m", end=' <- ')
    print('')
    print('\033[4;33m~\033[m' * 60)
count(int(input("Enter the beginning of the count: ")),
int(input("Enter the end of the count: ")),
int(input("Enter a range to the count: ")))
"""

### Second resolution 098 ###

"""
from time import sleep

def count(b, e, s):
    if s < 0:
        s *= -1
    if s == 0:
        s = 1
    print("~" * 20)
    print(f"Count of {b} until {e} of {s} in {s}")
    sleep(2)
    if b < e:
        count = b
        while count <= e:
            print(f"{count} ", end="", flush=True)
            sleep(0.5)
            count += s
        print("End!")
    else:
        count = b
        while count >= e:
            print(f"{count} ", end='', flush=True)
            sleep(0.5)
            count -= s
        print("End!")

# Main Program
count(1, 10, 1)
count(10, 0, 2)
print("~~" * 20)
print("Now is your time of customize the count")
count(int(input("Beginning: ")), int(input("End: ")), int(input("Step: ")))
"""

#  Challenge 099

"""
from random import randint
from time import sleep
def Biggest(*num):
    bigbig = 0
    print('\033[1;34m_\033[m' * 40)
    print(f"Were passed the number of the values {len(num)}")
    print('\033[1;34m_\033[m' * 40)
    sleep(1)
    for g in (num):
        if bigbig == 0:
            bigbig = g
        if bigbig < g:
            bigbig = g
    print('\033[1;33m~\033[m' * 40)
    print(f"values typed: {num}")
    print(f"The biggest value within values typed: {bigbig}")
    print('\033[1;33m~\033[m' * 40)
    sleep(2)

Biggest(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),)
Biggest(randint(1,100),randint(1,100),randint(1,100),)
Biggest(randint(1,100),randint(1,100),)
"""

# Challenge 100

"""
from random import randint
from time import sleep


def PrizeDraw(list):
    for c in range(0,5):
        list.append(randint(1,10))
        print(f"Roll {c+1} is {list[c]}")
        sleep(1)
    print(f"\033[1;34mThe values typed on list were {list}\033[m")
    Sum(list)
def Sum(list):
    Sum = 0
    for c in list:
        if c % 2 == 0:
            Sum += c
    print(f"\033[1;33mThe sum of all values pair are\033m \033[4;31m{Sum}\033[m")
numbers = []
PrizeDraw(numbers[:])
"""
