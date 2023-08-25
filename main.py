import tkinter
from PIL import Image, ImageTk
import random
import os

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the dice by @dobravaza')

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text="@dobravaza",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")

HeadingLabel.pack()

dice = ['die1.PNG', 'die2.PNG', 'die3.PNG', 
    'die4.PNG', 'die5.PNG', 'die6.PNG']

ImageLabel = tkinter.Label(root)
ImageLabel.pack(expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text="roll the dice", command=rolling_dice)
button.pack()

root.mainloop()
