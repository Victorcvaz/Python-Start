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
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace("\n", "")
            print(f"\033[1;32m{data[0]:<25}\033[m\033[1;32m{data[1]:>3} years\033[m")
        print(lay.line(2))


def register(arch, name='unknow', age=0):
    try:
        a = open(arch, 'at')
    except:
        lay.header("Was one error writing the data", 1 , 1)
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            lay.header("Was one error writing the data", 1 , 1)
        else:
            lay.header(f"New register of {name} added successfully!", 2, 2)
            a.close()