
import random
import json
import datetime

secret = random.randint(1, 10)

intentos = 0
nombre = str(input("Escriba su nombre: "))
print("Bienvenid@ " + nombre)
with open("score2.txt", "r") as score:
    score_lista = json.loads(score.read())
    print("La lista es " + str(score_lista))
    

while True:

    guess = int(input("Guess the secret number (between 1 and 30): "))
    intentos = intentos + 1
    wrong_guesses = intentos -1


    if guess == secret:

        score_lista.append({"Nombre": nombre, "Numero Secreto": secret, "Numero de intentos": intentos,  "Intentos falldios":  wrong_guesses, "Fecha": str(datetime.datetime.now())})
        with open("score2.txt", "w") as score_file:
            score_file.write(json.dumps(score_lista))

            print("You've guessed it - congratulations! It's number " + str(secret))

            print ("Number of attempts: " + str(intentos))

            break

    elif guess > secret:

        print("Your guess is not correct... try something smaller")

    elif guess < secret:

        print("Your guess is not correct... try something bigger")
