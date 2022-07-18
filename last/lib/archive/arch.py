import lib.layout.lay as lay

def arqexist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createarchive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        lay.header("Was one error in the archive create",1 , 1)
    else:
        lay.header(f"Archive {name} create successfully", 2, 2)


def readarchive(name):
    try:
        a = open(name, 'rt')
    except:
        lay.header("Error at reading the archive", 1, 1)
    else:
        lay.header("REGISTERED PEOPLE", 5, 5)
        print(a.read())
        print(lay.line(3))