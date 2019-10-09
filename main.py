import tkinter as tk
from tkinter import font


# Function that asks user of his move and controls user choice. It checks if chosen square is empty.
# It gives appropriate message
# It returns new board
#
# choice - player choice (row, column) - string
# board - previous board
# player - informs whose turn it is
def get_choice(choice, board, player):
    # converting string into apriopriate format
    choice = choice.split(",")
    choice = [int(i.strip()) for
              i in choice]
    # print(choice)
    # changing board

    if board[choice[0] - 1][choice[1] - 1] == 0:
        board[choice[0] - 1][choice[1] - 1] = player
    else:
        return 0
    return 1


# Draws a board
#
# board - Two dimensional list containing player choices
def draw_a_board(board):
    row = 3
    column = 3
    # choices = []  # list containing coordinates of firs player choices
    # x_choices = []  # list containing coordinates of second player choices
    line = "   "
    for i in range(column):
        line += " "
        line += str(i + 1)
        line += "  "
    print(line)
    print(" ", " ---" * column)
    for i in range(row):
        line = ""
        line += str(i+1)
        line += " "
        for j in range(column):
            line += "|"
            if board[i][j] == 1:
                line += " O "
            elif board[i][j] == 2:
                line += " X "
            else:
                line += "   "
        line += "|"
        print(line)
        print(" ", " ---" * column)
    # print("====" * column)


# function to check the board if there is a winner. If there is, returns who has won
#
# board - 3x3 list
def check_board(board):
    for player in [1, 2]:
        for i in range(3):
            condition3 = board[0][0] == board[1][1] == board[2][2] == player
            if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player  or condition3:
                print(player)
                return player
    return 0


# Checks if there are any moves left (if board is full). If board is full return 0, if there are moves do do, return 1
def is_move(board):
    is_0 = False
    for row in board:
        is_0 = is_0 or 0 in row
    return is_0


# Function to change button into image
def action(button, game):
    # Changing Button into image
    # photo = tk.PhotoImage(file="O.png")
    # button['image'] = photo
    board = game[0]
    player = game[1]
    position = button['text']
    # Changing text in button into player sign
    if not get_choice(position, game[0], game[1]):
        return 0
    if player == 1:
        button['text'] = "O"
    elif player == 2:
        button['text'] = "X"
    # Change player for next move
    # player = change_player(player)
    game[1] = change_player(player)
    draw_a_board(board)
    winner = check_board(board)
    if winner:
        if winner == 1:
            message['text'] = "O has won! "
            print("O has won")
            buttons_disable(game[2])
        elif winner == 2:
            message['text'] = "X has won! "
            print("X has won")
            buttons_disable(game[2])
    else:
        if player == 1:
            message['text'] = "Now O"
        else:
            message['text'] = "Now X"

    #button.destroy()


def change_player(player):
    if player == 1:
        return 2
    if player == 2:
        return 1


def game_ended():
    print("Game ended. No more moves possible")


def buttons_initialise():
    button_font = font.Font(name="Arial", size=40)
    buttons = [[tk.Button(frame, text=str(j + 1) + "," + str(i + 1), font=button_font) for j in range(3)] for i in
               range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].place(anchor="nw", relx=0.05 + i * 0.3, rely=0.05 + j * 0.3, relwidth=0.3, relheight=0.3)
            #  buttons[i][j]['command'] = lambda: change_image(buttons[i][j], 1) doesnt work
    buttons[0][0]['command'] = lambda: action(buttons[0][0], game)
    buttons[0][1]['command'] = lambda: action(buttons[0][1], game)
    buttons[0][2]['command'] = lambda: action(buttons[0][2], game)
    buttons[1][0]['command'] = lambda: action(buttons[1][0], game)
    buttons[1][1]['command'] = lambda: action(buttons[1][1], game)
    buttons[1][2]['command'] = lambda: action(buttons[1][2], game)
    buttons[2][0]['command'] = lambda: action(buttons[2][0], game)
    buttons[2][1]['command'] = lambda: action(buttons[2][1], game)
    buttons[2][2]['command'] = lambda: action(buttons[2][2], game)
    return buttons


def buttons_disable(buttons):
    buttons[0][0]['command'] = game_ended
    buttons[0][1]['command'] = game_ended
    buttons[0][2]['command'] = game_ended
    buttons[1][0]['command'] = game_ended
    buttons[1][1]['command'] = game_ended
    buttons[1][2]['command'] = game_ended
    buttons[2][0]['command'] = game_ended
    buttons[2][1]['command'] = game_ended
    buttons[2][2]['command'] = game_ended


def restart_game(game):
    buttons = game[2]
    for i in range(3):
        for j in range(3):
            buttons[i][j].destroy()
    game[1] = 1
    buttons = buttons_initialise()
    game[2] = buttons
    game[0] = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]


HEIGHT = 700
WIDTH = 800
player = 1

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="red")
frame.place(relx=0.5, rely=0.05, relwidth=0.7, relheight=0.7, anchor="n")

lower_frame = tk.Frame(root, bg="green")
lower_frame.place(relx=0.5, rely=0.80, relheight=0.15, relwidth=0.7, anchor="n")

message_font = font.Font(family="Times", size=30, weight="bold")
message = tk.Label(lower_frame, text="O starts", font=message_font, bg="gray")
message.place(relheight=1, relwidth=0.7)

restart_button = tk.Button(lower_frame, text="Restart",font=message_font, bg="blue", command=lambda:restart_game(game))
restart_button.place(relx=0.7, relwidth=0.3, relheight=1)


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
player = 1
buttons = buttons_initialise()
game = [board, player, buttons]


root.mainloop()

print(" Start")

