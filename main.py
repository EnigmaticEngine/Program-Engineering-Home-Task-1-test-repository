def Dud():

    return 'A!'

def inputControl():
    
    alfa = int(input("Введите число: "))

    return alfa

def characterChoiceConfirmation():

    gamma = input('Вы уверены в выборе данного имени? (y/n): ').lower().strip() == 'y'

    return gamma

def harderInputControl():

    beta = str(input("Введите имя персонажа: "))

    return beta

