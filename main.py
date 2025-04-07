#<!-- Deprecated initial debug functions. Touch at your own risk. -->

#def Dud():
#
#    return 'A!'

#def inputControl():
#
#    user_input = int(input("Введите число: "))
#
#    return user_input

# -- Code starts here. ---

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

def get_character_name():

    while True:

        name = input("Введите имя персонажа: ").strip()
        
        if 2 <= len(name) <= 20 and name.isalpha():

            if characterChoiceConfirmation():

                return name
            
        else:
            print("Имя должно содержать от 2 до 20 букв.")

def get_character_age():

    while True:

        try:

            age = int(input("Введите возраст персонажа (10-100): "))

            if 10 <= age <= 100:

                return age
            
            print("Возраст должен быть между 10 и 100.")

        except ValueError:
            print("Пожалуйста, введите число.")

def get_character_class():

    classes = ["Воин", "Маг", "Лучник", "Целитель"]

    print("\nДоступные классы:")

    for i, class_name in enumerate(classes, 1):

        print(f"{i}. {class_name}")
    
    while True:
        try:
            choice = int(input("\nВыберите класс (1-4): "))

            if 1 <= choice <= len(classes):

                return classes[choice - 1]
            
            print("Пожалуйста, выберите существующий класс.")

        except ValueError:
            print("Введите число от 1 до 4.")

def create_character():

    print("=== Создание персонажа ===")

    name = get_character_name()
    age = get_character_age()
    character_class = get_character_class()
    
    return {
        "name": name,
        "age": age,
        "class": character_class
    }

if __name__ == "__main__":

    character = create_character()
    
    print("\nСозданный персонаж:")
    print(f"Имя: {character['name']}")
    print(f"Возраст: {character['age']}")
    print(f"Класс: {character['class']}")

# bob