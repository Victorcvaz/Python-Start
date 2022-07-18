import lib.archive.arch as arc
import lib.layout.lay as lay
from time import sleep

arq = 'why.txt'

if not arc.arqexist(arq):
    arc.createarchive(arq)

while True:
    response = lay.menu(["Show the registered people", "Add a new register", "Exit"])
    if response == 1:
        arc.readarchive(arq)
    elif response == 2:
        print()
    elif response == 3:
        lay.header("Leaving the system! See you later!", 7, 7)
        break
    else:
        lay.header("Error, type a valid option",1 , 1)
    sleep(2)

