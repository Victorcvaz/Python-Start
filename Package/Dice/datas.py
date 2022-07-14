def format(msg):
    while True:
        data = str(input(msg)).strip()
        if data.replace('.', '', 1).isdigit() or data.replace(',', '', 1).isdigit():
            return float(data.replace(',', '.'))
        print(f"\033[1;31mError \"{data}\" not valid!  Type a value number!\033[m ")

def validation(msg):
    while True:
        show = str(input(msg)).upper().strip()
        if show == 'Y' or show == "N":
            return show
        print(f"\033[1;31mError \"{show}\" not valid! type only [Y/N]!\033[m")