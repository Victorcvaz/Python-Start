# Python interactive help

## 1) help()
## 2) help no terminal
## 3) print(print.__doc__)

# Python Docstring

'''
def testing(testingDoc):
    """
    -> Description function
    :Param testingDoc: Description of parameter function
    -> Create by Victor Cesar Vaz. 
    """
    testingDoc
help(testing)
'''

# Python Optional Parameters

"""
def sum(a=0, b=0, c=''):
    '''
    -> Sum of three values and show the result
    :param a: first value
    :param b: Second value
    :param c: Third value
    -> Create by Victor Cesar Vaz.
    '''
    '''
    s = a + b + c
    print(f"Sum of the values {s}")
    '''
    print(f"values {a}, {b} and {c}")
sum(1,2)
sum()  
sum('Victor','Pedro')
"""

# Python Scope of variables

## case 1 testing global escope and local scope
## in this case a global and a local
"""
def tests(b):
    a = 8
    b += 4
    c = 2
    print(f"A inside {a}")
    print(f"B inside {b}")
    print(f"C inside {c}")

a = 5
tests(a)
print(f"A outside {a}")
print(f"B outside {b}")
print(f"C outside {c}")
"""
## case 2 global scope applicable to local scope

"""
def tests(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A inside {a}")
    print(f"B inside {b}")
    print(f"C inside {c}")

a = 5
print(f"A outside first output {a}")
tests(a)
print(f"A outside second output {a}")
"""

# Python return

"""
def Sum(a=0,b=0,c=0):
    s = a+b+c
    return s
    s = 0 # stop the function after call return
print(Sum(3,2,5), Sum(2,2), Sum(6))
r1 = Sum(15,10)
print(r1)
"""

# Python exercise basic 01

"""
def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f*=c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"the results are {f1}, {f2} and {f3}")

# Python exercise basic 02

def test(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
if test(int(input("Number: "))):
    print("Is pair")
else:
    print("Is Odd")
"""

# Challenge 101

"""
def vote(year):
    from datetime import datetime
    years = datetime.now().year - int(year)
    if years < 16:
        return f'\033[1;33mYour age is {years}, Vote Denied\033[m'
    elif years > 18 and years < 60:
        return f'\033[1;33mYour age is {years}, Mandatory vote\033[m'
    else:
        return f'\033[1;33mYour age is {years}, Optional Vote\033[m'
result = vote(input("Birth year: "))
print('\033[1;36m~\033[m' * (len(result)+4))
print(f"{result:^{len(result)+4}}")
print('\033[1;36m~\033[m' * (len(result)+4))
"""

# Challenge 102 

"""
def fatorial(fat, show=0):
    '''
    -> Calculate the factorial of one number
    :param fat: factorial the be calculate
    :param: (optional) show or not the count down
    :return: result of the calculate
    '''
    c = fat-1
    for f in range(c, 0, -1):
        fat *= f
        if show:
            print(f"\033[1;35m{f+1}!\033[m", end="\033[1;32m x \033[m")
    if show:
        print(f"\033[1;35m1!\033[m", end="\033[1;32m = \033[m")
    print(f"\033[1;31m{fat}\033[m")
fatorial(5, True)
help(fatorial)
"""

# Challenge 103

"""
def token(name=0, basket=0):
    print('\033[1;33m~\033[m' * 30)
    if name == '':
        print(f"\033[1;34m  Player not found\033[m", end=' ')
        if basket.isnumeric():
            print(f"\033[1;31m{basket}\033[m")
        else:
            print("\033[1;31m0 baskets\033[m")
    else:
        print(f"\033[1;34m{name:>16}\033[m", end=' ')
        if basket.isnumeric():
            print(f"\033[1;31m{basket}\033[m")
        else:
            print(f"\033[1;31m0 baskets\033[m")
    print('\033[1;33m~\033[m' * 30)
token(str(input("Enter your name: ")), input("Baskets in the game: "))
"""

### Second Resolution 103 ###

"""
p = 2
def token(game='unknown', basket=0):
    print('\033[1;36m~\033[m' * 60)
    print(f"\033[1;34m{f'The player {game} did {basket} basket(s) in the championship':^60}\033[m")
    print('\033[1;36m~\033[m' * 60)

# Main program
n = str(input("Name of player: "))
g = str(input("Number of baskets: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    token(basket=g)
else:
    token(n, g)
"""

# Challenge 104 

