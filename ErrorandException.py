# Sintax basic Except
"""
try:
    a = int(input("Number: "))
    b = int(input("Number: "))
    c = a / b
except Exception as erro:
    print(f"The problem found was {erro.__class__}")
else:
    print(f"The result is: {c:.1f}")
finally:
    print("Come back again! ThankYou!")
"""

# Basic 2

"""
try:
    a = int(input("Number: "))
    b = int(input("Number: "))
    c = a / b
except Exception as erro:
    print(f"This error was {erro.__cause__}")
else:
    print(f"The result is: {c:.1f}")
finally:
    print("Come back again! ThankYou!")
"""
"""
except (ValueError, TypeError):
    print("We had one problem with the types of data that you typed")
except ZeroDivisionError:
    print("Don't is possible to divide a number by zero!")
except KeyboardInterrupt:
    print("The user preferred don't to inform the data")
"""

# Challenge 113 Basic Try and Except

"""
from Package.Numbers import Exceptions


msg = Exceptions.readint("Enter a integer number: ")
msg2 = Exceptions.readfloat("Enter a real number: ")
print(f"\033[1;34mThe value integer typed was {msg} and the real was {msg2}\033[m")
"""

# Challenge 114 testing if website is online in current time

"""
import urllib
import urllib.request

try:
    site=urllib.request.urlopen("http://pudim.com.br/")
except urllib.request.URLError:
    print("\033[1;31mPudim is offline now\033[m")
else:
    print("\033[1;32mPudim is online now\033[m")
"""

# Challenge 115

from PackModules.Layout import Layout
from PackModules.Numbers import NumbersExceptions
from PackModules.Strings import StrExceptions


def init(people=[]):
    person = {}
    name = years = 0
    option = ""
    while option != "Y":
        print('\033[1;33m~\033[m' * 40)
        name = StrExceptions.readstr("whats your name: ")
        years = NumbersExceptions.readint("how many years you've: ")
        print('\033[1;33m~\033[m' * 40)
        person['Name'] = name
        person['Years'] = years
        people.append(person.copy())
        person.clear()
        option = str(input("\033[1;37mEnter [Y] to stop: \033m")).upper()
    people = Layout.layout(people)
    if people == "S":
        return
    init(people)
init()


