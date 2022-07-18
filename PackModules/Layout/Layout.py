
from time import sleep

def layout(people):
    option = 0
    while True:
        print("\033[1;35mProcessing\033[m")
        sleep(4)
        print('\033[1;32m_\033[m' * 40)
        print(f"\033[1;32m{'MAIN MENU':^40}\033[m")
        print('\033[1;32m_\033[m' * 40)
        print(f"\033[1;33m1\033[m - \033[1;34mShow registered people\033[m")
        print(f"\033[1;33m2\033[m - \033[1;34mRegister new person\033[m")
        print(f"\033[1;33m3\033[m - \033[1;34mexit of System\033[m")
        print('\033[1;32m_\033[m' * 40)
        while True:
            try:
                option = int(input(f"\033[0;33mYour option: \033[m"))
                if option > 0 and option < 4:
                    break
                print("\033[1;31mWrong option: try again\033[m")
            except Exception as error:
                print(f"{error.__class__} Enter one valid option")
        if option == 1:
            print('\033[1;35m_\033[m' * 40)
            print(f"\033[1;35m{'PEOPLE REGISTERED':^40}\033[m")
            print('\033[1;35m_\033[m' * 40)
            for v in people:
                print(f"{v['Name']:<30}", end='')
                print(f"{v['Years']} years")
                sleep(1)
        if option == 2:
            print('\033[1;35m_\033[m' * 40)
            print(f"\033[1;35m{'Register a new person':^40}\033[m")
            print('\033[1;35m_\033[m' * 40)
            return people
        if option == 3:
            print("\033[1;34mLeaving the system, see you later\033[m")
            return "S"