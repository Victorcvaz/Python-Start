def increase(num, percent=0, show=0):
    """
    -> Function to increase percent value in a number
    :param num: The value we've going increase
    :param percent: Percent the increase
    :param show: True for format the values
    :return:
    """
    num *= percent / 100 + 1
    if show == "Y":
        return coin(num)
    else:
        return num
def decrease(num, percent=0, show=0):
    """
    -> Function to decrease percent value in a number
    :param num: The value we've going decrease
    :param percent: Percent the reduce
    :param show: True for format the values
    :return: Number calculated
    """
    num *= 1 - percent / 100
    if show == "Y":
        return coin(num)
    else:
        return num
def double(num, show=0):
    """
    -> Function to double the value of a number
    :param num: The value we've going double
    :param show: True for format the values
    :return: Number calculated
    """
    num *= 2
    if show == "Y":
        return coin(num)
    else:
        return num
def half(num, show=0):
    """
    -> Function to calculate half of a number
    :param num: The value we've going get the half
    :param show: True for format the values
    :return: Number calculated
    """
    num /= 2
    if show == "Y":
        return coin(num)
    else:
        return num

def coin(num, show=0):
    """
    -> Function to format the values in coin mode
    :param num: The value we've going format
    :param show: True for format the values
    :return: Number formated
    """
    if show == "N":
       return num
    num = str(f"\033[1;34mR${num:.2f}\033[m")
    return num.replace(".",",")

def summary(num ,percenti=0 , percentd=0, show=0):
    """
    -> Function to show some math operations with a number
    :param num: The value we've going to use for the summary
    :param percenti: Percent the increase
    :param percentd: Percent the reduce
    :param show: True for format the values
    :return: none
    """
    print(f"\033[1;33m~\033[m" * 30)
    print(f"{'Summary of the value':^30}")
    print(f"\033[1;33m_\033[m" * 30)
    print(f"{'Analysed price: ':<20}{coin(num, show)}")
    print(f"{'Double of price: ':<20}{double(num, show)}")
    print(f"{'Half of price: ':<20}{half(num, show)}")    
    print(f"{f'{percenti}% of increase: ':<20}{increase(num, percenti, show)}")
    print(f"{f'{percentd}% of reduce: ':<20}{decrease(num, percentd, show)}")
    print(f"\033[1;33m_\033[m" * 30)