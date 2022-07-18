import lib.archive.validnum as vn

def line(c=0,wei=42):
    if c == 0:
        return '_' * wei
    if c == 1:
        return '\033[1;31m_\033[m' * wei
    if c == 2:
        return '\033[1;32m_\033[m' * wei
    if c == 3:
        return '\033[1;33m_\033[m' * wei
    if c == 4:
        return '\033[1;34m_\033[m' * wei
    if c == 5:
        return '\033[1;35m_\033[m' * wei
    if c == 6:
        return '\033[1;36m_\033[m' * wei
    if c == 7:
        return '\033[1;37m_\033[m' * wei


def colors(txt, c=0):
    if c == 0:
        return f'{txt}'
    if c == 1:
        return f'\033[1;31m{txt}\033[m'
    if c == 2:
        return f'\033[1;32m{txt}\033[m'
    if c == 3:
        return f'\033[1;33m{txt}\033[m'
    if c == 4:
        return f'\033[1;34m{txt}\033[m'
    if c == 5:
        return f'\033[1;35m{txt}\033[m'
    if c == 6:
        return f'\033[1;36m{txt}\033[m'
    if c == 7:
        return f'\033[1;37m{txt}\033[m' 


def header(txt, c=0, cl=0):
    print(line(cl))
    print(colors(txt.center(42), c))
    print(line(cl))
    


def menu(list):
    header("MAIN MENU", 6, 6)
    for i, item in enumerate(list):
        print(f"\033[1;33m{i+1}\033[m - \033[1;34m{item}\033[m")
    opc = vn.readint("Your option: ")
    return opc
