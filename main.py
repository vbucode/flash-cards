from tkinter import *
import random

xlist = []

with open("words-eng-ru.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            xlist.append(row.replace("\n", ""))

class B(Button):
    def __init__(self, parent = None, **config):
        Button.__init__(self, parent, **config)
        self.config(command = self.startstopshowcards)
        self.place(x = 160, y = 140)

    def startstopshowcards(self):
        self.lbl = Label(text = "", fg = "yellow", bg = "black")
        self.lbl.place(x = 90, y = 60)
        while True:
            xvar = random.choice(xlist)
            self.lbl.config(text = xvar)
            self.after(5000)
            self.update()

def main():
    root = Tk()
    B(text = "show")
    root.title("Flash Cards")
    root.geometry("400x175")
    root.configure(bg = "black")
    root.mainloop()

if __name__ == "__main__":
    main()
