player1 = input("pilih salah satu(batu,gunting,kertas): ")
player2 = input("pilih salah satu(batu,gunting,kertas): ")
if player1 == player2:
    print("pilihan kedua player sama {player1}. It's a tie!")
elif player1 == "batu":
    if player2== "gunting":
        print("Omoo you win!")
    else:
        print("Oops you lose!")
elif player1 == "kertas":
    if player2 == "batu":
        print("Omoo you win!")
    else:
        print("Oops you lose!")
elif player1 == "gunting":
    if player2 == "kertas":
        print("Omoo You win!")
    else:
        print("Oops you lose!.")
