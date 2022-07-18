def readint(msg):
    while True:
        try:
            num = int(input(msg))
        except (KeyboardInterrupt):
            print("\033[1;31mThe user preferred don't type this number\033[m")
            return 0
        except Exception as error:
            print(f"\033[1;31m{error} Enter a valid number integer.\033[m")
        else:
            return num

def readfloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (KeyboardInterrupt):
            print("\033[1;31mThe user preferred don't type this number\033[m")
            return 0
        except Exception as error:
            print(f"\033[1;31m{error} Enter a valid number real.\033[m")
        else:
            return num

