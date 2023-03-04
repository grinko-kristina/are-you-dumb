# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import *
from tkmacosx import Button
import random


# ---------------------------- COMMANDS ------------------------------- #
def move():
    button_no.place(x=random.randint(10, 350), y=random.randint(100, 260))


def change():
    label.config(text="I Knew It!")
    label.place(x=167.5, y=40)
    button_no.destroy()
    button_yes.destroy()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Are You Dumb?")
YELLOW = "#FFD700"
FONT = "Poppins"
DARK_GREY = "#292b2c"
GREY = "#414341"
window.geometry("520x300")
window.config(bg=YELLOW)


# ---------------------------- LABELS ------------------------------- #
label = Label(text="Are You Dumb?", fg="white", bg=YELLOW, font=(FONT, 45, "bold"))
label.place(x=100, y=40)


# ---------------------------- BUTTONS ------------------------------- #
button_yes = Button(text="Yes, I am.", fg="white", highlightbackground="white", bg=GREY, activebackground=DARK_GREY,
                    font=(FONT, 20, "bold"), highlightthickness=0, command=change)
button_yes.place(x=50, y=170)


button_no = Button(text="No, I am not.", fg="white", highlightbackground="white", bg=GREY, activebackground=DARK_GREY,
                   font=(FONT, 20, "bold"), highlightthickness=0, command=move)
button_no.place(x=320, y=170)


window.mainloop()
