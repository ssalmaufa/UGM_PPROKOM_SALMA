player1=str(input("batu,kertas,gunting:"))
player2=str(input("batu,kertas,gunting:"))

if("player 1 gunting==player 2 batu"):
    print('batu menang')
elif("player 1 gunting==player 2 kertas"):
    print('gunting menang')
elif('player 1 gunting==player 2 gunting'):
    print('seri')
elif('player 1 batu==player 2 kertas'):
    print('kertas menang')
elif('player 1 batu==player2 gunting'):
    print('batu menang')
elif('player 1 batu==player 2 batu'):
    print('seri')
elif('player 1 kertas==player 2 kertas'):
    print('seri')
elif("player1 kertas==player 2 batu"):
    print('kertas menang')
elif('player 1 kertas==player2 gunting'):
    print('gunting menang')
