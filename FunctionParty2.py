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