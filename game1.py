from tkinter import *
import random
from time import sleep
# from PIL import *
# from PIL import Image, ImageTk
root = Tk()
root.resizable(0, 0)
c = Canvas(root, width=500, height=500, bg="white")
c.pack()
ball = c.create_oval(460, 100, 500, 140, fill='green')
text=Label(text="0",font="Arial 30",fg="black", bg="white")
text.pack(side=LEFT)
#text.place(x=440,y=5)

t1=Label(text="Game Over",font="Arial 30",fg="Red",bg="white")


# img=Image.open("sm.png")

# img=img.resize((50,50))
# image1 = ImageTk.PhotoImage(img)
# c.create_image(5,5,image=image1)
y1=10
y2=90
schet=0
p=c.create_rectangle(10,y1,20,y2,fill='red')
#c.coords(ball, 140,100,180,140)
def motion1():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] <500:
        root.after(10, motion1)
    else:
        motion()
def motion():
    global p
    global text
    global schet
    global flag
    flag=True
    global t1
    c.move(ball, -1, 0)


    if c.coords(ball)[0] ==0: #or c.coords(p)[2]==c.coords(ball)[0] and c.coords(p)[3]<(c.coords(ball)[1]+c.coords(ball)[3])/2>c.coords(p)[1]:


        print("slit")
        schet=0
        flag=False
        t1.place(x=150,y=210)


    elif c.coords(p)[2]==c.coords(ball)[0] and c.coords(p)[1]<(c.coords(ball)[1]+c.coords(ball)[3])/2<c.coords(p)[3]:
        schet+=1
        print(schet)
        text.config(text=schet)
        x=random.randint(0, 460)
        c.coords(ball, 460, x, 500, x+40)
        root.after(10, motion)

    else:

        root.after(10, motion)

def s(event):
    global y1
    global y2
    global p
    if y2<500:
        y1+=5
        y2+=5
        c.delete(p)
        p = c.create_rectangle(10, y1, 20, y2, fill='red')
        root.after(5)
def w(event):
    global y1
    global y2
    global p
    if y1>0:
        y1 -= 5
        y2 -= 5
        c.delete(p)
        p = c.create_rectangle(10, y1, 20, y2, fill='red')
        root.after(1)
c.bind_all("<KeyPress-w>",w)
c.bind_all("<KeyPress-s>",s)


motion()
root.mainloop()