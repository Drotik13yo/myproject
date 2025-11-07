""""
a =  int(input("What is starting price?"))
b = int(input("How much % is discount?"))
newprice = a * b /100
print(
"""
from unittest import case

print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y?")
print("[3] x wordt verhoogd met y%")
print("[4] x wordt verlaagd met y%")
print("[5] Het getal stijgt van x naar y, hoeveel %?")
print("[6] Het getal daalt van x naar y, hoeveel %?")
choice = input("Welke optie kies je?")
match choice:
    case "1":
        print("optie 2 is gekozen")
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / 100 * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer) )

    case "2":
        print("optie 2 is gekozen")
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (x / y ) * 100
        print("De vraag is: hoeveel % is " + str(x) + " van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " "(" + str(x) + ")" + str(y) + "* 100" + str(( x / y ) * 100 ) " = " + str(answer) )
        

    case "3":
        print("optie 3 is gekozen")
        x = float(input("Wat is begin getal(x)?"))
        y = float(input("Met hoevel % verlaagd?"))
        antwer = x * (1 + y / 100)

    case "4":
        print("optie 4 is gekozen")
        x = float(input("Wat is begin getal(x)?"))
        y = float(input("Met hoevel % verlaagd?"))
        answer = x * (1 - y / 100)

    case "5":
        print("optie 5 is gekozen")
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = ((y - x) / x) * 100

    case "6":
        print("optie 6 is gekozen")
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = ((x - y) / x) * 100

    case _:
        print("je hebt een ongeldige optie gekozen")
