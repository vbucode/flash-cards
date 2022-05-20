import tkinter
import random

root = tkinter.Tk()
root.title("Flash Cards")
root.geometry("500x175")
root.configure(bg = "black")
forcount = {}
count = 0
startstopflag = 0

with open("words-eng-ru.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            eng, rus, *res = row.split(":")
            forcount[eng] = rus

def showcards():
    global startstopflag
    while startstopflag == 1:
        engvar, ruvar = random.choice(list(forcount.items()))
        lbl1.configure(text = engvar)
        lbl2.configure(text = ruvar)
        root.after(5000)
        root.update()

def startstopshowcards():
    global startstopflag
    if startstopflag == 0:
        btn1["text"] = "pause"
        startstopflag = 1
        showcards()
    else:
        btn1["text"] = "show"
        startstopflag = 0

def countwords():
    global count
    count = len(forcount.items())
    lbl4.configure(text = count)
    ent_eng.delete(0, "end")
    ent_ru.delete(0, "end")

lbl1 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl2 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl3 = tkinter.Label(root, text = "total words: ", fg = "white", bg = "black")
lbl4 = tkinter.Label(root, text = "", fg = "white", bg = "black")
btn1 = tkinter.Button(root, text = "show", bg = "gray", command = startstopshowcards)
lbl1.place(x = 180, y = 30)
lbl2.place(x = 180, y = 60)
lbl3.place(x = 190, y = 120)
lbl4.place(x = 270, y = 120)
btn1.place(x = 225, y = 140)
countwords()
if __name__ == "__main__":
    root.mainloop()
