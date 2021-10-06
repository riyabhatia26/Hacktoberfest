from tkinter import *
from tkinter import messagebox

game = {"Started": False, "player": "O"}
player = "X"
button = [[], [], []]
root = Tk()
label_player_info_var = StringVar()


def get_player():
    if game["player"] == "X":
        return "O"
    else:
        return "X"


def is_board_disabled():
    for i in range(0, 3):
        for j in range(0, 3):
            if button[i][j]["state"] != DISABLED:
                return False
    return True


def board_check():
    global player
    for i in range(0, 3):
        cond1 = button[i][0]["text"] == button[i][1]["text"] == button[i][2]["text"] == player
        cond2 = button[0][i]["text"] == button[1][i]["text"] == button[2][i]["text"] == player
        if cond1 or cond2:
            messagebox.showinfo("Congrats!!", "'" + player + "' has won")
            reset_board()

    cond1 = button[0][0]["text"] == button[1][1]["text"] == button[2][2]["text"] == player
    cond2 = button[0][2]["text"] == button[1][1]["text"] == button[2][0]["text"] == player

    if cond1 or cond2:
        messagebox.showinfo("Congrats!!", "'" + player + "' has won")
        reset_board()

    elif is_board_disabled():
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset_board()


def btn_click(row, col):
    global game
    global button
    global player
    global label_player_info_var
    player = get_player()
    button[row][col].config(text=player, state=DISABLED, bg='black', disabledforeground="gray")
    label_player_info_var.set("Player %s" % player)
    game["player"] = player
    board_check()


def start_btn_click():
    global label_player_info_var
    global game
    if game["Started"]:
        pass
    else:
        enable_button()
        label_player_info_var.set("Player X")
        game["Started"] = True


def reset_board():
    for i in range(0, 3):
        for j in range(0, 3):
            button[i][j]["state"] = NORMAL
            button[i][j].config(text="", bg='purple3')


def reset_btn_click():
    global game
    global label_player_info_var
    label_player_info_var.set("!Ready!")
    game["Started"] = False
    for i in range(0, 3):
        for j in range(0, 3):
            button[i][j]["state"] = DISABLED
            button[i][j].config(text="", bg='purple3')


def enable_button():
    for i in range(0, 3):
        for j in range(0, 3):
            button[i][j]["state"] = "normal"


def main():
    global root
    root.title("Tic Tac Toe")
    root.geometry("300x350")
    root.resizable(True, True)
    root.configure(bg='purple3')

    frame_board = Frame(root, padx=5, pady=5, height=300, width=300, background='purple3')
    frame_bar = Frame(root, padx=5, pady=5, height=100, width=300, background='purple3')

    start_btn = Button(frame_bar, text="Start", bg='gray', fg='white', command=lambda: start_btn_click())
    reset_btn = Button(frame_bar, text="Reset", bg='gray', fg='white', command=lambda: reset_btn_click())

    start_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    reset_btn.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

    global game
    global label_player_info_var
    label_player_info_var.set("!Ready!")

    label_player_info = Label(frame_bar, width=20, textvariable=label_player_info_var, relief=RAISED)
    label_player_info.grid(row=0, columnspan=4)
    label_player_info.configure(anchor=CENTER)

    global button
    for i in range(0, 3):
        for j in range(0, 3):
            button[i].append(
                Button(frame_board, text=" ", font='Times 20 bold', bg='black', fg='white', height=2, width=4,
                       background='purple1', command=lambda row=i, col=j: btn_click(row, col)))
            button[i][j]["state"] = "disabled"
            button[i][j].grid(row=i, column=j)

    frame_board.pack()
    frame_bar.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
