from tkinter import *
import random

root = Tk()
root.title("Flash Cards")
root.geometry("400x175")
root.configure(bg = "black")

startstop = 0
xlist = []

with open("words-eng-ru.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            xlist.append(row)


def startstopshowcards():
    global startstop
    if startstop == 0:
        btn1["text"] = "pause"
        startstop = 1
        while startstop == 1:
            try:
                var = random.choice(xlist)
                l, r = var.split(":")
                lbl1.configure(text = l)
                lbl2.configure(text = r)
                root.after(5000)
                root.update()
            except TclError:
                sys.exit()
    else:
        btn1["text"] = "show"
        startstop = 0

def countwords():
    count = len(xlist)
    lbl4.configure(text = str(count))

lbl1 = Label(root, text = "", fg = "yellow", bg = "black")
lbl2 = Label(root, text = "", fg = "yellow", bg = "black")
lbl3 = Label(root, text = "total words: ", fg = "white", bg = "black")
lbl4 = Label(root, text = "", fg = "white", bg = "black")
btn1 = Button(root, text = "show", bg = "gray", command = startstopshowcards)
lbl1.place(x = 60, y = 30)
lbl2.place(x = 60, y = 60)
lbl3.place(x = 120, y = 120)
lbl4.place(x = 205, y = 120)
btn1.place(x = 160, y = 140)

countwords()

if __name__ == "__main__":
    root.mainloop()
