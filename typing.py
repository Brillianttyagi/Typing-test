from tkinter import *
import wikipedia
import time
def random_page():
    random = wikipedia.random(1)
    try:
        result = wikipedia.page(random).summary
    except wikipedia.exceptions.DisambiguationError as e:
        result = random_page()
    return result

def final(*args):
    global paragraph
    global text
    speed = ""
    count = 0
    text_entered = e2.get()
    text_entered = text_entered.split(" ")
    e2.delete(0, END)
    for i in range(len(text_entered)):
        if paragraph[i] == text_entered[i]:
            count+=1
    if (count<15):
        speed = "Bad"
    elif (count<30):
        speed = "Average"
    else:
        speed = "Good"
    words_acc = str((count//len(text_entered))*100)
    count = str(count)
    text.set("Words Typed:"+count+"     Accuracy:"+words_acc+"%   Typing speed:"+speed+"   ")


    
def count(label1):
    global counter
    counter = 0
    def display():
        global counter
        if counter<=60:
            screen = str(counter)
            label1['text'] = screen
        label1.after(1000,display)
        counter = counter+1
    display()
    

def updatepara():
    global text2
    paragraph = random_page()
    paragraph = paragraph.split(" ")
    text2.set(paragraph[0:80])

if __name__ == "__main__":
    paragraph = random_page()
    paragraph = paragraph.split(" ")
    root = Tk()
    counter = 0
    text = StringVar()
    text2 = StringVar()
    text2.set(paragraph[0:80])
    root.geometry('800x650')
    f1 = LabelFrame(root,bd = 5,relief = GROOVE)
    l1 = Label(f1,textvariable = text2 ,wraplength = 800,font=("times new roman",15,"bold"),bg = "white")
    f1.pack(expand = TRUE,fill = BOTH)
    l1.pack(expand = TRUE,fill = BOTH)
    f2 = LabelFrame(root,bd = 5,relief = GROOVE)
    e2 = Entry(f2,font=("times new roman",15,"bold"),bg = "white")
    f2.pack(expand = TRUE,fill = BOTH)
    e2.bind("<Return>",final)
    e2.pack(expand = TRUE,fill = BOTH)
    f3 = LabelFrame(root,bd = 5,relief = GROOVE)
    l3 = Label(f3,textvariable = text,font=("times new roman",15,"bold"),bg = "white")
    label1 = Label(f3,text = "Timer",font=("times new roman",15,"bold"),bg = "white")
    text.set("Words Typed:        Accuracy:        Typing speed:        ")
    b1 = Button(f3,text = "Start",font = ("times new roman",20),bg = "Red",command = lambda:count(label1))
    f3.pack(expand = TRUE,fill = BOTH)
    b2 = Button(f3,text = "Change Paragraph",font = ("times new roman",20),bg = "Red",command = updatepara)
    label1.pack()
    l3.pack(expand = TRUE)
    b1.pack()
    b2.pack()
    root.mainloop()

