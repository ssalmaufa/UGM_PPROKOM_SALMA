player1 = input("pilih salah satu(batu,gunting,kertas): ")
player2 = input("pilih salah satu(batu,gunting,kertas): ")
if player1 == player2:
    print("pilihan kedua player sama {player1}. It's a tie!")
elif player1 == "batu":
    if player2== "gunting":
        print("batu win the game!")
    else:
        print("Oops player 1 you lose!")
elif player1 == "kertas":
    if player2 == "batu":
        print("kertas win the game!")
    else:
        print("Oops player 1 you lose!")
elif player1 == "gunting":
    if player2 == "kertas":
        print("gunting win the game!")
    else:
        print("Oops player 1, u lose!.")
