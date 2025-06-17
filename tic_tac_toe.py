from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
        
def enter_move(board):
    while True:
        try:
            move=int(input("Enter your move(1-9):"))
            if move < 1 or move > 9:
                print("Move must be between 1 and 9.")
                continue
            row = (move-1) // 3
            col = (move-1) % 3
            
            if board[row][col] in ['X', 'O']:
                print("That field is already occupied.")
                continue
            
            board[row][col]='O'
            break
        except ValueError:
            print("Please, enter a valid number.")
            
def make_list_of_free_fields(board):
    free_fields=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X','O']:
                free_fields.append((row,col))
    return free_fields
    
def victory_for(board,sign): #zafer kontrolü
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or \
           all(board[i][j] == sign for j in range(3)):
               return True
        if (board[0][0] == board[1][1] == board[2][2] == sign) or \
           (board[0][2] == board[1][1] == board[2][0] == sign):
               return True
        return False
        
def draw_move(board):
    free=make_list_of_free_fields(board)
    if free:
        row,col = free[randrange(len(free))]
        board[row][col]='X'
        
def play_game():
    board = [ ['1','2','3'],  ['4', '5', '6'], ['7', '8', '9'] ]
    
    first = input("Who starts? (you/computer): ").strip().lower()
    while first not in ["you", "computer"]:
        first = input("Please type 'you' or 'computer': ").strip().lower()

    if first == "computer":
        board[1][1] = 'X' #The computer starts with the center point (1,1)
        
    current_turn = first
    
    while True:
        display_board(board)
        
        if victory_for(board,'X'):
           print("Computer won!")
           break
        elif victory_for(board,'O'):
           print("You won!")
           break
        elif not make_list_of_free_fields(board):
           print("It is a tie!")
           break
       
        if current_turn == "you":
            enter_move(board)
            current_turn = "computer"
        else:
            draw_move(board)
            current_turn = "you"
       
while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break