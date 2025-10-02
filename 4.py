import random
point = 0
male = 0
tafel = int(input("tafel van:"))
while True:
    b = random.randint(1, 10)
    antwoord = tafel * b

    gok = int(input(f" {tafel} x {b} = "))
    if gok == antwoord:
            print("good") 
            point +=1
            male +=1
    else:
            print("nope, answer is", antwoord)
            male +=1
    if point == 10:
            print("you win")
            break
    if male == 10:
            print ("good jod")
            print("your score:", point)
            break
    