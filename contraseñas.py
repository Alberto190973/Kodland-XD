import random

characters = "+*/+/ñ/*!&$:?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def Create_Password(password_length):
    password = ""
    n1 = 0
    for i in range(password_length):
        n1 += 1
        if (n1 % 5) == 0:
            for i in range(1):
                password += "-"
        else:
            password += str(random.choice(characters))
    return password

length1 = 0

while True:
    try:
        length1 = int(input("Introduce tu longitud de tu contraseña: "))
    except ValueError:
        print("ValueError")
    if length1 <= 1:
        print("SyntaxError: numero mas bajo que uno")
    else:
        print(f"Aqui tienes tu contraseña: {Create_Password(length1)}")