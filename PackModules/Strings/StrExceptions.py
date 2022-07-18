def readstr(msg, name=""):
    while True:
        try:
            while name == "" or name.isnumeric():
                name = str(input(msg)).title().strip()
                if name == "" or name.isnumeric():
                    print(f"\033[1;31mThis is not valid, enter only chacaters\033[m")
        except Exception as error:
            print(f"\033[1;31m{error} Enter a valid character.\033[m")
        else:
            return name