"""
def readint(int):
    while True:
        if int.isnumeric():
            break
        print("\033[1;31mError, enter a valid number!\033[m")
        int = input("Enter any number: ")
    print(f"\033[1;32mYou've typed \033[m\033[1;35m{int}\033[m")
readint(input("Enter any number: "))
"""

# Challenge 105

"""
dictpeople = {}
result = {}
def averageF(en, math, his, py, sit=0):
    while True:
        dictpeople['English'] = en
        dictpeople["Math"] = math
        dictpeople["History"] = his
        dictpeople["Python"] = py
        print('\033[1;33m~\033[m' * 65)
        print(f"\033[1;34m{dictpeople}\033[m")
        print('\033[1;33m~\033[m' * 65)
        while True:
            response = str(input("All notes are okay? [Y/N] ")).upper().strip()[0]
            if response in "Y":
                break
            else: 
                en = float(input("Enter your english note again: "))
                math = float(input("Enter your math note again: "))
                his = float(input("Enter your históry note again: "))
                py = float(input("Enter your python note again: "))
                dictpeople.clear()
                print("\033[1;31m Notes updated\033[m")
                break
        if response == "Y": 
            break 
    tot = biggest = smaller = average = 0
    for k, v in dictpeople.items():
        tot += 1
        average += v
        if k == "English":
            biggest = v
            smaller = v
        if biggest < v:
            biggest = v
        if smaller > v:
            smaller = v
    average /= tot
    result ['Total'] = tot
    result['Biggest'] = biggest
    result['Smaller'] = smaller
    result['Average'] = average
    if sit:
        if average > 6:
            result['Situation'] = 'Good' 
        else:
            result['Situation'] = 'Bad'
    print('\033[1;35m~\033[m' * 65)
    print(f"\033[1;36m{result}\033[m")
    print('\033[1;35m~\033[m' * 65)
averageF(5.5, 9.5 ,10 ,6.5, True)
print
"""

### Second Resolution ###

"""
def notes(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situation'] = 'Good'
        elif r['Média'] >= 5:
            r['Situation'] = 'Reasonable'
        else:
            r['Situation'] = 'Bad'
    return r

# Main Program
resp = notes(8, 9, 5.5, 2.5, 9.5, sit=True)
print(f'\033[1;35m{resp}\033[m')
print(f"\033[1;36m{notes(9, 10, 5.5, 2.5, 8.5, sit=True)}\033[m")
"""

# Challenge 106

"""
def helpF(method=0):
    while True:
        print('\033[1;33;43m~\033[m' * 60)
        print(f"\033[1;97;43m{'Shown details: interactive help':^60}\033[m")
        print('\033[1;33;43m~\033[m' * 60)
        method = str(input(f"\033[1;31mEnter another Method or Library: \033[m")).strip()
        print('\033[1;36;46m~\033[m' * 60)
        print(f"\033[1;97;46m{f'Acessing manual -> {method} <-':^60}\033[m")
        print('\033[1;36;46m~\033[m' * 60)
        help(method)
        print('\033[1;34;44m_\033[m' * 60)
        while True:
            response = str(input(f"\033[1;31mYou want to continue? [Y/N] \033[m")).strip().upper()[0]
            if response in "YN":
                break
        if response in "N":
            break
helpF()
print("\033[1;36mShutting down\033[m")
"""

### Second Resolution 106 ###

"""
c = (   '\033[m',         # 0 - without colors
        '\033[1;30;41m',  # 1 - red
        '\033[1;30;42m',  # 2 - green
        '\033[1;30;43m',  # 3 - yellow
        '\033[1;30;44m',  # 4 - blue
        '\033[1;30;45m',  # 5 - magenta
        '\033[1;30;46m',  # 6 - cyan
        '\033[7;30m'      # 7 - white
);

def HELP(content):
    TITLE(f"Acess the manual of the comand \'{content}\'",4)
    print(c[7], end='')
    help(content)
    print(c[6], end='')
    
def TITLE(msg, color=0):
    weight = len(msg) + 4
    print(c[color], end='')
    print("~" * weight)
    print(f"   {msg}")
    print("~" * weight)
    print(c[0], end='')    

# Main Program
comand = ''
while True:
    print()
    TITLE('System of help PYHELP', 2)
    print()
    comand = str(input("function or library -> "))
    if comand.upper() == 'END':
        break
    else:
        HELP(comand)
TITLE('See you Soon!', 5)
"""