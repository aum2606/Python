from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
curr_card= {}
to_learn = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global curr_card,flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(bg_img, image=card_front_img)
    flip_timer= window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=curr_card["English"], fill="white")
    canvas.itemconfig(bg_img, image=card_back_img)

def is_known():
    to_learn.remove(curr_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash learn")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
bg_img = canvas.create_image(400,263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unkown_btn = Button(image=cross_img,highlightthickness=0, command=next_card)
unkown_btn.grid(row=1,column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()