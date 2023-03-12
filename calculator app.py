from tkinter import *

root=Tk()

root.geometry("300x275")
expression=" "
screen=StringVar()
calc=Label(root,textvariable=screen,height=2,width=16,font=('Arial',24))
calc.grid(columnspan=5)

def press(num):
    global expression
    expression+=str(num)
    screen.set(expression)

def equalbutton():
    global expression
    total=str(eval(expression))
    screen.set(total)
    expression=""

def clear():
    global expression
    expression=""
    screen.set("")

button0=Button(root,text="0",command=lambda:press(0),width=5,font=('Arial',14))
button0.grid(row=5,column=1)
button1=Button(root,text="1",command=lambda:press(1),width=5,font=('Arial',14))
button1.grid(row=2,column=0)
button2=Button(root,text="2",command=lambda:press(2),width=5,font=('Arial',14))
button2.grid(row=2,column=1)
button3=Button(root,text="3",command=lambda:press(3),width=5,font=('Arial',14))
button3.grid(row=2,column=2)
button4=Button(root,text="4",command=lambda:press(4),width=5,font=('Arial',14))
button4.grid(row=3,column=0)
button5=Button(root,text="5",command=lambda:press(5),width=5,font=('Arial',14))
button5.grid(row=3,column=1)
button6=Button(root,text="6",command=lambda:press(6),width=5,font=('Arial',14))
button6.grid(row=3,column=2)
button7=Button(root,text="7",command=lambda:press(7),width=5,font=('Arial',14))
button7.grid(row=4,column=0)
button8=Button(root,text="8",command=lambda:press(8),width=5,font=('Arial',14))
button8.grid(row=4,column=1)
button9=Button(root,text="9",command=lambda:press(9),width=5,font=('Arial',14))
button9.grid(row=4,column=2)
buttonpl=Button(root,text="+",command=lambda:press("+"),width=5,font=('Arial',14))
buttonpl.grid(row=2,column=3)
buttonmi=Button(root,text="-",command=lambda:press("-"),width=5,font=('Arial',14))
buttonmi.grid(row=3,column=3)
buttonmu=Button(root,text="*",command=lambda:press("*"),width=5,font=('Arial',14))
buttonmu.grid(row=4,column=3)
buttondi=Button(root,text="/",command=lambda:press("/"),width=5,font=('Arial',14))
buttondi.grid(row=5,column=3)
buttondeq=Button(root,text="=",command=equalbutton,width=5,font=('Arial',14))
buttondeq.grid(row=5,column=2)
buttonc=Button(root,text="c",command=clear,width=5,font=('Arial',14))
buttonc.grid(row=5,column=0)


root.mainloop()