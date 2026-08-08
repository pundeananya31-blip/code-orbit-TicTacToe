import tkinter as tk
from tkinter import messagebox
import random

# ==============================
# TIC-TAC-TOE WITH SIMPLE AI
# CodeOrbit Tech Internship
# ==============================

root = tk.Tk()
root.title("Tic-Tac-Toe | Simple AI")
root.geometry("520x700")
root.resizable(False, False)
root.configure(bg="#EDE9FE")

# ------------------------------
# Game Variables
# ------------------------------
board = [""] * 9
player = "X"
computer = "O"
game_over = False

# ------------------------------
# Winning Combinations
# ------------------------------
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# ------------------------------
# Check Winner
# ------------------------------
def check_winner():
    for a, b, c in winning_combinations:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a], (a, b, c)

    if "" not in board:
        return "Draw", None

    return None, None


# ------------------------------
# Player Move
# ------------------------------
def player_move(index):

    global game_over

    if game_over or board[index] != "":
        return

    board[index] = player

    buttons[index].config(
        text="X",
        fg="#2563EB",
        bg="#DBEAFE",
        activebackground="#BFDBFE"
    )

    winner, combination = check_winner()

    if winner:
        finish_game(winner, combination)
        return

    status_label.config(
        text="🤖 Computer is thinking...",
        fg="#7C3AED"
    )

    root.after(500, computer_move)


# ------------------------------
# Computer Move
# ------------------------------
def computer_move():

    global game_over

    if game_over:
        return

    move = find_best_move()

    if move is not None:

        board[move] = computer

        buttons[move].config(
            text="O",
            fg="#DC2626",
            bg="#FEE2E2",
            activebackground="#FECACA"
        )

    winner, combination = check_winner()

    if winner:
        finish_game(winner, combination)
    else:
        status_label.config(
            text="😊 Your Turn - Choose a Box",
            fg="#111827"
        )


# ------------------------------
# Simple AI
# ------------------------------
def find_best_move():

    # 1. AI tries to win
    for i in range(9):

        if board[i] == "":

            board[i] = computer
            winner, _ = check_winner()
            board[i] = ""

            if winner == computer:
                return i

    # 2. AI blocks player
    for i in range(9):

        if board[i] == "":

            board[i] = player
            winner, _ = check_winner()
            board[i] = ""

            if winner == player:
                return i

    # 3. Center
    if board[4] == "":
        return 4

    # 4. Corners
    corners = [0, 2, 6, 8]
    available_corners = [
        i for i in corners if board[i] == ""
    ]

    if available_corners:
        return random.choice(available_corners)

    # 5. Any available position
    available = [
        i for i in range(9) if board[i] == ""
    ]

    if available:
        return random.choice(available)

    return None


# ------------------------------
# Finish Game
# ------------------------------
def finish_game(winner, combination):

    global game_over

    game_over = True

    # Highlight winning boxes
    if combination:

        for index in combination:

            buttons[index].config(
                bg="#BBF7D0",
                fg="#166534"
            )

    if winner == "X":

        status_label.config(
            text="🎉 YOU WIN!",
            fg="#16A34A"
        )

        messagebox.showinfo(
            "🎉 Congratulations!",
            "You won the game!"
        )

    elif winner == "O":

        status_label.config(
            text="🤖 COMPUTER WINS!",
            fg="#DC2626"
        )

        messagebox.showinfo(
            "Game Over",
            "Computer won this time! 🤖"
        )

    else:

        status_label.config(
            text="🤝 IT'S A DRAW!",
            fg="#CA8A04"
        )

        messagebox.showinfo(
            "Game Over",
            "It's a Draw! 🤝"
        )


# ------------------------------
# New Game
# ------------------------------
def new_game():

    global board, game_over

    board = [""] * 9
    game_over = False

    for button in buttons:

        button.config(
            text="",
            state="normal",
            bg="#FFFFFF",
            fg="#111827"
        )

    status_label.config(
        text="😊 Your Turn - Choose a Box",
        fg="#111827"
    )


# ------------------------------
# Exit
# ------------------------------
def exit_game():

    answer = messagebox.askyesno(
        "Exit Game",
        "Do you really want to exit?"
    )

    if answer:
        root.destroy()


# ==================================================
# GUI DESIGN
# ==================================================

# Header
header = tk.Frame(
    root,
    bg="#6D28D9",
    height=120
)

header.pack(fill="x")

title = tk.Label(
    header,
    text="🎮 TIC-TAC-TOE",
    font=("Arial", 28, "bold"),
    bg="#6D28D9",
    fg="white"
)

title.pack(pady=(20, 2))

subtitle = tk.Label(
    header,
    text="⚡ Play Against Simple AI ⚡",
    font=("Arial", 12, "bold"),
    bg="#6D28D9",
    fg="#E9D5FF"
)

subtitle.pack()


# Player Information
info_frame = tk.Frame(
    root,
    bg="#EDE9FE"
)

info_frame.pack(pady=18)

you_label = tk.Label(
    info_frame,
    text="👤 YOU = X",
    font=("Arial", 13, "bold"),
    bg="#DBEAFE",
    fg="#1D4ED8",
    padx=25,
    pady=10
)

you_label.grid(row=0, column=0, padx=7)

ai_label = tk.Label(
    info_frame,
    text="🤖 AI = O",
    font=("Arial", 13, "bold"),
    bg="#FEE2E2",
    fg="#B91C1C",
    padx=25,
    pady=10
)

ai_label.grid(row=0, column=1, padx=7)


# Status
status_label = tk.Label(
    root,
    text="😊 Your Turn - Choose a Box",
    font=("Arial", 15, "bold"),
    bg="#EDE9FE",
    fg="#111827"
)

status_label.pack(pady=5)


# Game Board
board_container = tk.Frame(
    root,
    bg="#4C1D95",
    padx=7,
    pady=7
)

board_container.pack(pady=18)

buttons = []

for i in range(9):

    button = tk.Button(
        board_container,
        text="",
        font=("Arial", 30, "bold"),
        width=4,
        height=2,
        bg="#FFFFFF",
        fg="#111827",
        activebackground="#F3E8FF",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda index=i: player_move(index)
    )

    row = i // 3
    column = i % 3

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )

    buttons.append(button)


# Control Buttons
control_frame = tk.Frame(
    root,
    bg="#EDE9FE"
)

control_frame.pack(pady=15)


new_button = tk.Button(
    control_frame,
    text="🔄  NEW GAME",
    font=("Arial", 12, "bold"),
    bg="#7C3AED",
    fg="white",
    activebackground="#6D28D9",
    activeforeground="white",
    width=16,
    height=2,
    relief="flat",
    cursor="hand2",
    command=new_game
)

new_button.grid(row=0, column=0, padx=8)


exit_button = tk.Button(
    control_frame,
    text="❌  EXIT",
    font=("Arial", 12, "bold"),
    bg="#EF4444",
    fg="white",
    activebackground="#DC2626",
    activeforeground="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2",
    command=exit_game
)

exit_button.grid(row=0, column=1, padx=8)


# Footer
footer = tk.Label(
    root,
    text="💻 Python • Tkinter • Simple AI",
    font=("Arial", 10, "bold"),
    bg="#EDE9FE",
    fg="#6B7280"
)

footer.pack(pady=15)


# Start Application
root.mainloop()