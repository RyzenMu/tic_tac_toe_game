import random



def board():
    position1 = int(input("Enter a Position1: "))
    computer1 = random.randint(1, 9)



    character = '*'

    character1 = 'O'



    for cell in range(1, 10):

        while computer1 == position1:
            computer1 = random.randint(1, 9)

        if cell == position1:
            print(f'| {character}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == computer1:
            print(f'| {character1}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        else:
            print("|", cell, " ", end='|')

        if cell % 3 == 0:
            print()
    print("Computer Position is :", computer1)



    position2 = int(input("Enter a Position2: "))
    computer2 = random.randint(1, 9)



    for cell in range(1, 10):

        while computer2 == position2 or computer2 == position1 or computer2 == computer1:
            computer2 = random.randint(1, 9)

        if cell == position1:
            print(f'| {character}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == position2:
            print(f'| {character}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == computer1:
            print(f'| {character1}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == computer2:
            print(f'| {character1}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        else:
            print("|", cell, " ", end='|')

        if cell % 3 == 0:
            print()

    print("Computer Position is :", computer2)



    position3 = int(input("Enter a Position3: "))
    computer3 = random.randint(1, 9)


    for cell in range(1, 10):

        while computer3 == position3 or computer3 == computer2 or computer3 == computer1 or computer3 == position2 or computer3 == position1:
            computer3 = random.randint(1, 9)

        if cell == position1:
            print(f'| {character}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == position2:
            print(f'| {character}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == position3:
            print(f'| {character}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == computer1:
            print(f'| {character1}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == computer2:
            print(f'| {character1}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        if cell == computer3:
            print(f'| {character1}  |', end='')
            if cell % 3 == 0:
                print()
            continue
        else:
            print("|", cell, " ", end='|')
        if cell % 3 == 0:
            print()
    print("Computer Position is :", computer3)


    if position1 == 3 and position2 == 6 and position3 == 9:
        print("You win!!!")
    elif position1 == 3 and position2 == 9 and position3 == 6:
        print("You win!!!")
    elif position1 == 6 and position2 == 3 and position3 == 9:
        print("You win!!!")
    elif position1 == 6 and position2 == 9 and position3 == 3:
        print("You win!!!")
    elif position1 == 9 and position2 == 3 and position3 == 6:
        print("You win!!!")
    elif position1 == 9 and position2 == 6 and position3 == 3:
        print("You win!!!")
    elif position1 == 2 and position2 == 5 and position3 == 8:
        print("You win!!!")
    elif position1 == 2 and position2 == 8 and position3 == 5:
        print("You win!!!")
    elif position1 == 5 and position2 == 2 and position3 == 8:
        print("You win!!!")
    elif position1 == 5 and position2 == 8 and position3 == 2:
        print("You win!!!")
    elif position1 == 8 and position2 == 2 and position3 == 5:
        print("You win!!!")
    elif position1 == 8 and position2 == 5 and position3 == 2:
        print("You win!!!")
    elif position1 == 1 and position2 == 4 and position3 == 7:
        print("You win!!!")
    elif position1 == 1 and position2 == 7 and position3 == 4:
        print("You win!!!")
    elif position1 == 4 and position2 == 1 and position3 == 7:
        print("You win!!!")
    elif position1 == 4 and position2 == 7 and position3 == 1:
        print("You win!!!")
    elif position1 == 7 and position2 == 1 and position3 == 4:
        print("You win!!!")
    elif position1 == 7 and position2 == 4 and position3 == 1:
        print("You win!!!")
    elif position1 == 1 and position2 == 5 and position3 == 9:
        print("You win!!!")
    elif position1 == 1 and position2 == 9 and position3 == 5:
        print("You win!!!")
    elif position1 == 5 and position2 == 1 and position3 == 9:
        print("You win!!!")
    elif position1 == 5 and position2 == 9 and position3 == 1:
        print("You win!!!")
    elif position1 == 9 and position2 == 1 and position3 == 5:
        print("You win!!!")
    elif position1 == 9 and position2 == 5 and position3 == 1:
        print("You win!!!")
    elif position1 == 3 and position2 == 5 and position3 == 7:
        print("You win!!!")
    elif position1 == 3 and position2 == 7 and position3 == 5:
        print("You win!!!")
    elif position1 == 5 and position2 == 3 and position3 == 7:
        print("You win!!!")
    elif position1 == 5 and position2 == 7 and position3 == 3:
        print("You win!!!")
    elif position1 == 7 and position2 == 3 and position3 == 5:
        print("You win!!!")
    elif position1 == 7 and position2 == 5 and position3 == 3:
        print("You win!!!")
    elif position1 == 1 and position2 == 2 and position3 == 3:
        print("You win!!!")
    elif position1 == 1 and position2 == 3 and position3 == 2:
        print("You win!!!")
    elif position1 == 2 and position2 == 1 and position3 == 3:
        print("You win!!!")
    elif position1 == 2 and position2 == 3 and position3 == 1:
        print("You win!!!")
    elif position1 == 3 and position2 == 1 and position3 == 2:
        print("You win!!!")
    elif position1 == 3 and position2 == 2 and position3 == 1:
        print("You win!!!")
    elif position1 == 4 and position2 == 5 and position3 == 6:
        print("You win!!!")
    elif position1 == 4 and position2 == 6 and position3 == 5:
        print("You win!!!")
    elif position1 == 5 and position2 == 4 and position3 == 6:
        print("You win!!!")
    elif position1 == 5 and position2 == 6 and position3 == 4:
        print("You win!!!")
    elif position1 == 6 and position2 == 4 and position3 == 5:
        print("You win!!!")
    elif position1 == 6 and position2 == 5 and position3 == 4:
        print("You win!!!")
    elif position1 == 7 and position2 == 8 and position3 == 9:
        print("You win!!!")
    elif position1 == 7 and position2 == 9 and position3 == 8:
        print("You win!!!")
    elif position1 == 8 and position2 == 7 and position3 == 9:
        print("You win!!!")
    elif position1 == 8 and position2 == 9 and position3 == 7:
        print("You win!!!")
    elif position1 == 9 and position2 == 7 and position3 == 8:
        print("You win!!!")
    elif position1 == 9 and position2 == 8 and position3 == 7:
        print("You win!!!")
    else:
        print("You Lose")

    you = "Computer Wins"
    if computer1 == 3 and computer2 == 6 and computer3 == 9:
        print("%s win!!!" % you)
    elif computer1 == 3 and computer2 == 9 and computer3 == 6:
        print(you)
    elif computer1 == 6 and computer2 == 3 and computer3 == 9:
        print(you)
    elif computer1 == 6 and computer2 == 9 and computer3 == 3:
        print(you)
    elif computer1 == 9 and computer2 == 3 and computer3 == 6:
        print(you)
    elif computer1 == 9 and computer2 == 6 and computer3 == 3:
        print(you)
    elif computer1 == 2 and computer2 == 5 and computer3 == 8:
        print(you)
    elif computer1 == 2 and computer2 == 8 and computer3 == 5:
        print(you)
    elif computer1 == 5 and computer2 == 2 and computer3 == 8:
        print(you)
    elif computer1 == 5 and computer2 == 8 and computer3 == 2:
        print(you)
    elif computer1 == 8 and computer2 == 2 and computer3 == 5:
        print(you)
    elif computer1 == 8 and computer2 == 5 and computer3 == 2:
        print(you)
    elif computer1 == 1 and computer2 == 4 and computer3 == 7:
        print(you)
    elif computer1 == 1 and computer2 == 7 and computer3 == 4:
        print(you)
    elif computer1 == 4 and computer2 == 1 and computer3 == 7:
        print(you)
    elif computer1 == 4 and computer2 == 7 and computer3 == 1:
        print(you)
    elif computer1 == 7 and computer2 == 1 and computer3 == 4:
        print(you)
    elif computer1 == 7 and computer2 == 4 and computer3 == 1:
        print(you)
    elif computer1 == 1 and computer2 == 5 and computer3 == 9:
        print(you)
    elif computer1 == 1 and computer2 == 9 and computer3 == 5:
        print(you)
    elif computer1 == 5 and computer2 == 1 and computer3 == 9:
        print(you)
    elif computer1 == 5 and computer2 == 9 and computer3 == 1:
        print(you)
    elif computer1 == 9 and computer2 == 1 and computer3 == 5:
        print(you)
    elif computer1 == 9 and computer2 == 5 and computer3 == 1:
        print(you)
    elif computer1 == 3 and computer2 == 5 and computer3 == 7:
        print(you)
    elif computer1 == 3 and computer2 == 7 and computer3 == 5:
        print(you)
    elif computer1 == 5 and computer2 == 3 and computer3 == 7:
        print(you)
    elif computer1 == 5 and computer2 == 7 and computer3 == 3:
        print(you)
    elif computer1 == 7 and computer2 == 3 and computer3 == 5:
        print(you)
    elif computer1 == 7 and computer2 == 5 and computer3 == 3:
        print(you)
    elif computer1 == 1 and computer2 == 2 and computer3 == 3:
        print(you)
    elif computer1 == 1 and computer2 == 3 and computer3 == 2:
        print(you)
    elif computer1 == 2 and computer2 == 1 and computer3 == 3:
        print(you)
    elif computer1 == 2 and computer2 == 3 and computer3 == 1:
        print(you)
    elif computer1 == 3 and computer2 == 1 and computer3 == 2:
        print(you)
    elif computer1 == 3 and computer2 == 2 and computer3 == 1:
        print(you)
    elif computer1 == 4 and computer2 == 5 and computer3 == 6:
        print(you)
    elif computer1 == 4 and computer2 == 6 and computer3 == 5:
        print(you)
    elif computer1 == 5 and computer2 == 4 and computer3 == 6:
        print(you)
    elif computer1 == 5 and computer2 == 6 and computer3 == 4:
        print(you)
    elif computer1 == 6 and computer2 == 4 and computer3 == 5:
        print(you)
    elif computer1 == 6 and computer2 == 5 and computer3 == 4:
        print(you)
    elif computer1 == 7 and computer2 == 8 and computer3 == 9:
        print(you)
    elif computer1 == 7 and computer2 == 9 and computer3 == 8:
        print(you)
    elif computer1 == 8 and computer2 == 7 and computer3 == 9:
        print(you)
    elif computer1 == 8 and computer2 == 9 and computer3 == 7:
        print(you)
    elif computer1 == 9 and computer2 == 7 and computer3 == 8:
        print(you)
    elif computer1 == 9 and computer2 == 8 and computer3 == 7:
        print(you)



board()

















