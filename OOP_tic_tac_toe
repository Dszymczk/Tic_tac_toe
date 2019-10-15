import tkinter as tk
from tkinter import font



class Square(tk.Button):
    # initializer
    def change_state(self, player):
        if player == 1:
            self['image'] = photo_O
            self['text'] = "O"
        elif player == 2:
            self['image'] = photo_X
            self['text'] = "X"

    def __init__(self, the_window, xindex, yindex):
        tk.Button.__init__(self, the_window)
        self.i = xindex
        self.j = yindex
        self.state = 0

        self.place(relx=0.05+(xindex-1)*0.3, rely=0.05+(yindex-1)*0.3, relwidth=0.3, relheight=0.3, anchor="nw")

        self['command'] = lambda: self.change_state(1)

    def disable(self):
        self['command'] = lambda: print("Nothing to do")


class Game(Square):
    # initializer
    def __init__(self, parent_window):
        self.frame = tk.Frame(parent_window, bg="red")
        self.frame.place(relx=0.5, rely=0.05, relwidth=0.7, relheight=0.7, anchor="n")

        self.player = 1
        self.board_state = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
        self.but11 = Square(self.frame, 1, 1)
        self.but12 = Square(self.frame, 1, 2)
        self.but13 = Square(self.frame, 1, 3)
        self.but21 = Square(self.frame, 2, 1)
        self.but22 = Square(self.frame, 2, 2)
        self.but23 = Square(self.frame, 2, 3)
        self.but31 = Square(self.frame, 3, 1)
        self.but32 = Square(self.frame, 3, 2)
        self.but33 = Square(self.frame, 3, 3)

        self.activate_buttons()

        self.lower_frame = tk.Frame(parent_window, bg="green")
        self.lower_frame.place(relx=0.5, rely=0.80, relheight=0.15, relwidth=0.7, anchor="n")

        message_font = font.Font(family="Times", size=30, weight="bold")
        self.message = tk.Label(self.lower_frame, text="O starts", font=message_font, bg="gray")
        self.message.place(relheight=1, relwidth=0.7)

        self.restart_button = tk.Button(self.lower_frame, text="Restart", font=message_font, bg="blue",
                                   command=lambda: self.game_restart())
        self.restart_button.place(relx=0.7, relwidth=0.3, relheight=1)

    def change_player(self):
        # print("change player")
        # self.player = 1
        # print(self.player)
        if self.player == 1:
            self.player = 2
            self.message['text'] = "Now X"
        elif self.player == 2:
            self.player = 1
            self.message['text'] = "Now O"

    def action(self, but):
        but.change_state(self.player)
        self.board_state[but.j-1][but.i-1] = self.player
        # print(self.board_state)
        winner = self.check_board()
        if winner == 1:
            print("O has won")
            self.message['text'] = "O has won!"
            self.disable_buttons()
        elif winner == 2:
            print("O has won")
            self.message['text'] = "X has won!"
            self.disable_buttons()
        elif winner == 3:
            print("Draw")
            self.message['text'] = "Draw!"
            self.disable_buttons()
        else:
            self.change_player()

    def check_board(self):
        print("check_board")
        board = self.board_state
        for i in range(3):
            condition3 = board[0][0] == board[1][1] == board[2][2] == self.player
            condition4 = board[2][0] == board[1][1] == board[0][2] == self.player
            if board[i][0] == board[i][1] == board[i][2] == self.player or board[0][i] == board[1][i] == board[2][i] == self.player  or condition3 or condition4:
                print(self.player)
                return self.player
            elif not self.is_move():
                return 3
        return 0

    def is_move(self):
        is_0 = False
        for row in self.board_state:
            is_0 = is_0 or 0 in row
        return is_0

    def disable_buttons(self):
        self.but11.disable()
        self.but12.disable()
        self.but13.disable()
        self.but21.disable()
        self.but22.disable()
        self.but23.disable()
        self.but31.disable()
        self.but32.disable()
        self.but33.disable()

    def activate_buttons(self):
        self.but11['command'] = lambda: self.action(self.but11)
        self.but12['command'] = lambda: self.action(self.but12)
        self.but13['command'] = lambda: self.action(self.but13)
        self.but21['command'] = lambda: self.action(self.but21)
        self.but22['command'] = lambda: self.action(self.but22)
        self.but23['command'] = lambda: self.action(self.but23)
        self.but31['command'] = lambda: self.action(self.but31)
        self.but32['command'] = lambda: self.action(self.but32)
        self.but33['command'] = lambda: self.action(self.but33)

        self.but11['text'] = ""
        self.but12['text'] = ""
        self.but13['text'] = ""
        self.but21['text'] = ""
        self.but22['text'] = ""
        self.but23['text'] = ""
        self.but31['text'] = ""
        self.but32['text'] = ""
        self.but33['text'] = ""

    def game_restart(self):
        self.activate_buttons()
        self.player = 1
        self.message['text'] = "O starts"
        self.board_state = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]


if __name__ == "__main__":


    HEIGHT = 700
    WIDTH = 800

    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    photo_O = tk.PhotoImage(file="O_m.png")
    photo_X = tk.PhotoImage(file='X_m.png')

    my_game = Game(root)

    root.mainloop()
