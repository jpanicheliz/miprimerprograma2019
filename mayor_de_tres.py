
number_to_guess = 2

user_number = int(input("Adivina un numero entre 1 y 10, tienes 5 intentos: "))

if number_to_guess == user_number:
    print("Has ganado")
else:
    user_number = int(input("no lo has adinvinado, intentalo otra vez: "))
    if number_to_guess == user_number:
        print("Has ganado")
    else:
        user_number = int(input("no lo has adinvinado, intentalo otra vez: "))
        if number_to_guess == user_number:
            print("Has ganado")
        else:
            user_number = int(input("no lo has adinvinado, intentalo otra vez: "))
            if number_to_guess == user_number:
                print("Has ganado")
            else:
                user_number = int(input("no lo has adinvinado, intentalo otra vez: "))
                if number_to_guess == user_number:
                    print("Has ganado")
                else:
                    user_number = int(input("has perdido"))

