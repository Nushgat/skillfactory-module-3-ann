board = [[" "] * 3 for i in range(3)]

def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(board[i])
        print(f"{i} {row_info}")

show()

def ask():
    x, y = map(int, input("        Ваш код").split())
