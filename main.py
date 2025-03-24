def Dud():

    return 'A!'

def inputControl():
    
    user_input = int(input("Введите число: "))
    
    return user_input

def characterChoiceConfirmation():

    answer = input("Вы уверены в выборе данного имени? (Y/N): ")

    return answer.upper() == "Y"

def harder_input_control():
    
    try: 
        value = int(input("Введите число от 1 до 10: "))
        if 1 <= value <= 10:
            return value
        else:
            return None
    except ValueError:
        return None
        
