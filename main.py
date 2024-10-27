from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window configuration
root = Tk()
root.title("Rock Paper Scissors Game")
root.configure(background="black")  # Dark-themed background
root.geometry("800x600")  # window size

root.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="col")
root.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="row")

# Function to resize images
def resize_image(img_path):
    img = Image.open(img_path)
    return ImageTk.PhotoImage(img.resize((100, 100), Image.LANCZOS))  

# Loaded images
rock_img = resize_image("rock.png")
paper_img = resize_image("paper.png")
scissor_img = resize_image("scissors.jpeg")

rock_img_comp = resize_image("rock.png")
paper_img_comp = resize_image("paper.png")
scissor_img_comp = resize_image("scissors.jpeg")

user_label = Label(root, image=scissor_img, bg="black")
comp_label = Label(root, image=scissor_img_comp, bg="black")
user_label.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")
comp_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

playerScore = Label(root, text=0, font=("Arial", 28, "bold"), bg="black", fg="white")
computerScore = Label(root, text=0, font=("Arial", 28, "bold"), bg="black", fg="white")
playerScore.grid(row=1, column=3, sticky="nsew")
computerScore.grid(row=1, column=1, sticky="nsew")

user_indicator = Label(root, text="USER", font=("Arial", 20, "bold"), bg="black", fg="white")
comp_indicator = Label(root, text="COMPUTER", font=("Arial", 20, "bold"), bg="black", fg="white")
user_indicator.grid(row=0, column=3, sticky="nsew")
comp_indicator.grid(row=0, column=1, sticky="nsew")

msg = Label(root, font=("Arial", 18, "bold"), bg="purple", fg="white", wraplength=600, justify=CENTER)
msg.grid(row=3, column=0, columnspan=5, pady=20, sticky="nsew") 

# Game State 
rounds = 3
user_wins = 0
computer_wins = 0

def updateMessage(text):
    msg.config(text=text)

def updateUserScore():
    score = int(playerScore["text"])
    playerScore.config(text=str(score + 1))

def updateCompScore():
    score = int(computerScore["text"])
    computerScore.config(text=str(score + 1))

def checkWin(player, computer):
    global user_wins, computer_wins

    if player == computer:
        updateMessage("It's a tie!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        updateMessage("You win this round! 🎉")
        updateUserScore()
        user_wins += 1
    else:
        updateMessage("Computer wins this round! 😔")
        updateCompScore()
        computer_wins += 1

    if user_wins == rounds or computer_wins == rounds:
        declare_winner()

def declare_winner():
    if user_wins > computer_wins:
        updateMessage("You won the game! 🏆 Congratulations! 🎉")
    else:
        updateMessage("Computer won the game! 😞 Better luck next time.")

    rock_btn.config(state=DISABLED)
    paper_btn.config(state=DISABLED)
    scissor_btn.config(state=DISABLED)

def reset_game():
    global user_wins, computer_wins
    user_wins = 0
    computer_wins = 0
    playerScore.config(text="0")
    computerScore.config(text="0")
    updateMessage("Make your move!")
    user_label.config(image=scissor_img)
    comp_label.config(image=scissor_img_comp)

    rock_btn.config(state=NORMAL)
    paper_btn.config(state=NORMAL)
    scissor_btn.config(state=NORMAL)

choices = ["rock", "paper", "scissor"]

def updateChoice(user_choice):
    computer_choice = choices[randint(0, 2)]

    if computer_choice == "rock":
        comp_label.config(image=rock_img_comp)
    elif computer_choice == "paper":
        comp_label.config(image=paper_img_comp)
    else:
        comp_label.config(image=scissor_img_comp)

    if user_choice == "rock":
        user_label.config(image=rock_img)
    elif user_choice == "paper":
        user_label.config(image=paper_img)
    else:
        user_label.config(image=scissor_img)

    checkWin(user_choice, computer_choice)

button_style = {"width": 12, "height": 2, "font": ("Arial", 16, "bold")}

rock_btn = Button(root, text="Rock", bg="#FF3E4D", fg="black", **button_style,
                  command=lambda: updateChoice("rock"))
rock_btn.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")

paper_btn = Button(root, text="Paper", bg="#FAD02E", fg="black", **button_style,
                   command=lambda: updateChoice("paper"))
paper_btn.grid(row=2, column=2, padx=15, pady=15, sticky="nsew")

scissor_btn = Button(root, text="Scissor", bg="#0ABDE3", fg="black", **button_style,
                     command=lambda: updateChoice("scissor"))
scissor_btn.grid(row=2, column=3, padx=15, pady=15, sticky="nsew")

new_game_btn = Button(root, text="New Game", bg="#27AE60", fg="black", **button_style,
                      command=reset_game)
new_game_btn.grid(row=4, column=2, padx=15, pady=15, sticky="nsew")

updateMessage("Make your move!")

# Start the Tkinter event loop
root.mainloop()
