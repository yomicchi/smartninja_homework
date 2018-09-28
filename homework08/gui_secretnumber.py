import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text = "Guess the secret number!")
greeting.pack()

secret = random.randint(1, 100)

guess = Tkinter.Entry(window)
guess.pack()


def check_guess():
    if int(guess.get()) == secret:
        result_text = "Richtig geraten :D"
    elif int(guess.get()) > secret:
        result_text = "Leider falsch! Deine Zahl ist zu hoch."
    elif int(guess.get()) < secret:
        result_text = "Leider falsch! Deine Zahl ist zu niedrig."

    tkMessageBox.showinfo("Result", result_text)


submit = Tkinter.Button(window, text="Submit", command=check_guess)
submit.pack()

window.mainloop()
