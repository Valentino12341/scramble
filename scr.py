import random 
from tkinter import*
from tkinter import messagebox
from tkinter import font
win = Tk()
win.geometry("700x600")
win.config(bg="Lightgreen")



correct = [
    "apple", "banana", "cobra", "fly", "dog", "text", "python", "random", "jungle", "wizard", "orange", "planet","school", "friend", "cloud", "window", "travel", "garden", "bridge", "dream", "storm", "castle", "button", "mirror","forest", "rocket", "dragon", "island", "secret", "silver", "giants", "camera", "pirate", "helmet", "tunnel", "puzzle","clocks", "energy", "hunter", "object", "spaces", "danger", "magic", "future", "glider", "goblin", "desert", "ocean","rhythm", "crystal", "potion", "flames", "marvel", "quest", "robot", "cyborg", "dancer", "melody", "singer", "artist","vision", "shapes", "number", "plasma", "galaxy", "vector", "bounce", "clover", "rabbit", "bubble", "gadget", "circle","square", "pillow", "feather", "pencil", "candle", "laptop", "shadow", "spaceship", "gravity", "science", "pyramid","oxygen", "matrix", "cloudy", "bridge", "castle", "window", "planet", "travel", "mirror", "orange", "python", "jungle","banana", "planet", "wizard", "garden", "random", "storm", "dream", "friend", "school"
]

jumbled = [     
    "eplpa", "anbaan", "rocba", "lyf", "ogd", "xtte", "typhon", "omdnar", "ugnlej", "dazwir", "aegorn", "nelpat","cohlos", "nerdif", "ludco", "ndwoiw", "elvrat", "edgnar", "igrdeb", "amrde", "ormts", "tslcae", "tutobn", "rorrim","oerstf", "kctoer", "gonadr", "danlsi", "ceerst", "vresil", "tsiang", "armeca", "atrepi", "temhel", "nelnut", "elupzz","skcolc", "gnyree", "nteruh", "jecobt", "scespa", "rdegan", "cigam", "rueftu", "dirgel", "nlogib", "tsreed", "cnaeo","myhtrh", "tscryal", "tionpo", "sfelma", "mlvear", "etqsu", "obotr", "bgryco", "rcedna", "yodlem", "rgenis", "tsitra","sionvi", "hspase", "rebmun", "slpmaa", "laxgay", "cetrov", "ceubon", "velocr", "tibbar", "blubbe", "tedgag", "lrecic","rauqes", "wollip", "aretfeh", "licpen", "ladcen", "ptolpa", "odswah", "ipchseass", "tivgary", "cenecsi", "darypmi","noyxge", "ratimx", "dculoy", "edbirg", "lceast", "wonidw", "nelpta", "elvart", "rorrim", "agroen", "typhon", "genjul","nanaba", "tnleap", "dazwri", "nedgra", "nordam", "mtsor", "meadr", "rdenfi", "holcos"
]
storecor = ""
storejumb = ""
score = 0
attempt = -1
penatly = 0
first_hint = 0
hintindex = 1

def hint():# HINT BUTTON
    global storecor,storejumb,penatly,attempt,first_hint,hintindex
    print(storecor[hintindex])
    first_hint +=1
    
    hint_label.config(text="the first letter ="+storecor[0:hintindex])
    penatly += 1
    penatly_label.config(text="penalty for hint = "+str(penatly))
    hintindex +=1
    if penatly == 3:
        attempt += 1
        penatly = 0
        sL.config(text=str(score)+"/"+str(attempt))
        penatly_label.config(text=penatly)
        print("test")
    if first_hint == 1:
        messagebox.showinfo("hints","3 hints = 1 try ")

def newword(): #RESET BUTTON
    global correct,jumbled,storecor,storejumb,attempt,hintindex
    hintindex = 1
    ra = random.randint(0,101)
    storecor = correct[ra]
    storejumb = jumbled[ra]
    qL.config(text=storejumb)
    attempt += 1
    sL.config(text=str(score)+"/"+str(attempt))
    hint_label.config(text="")

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
