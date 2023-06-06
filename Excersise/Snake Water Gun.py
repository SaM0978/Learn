import random

def S_W_G(loop: str = ""):
    try:
        if loop == "":
            Input = int(input("Choose Stone-1, Paper-2, Scissor-3\n"))
            Computer = random.choice([1, 2, 3])
            Comp_Point = 0
            Player_Point = 0

            if Input == 1 and Computer == 1:
                print("It's a tie")
                Comp_Point += 1
                Player_Point += 1
                print(f"Computer's Choice: {Computer}")
            elif Input == 2 and Computer == 2:
                print("It's a tie")
                Comp_Point += 1
                Player_Point += 1
                print(f"Computer's Choice: {Computer}")
            elif Input == 3 and Computer == 3:
                print("It's a tie")
                Comp_Point += 1
                Player_Point += 1
                print(f"Computer's Choice: {Computer}")
            elif Input == 2 and Computer == 1:
                Comp_Point += 1
                Player_Point += 0
                print(f"Computer's Choice: {Computer}")
                print("Player Won")
            elif Input == 1 and Computer == 2:
                Comp_Point += 0
                Player_Point += 1
                print(f"Computer's Choice: {Computer}")
                print("Player Won")
            elif Input == 3 and Computer == 2:
                Comp_Point += 0
                Player_Point += 1
                print(f"Computer's Choice: {Computer}")
                print("Player Won")
            elif Input == 2 and Computer == 3:
                Comp_Point += 1
                Player_Point += 0
                print(f"Computer's Choice: {Computer}")
                print("Computer Won")
            elif Input == 3 and Computer == 1:
                Comp_Point += 1
                Player_Point += 0
                print(f"Computer's Choice: {Computer}")
                print("Computer Won")
            elif Input == 1 and Computer == 3:
                Comp_Point += 0
                Player_Point += 1
                print(f"Computer's Choice: {Computer}")
                print("Player Won")
            else:
                Player_Point += 0
                Comp_Point += 0
                print(f"Computer's Choice: {Computer}")

            if Player_Point > Comp_Point:
                print(f"Player Won {Player_Point}")
            elif Player_Point == Comp_Point:
                print("It's a Tie")
            else:
                print(f"Computer Won: {Comp_Point}")

        else:
            Comp_Point = 0
            Player_Point = 0
            for i in range(1, int(loop) + 1):
                print(f"Round {i}")
                Input = int(input("Choose Stone-1, Paper-2, Scissor-3\n"))
                Computer = random.choice([1, 2, 3])

                if Input == Computer:
                    print(f"Computer's Choice: {Computer}")
                    print("It's a Tie")
                elif Input == 2 and Computer == 1:
                    Comp_Point += 1
                    Player_Point += 0
                    print(f"Computer's Choice: {Computer}")
                    print("Player Won")
                elif Input == 1 and Computer == 2:
                    Comp_Point += 0
                    Player_Point += 1
                    print(f"Computer's Choice: {Computer}")
                    print("Player Won")
                elif Input == 3 and Computer == 2:
                    Comp_Point += 0
                    Player_Point += 1
                    print(f"Computer's Choice: {Computer}")
                    print("Player Won")
                elif Input == 2 and Computer == 3:
                    Comp_Point += 1
                    Player_Point += 0
                    print(f"Computer's Choice: {Computer}")
                    print("Computer Won")
                elif Input == 3 and Computer == 1:
                    Comp_Point += 1
                    Player_Point += 0
                    print(f"Computer's Choice: {Computer}")
                    print("Computer Won")
                elif Input == 1 and Computer == 3:
                    Comp_Point += 0
                    Player_Point += 1
                    print(f"Computer's Choice: {Computer}")
                    print("Player Won")
                else:
                    Player_Point += 0
                    Comp_Point += 0
                    print(f"Computer's Choice: {Computer}")

            if Player_Point > Comp_Point:
                print(f"Player Won: {Player_Point} rounds")
            elif Player_Point == Comp_Point:
                print("It's a Tie")
            else:
                print(f"Computer Won: {Comp_Point} rounds")

    except ValueError:
        print("Invalid input. Please enter an integer.")


S_W_G('2')
