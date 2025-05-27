import random 
from tkinter import*
from tkinter import messagebox
from tkinter import font
win = Tk()
win.geometry("700x600")
win.config(bg="Lightgreen")



correct = ["apple","banana","cobra","fly","dog","text"]
jumbled = ["eplpa","anbaan","rocba","lyf","ogd","xtte"]
storecor = ""
storejumb = ""
score = 0
attempt = -1
penatly = 0
first_hint = 0


def hint():# HINT BUTTON
    global storecor,storejumb,penatly,attempt,first_hint
    print(storecor[0])
    first_hint +=1
    hint_label.config(text="the first letter ="+storecor[0])
    penatly += 1
    penatly_label.config(text="penalty for hint = "+str(penatly))
    if penatly == 3:
        attempt += 1
        penatly = 0
        sL.config(text=str(score)+"/"+str(attempt))
        penatly_label.config(text=penatly)
        print("test")
    if first_hint == 1:
        messagebox.showinfo("hints","3 hints = 1 try ")



def newword(): #RESET BUTTON
    global correct,jumbled,storecor,storejumb,attempt
    ra = random.randint(0,5)
    storecor = correct[ra]
    storejumb = jumbled[ra]
    qL.config(text=storejumb)
    attempt += 1
    sL.config(text=str(score)+"/"+str(attempt))

def check(): #CHECK BUTTON
    global correct,jumbled,storecor,storejumb,score,attempt
    th = e1.get()
    #attempt +=1
    if storecor == th:
        print("yea")
        messagebox.showinfo("yea","Thats correct")
        score += 1
        newword()
        e1.delete(0,END)

    sL.config(text=str(score)+"/"+str(attempt))





hL = Label(win,text="What word is this?",font=("Arial",18),bg="Lightgreen")
hL.pack()

qL = Label(win,text="",font=("bodoni MT",24),bg="Lightgreen")
qL.pack(pady=30)

e1 = Entry(win,width=20,font=("Arial",20))
e1.pack()

cB = Button(win,text="Check answer",width=20,height=3,font=("Arial",15),command=check)
cB.pack(pady=20)

rB = Button(win,text="Reset",font=("Arial",16),width=20,height=3,command=newword)
rB.pack()



hint_button = Button(win,text="HINT",font=("Arial",17),width=20,height=3,command=hint)
hint_button.pack(pady=20)

sL = Label(win,text="0/0",font=("bodoni MT",24),bg="Lightgreen")
sL.pack(side=LEFT,padx=20)

hint_label = Label(win,text="",font=("bodoni MT",24),bg="Lightgreen")
hint_label.pack(side=RIGHT,padx=20)
newword()

penatly_label  = Label(win,text="0",font=("bodoni MT",18),bg="Lightgreen")
penatly_label.place(x=480,y=10)




win.mainloop()
