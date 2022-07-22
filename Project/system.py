from lib.archive import arch as arc, validata as vn
import lib.layout.lay as lay
from time import sleep

arch = 'why.txt'

if not arc.arqexist(arch):
    arc.createarchive(arch)

while True:
    response = lay.menu(["Show the registered people", "Add a new register", "Exit"])
    if response == 1:
        arc.readarchive(arch)
    elif response == 2:
        lay.header("NEW REGISTER", 3, 3)
        name = vn.readstr("Name: ")
        age = vn.readint("Age: ")
        arc.register(arch, name, age)
    elif response == 3:
        lay.header("Leaving the system! See you later!", 7, 7)
        break
    else:
        lay.header("Error, type a valid option",1 , 1)
    sleep(2)

