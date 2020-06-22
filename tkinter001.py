#Tic Tac Toe game 
import tkinter as tk

player = "x"
stopGame = False

bgColor = "gray"
fgColor = "white"
winColor = "black"


def RunProgram():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.resizable(0, 0)

    def activate(x, y):
        global player
        if player == "x" and states[x][y] == 0 and stopGame is False:
            box[x][y].config(text="x", fg="white", bg="#B80028")
            states[x][y] = "x"
            player = "o"
        elif player == "o" and states[x][y] == 0 and stopGame is False:
            box[x][y].config(text="o", fg="white", bg="#0a44a1")
            states[x][y] = "o"
            player = "x"
        checkForWinner()

    def checkForWinner():
        global stopGame
        stopGame = False
        for i in range(3):
            if states[i][0] == states[i][1] == states[i][2] != 0:
                box[i][0].config(bg=winColor)
                box[i][1].config(bg=winColor)
                box[i][2].config(bg=winColor)
                stopGame = True
            elif states[0][i] == states[1][i] == states[2][i] != 0:
                box[0][i].config(bg=winColor)
                box[1][i].config(bg=winColor)
                box[2][i].config(bg=winColor)
                stopGame = True
            elif states[0][0] == states[1][1] == states[2][2] != 0:
                box[0][0].config(bg=winColor)
                box[1][1].config(bg=winColor)
                box[2][2].config(bg=winColor)
                stopGame = True
            elif states[2][0] == states[1][1] == states[0][2] != 0:
                box[2][0].config(bg=winColor)
                box[1][1].config(bg=winColor)
                box[0][2].config(bg=winColor)
                stopGame = True

    def restart():
        root.destroy()
        RunProgram()

    box = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    frames = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    states = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # Buttons
    for i in range(3):
        for j in range(3):
            frames[i][j] = tk.Label(root, bg="light gray", bd=3)
            frames[i][j].grid(row=i, column=j)

            box[i][j] = tk.Button(frames[i][j], font=("Arial", 65), width=3,
                                  bg=fgColor, border=0, command=lambda x=i, y=j: activate(x, y))
            box[i][j].pack()

    # Restart Button
    button_restart = tk.Button(root, text="   RESTART   ", font=(
        "Arial", 15, "bold"), border=0, fg="Black", command=restart, activebackground="gray", activeforeground="white")
    button_restart.grid(row=5, column=1, ipady=2)

    # O and X Label
    label1 = tk.Label(root, text="O", fg="#0a44a1",
                      border=3, font=("Arial", 23, "bold"))
    label1.grid(row=5, column=0)

    label2 = tk.Label(root, text="X", fg="#B80028",
                      border=3, font=("Arial", 23, "bold"))
    label2.grid(row=5, column=2)

    root.mainloop()


RunProgram()


