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
from datetime import datetime

def vote(year):
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