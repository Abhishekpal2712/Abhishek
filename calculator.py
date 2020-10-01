from tkinter import*
import math
root=Tk()
root.title('Calculator')
#root.iconbitmap('')
root.geometry("300x350")
root.resizable(0,0)

val=''
def btn1clicked():
    global val
    val=val+str(1)
    data.set(val)
def btn2clicked():
    global val
    val=val+str(2)
    data.set(val)
def btn3clicked():
    global val
    val=val+str(3)
    data.set(val)
def btn4clicked():
    global val
    val=val+str(4)
    data.set(val)
def btn5clicked():
    global val
    val=val+str(5)
    data.set(val)
def btn6clicked():
    global val
    val=val+str(6)
    data.set(val)
def btn7clicked():
    global val
    val=val+str(7)
    data.set(val)
def btn8clicked():
    global val
    val=val+str(8)
    data.set(val)
def btn9clicked():
    global val
    val=val+str(9)
    data.set(val)
def btn0clicked():
    global val
    val=val+str(0)
    data.set(val)
def btndclicked():
    global val
    val=val+'.'
    data.set(val)
def btnplusclicked():
    global val
    val=val+'+'
    data.set(val)
def btnminusclicked():
    global val
    val=val+'-'
    data.set(val)
def btnmul():
    global val
    val=val+'*'
    data.set(val)
def btndiv():
    global val
    val=val+'/'
    data.set(val)
def btnmoddiv():
    global val
    val=val+'%'
    data.set(val)

def result():
    global val
    result=eval(val)
    val=str(result)
    print(result)
    data.set(result)

def btnrefre():
    global val
    val=''
    data.set(val)
def sqrtx():
    global val
    result=eval(val)
    sqrtres=round(math.sqrt(result),2)
    val=str(sqrtres)
    data.set(sqrtres)
def power():
    global val
    result=eval(val)
    sres=result**2
    val=str(sres)
    data.set(sres)



# ----------------- Label ---------------------------------------
data=StringVar()
label=Label(root,text='result',anchor=SE,font=('Verdana',22),relief=SUNKEN,textvar=data,background='white')
label.pack(expand=True,fill=BOTH)
# ------------------Frames---------------------------------------
btnRowOne=Frame(root,bg='green')
btnRowOne.pack(expand=True,fill=BOTH)

btnRowTwo=Frame(root,bg='red')
btnRowTwo.pack(expand=True,fill=BOTH)

btnRowThree=Frame(root,bg='yellow')
btnRowThree.pack(expand=True,fill=BOTH)

btnRowFour=Frame(root)
btnRowFour.pack(expand=True,fill=BOTH)

btnRowFive=Frame(root)
btnRowFive.pack(expand=True,fill=BOTH)


# ----------------- Buttons -------------------------------------

btn1 = Button(btnRowOne,text='1',font=('ariel',20),relief=GROOVE,border=0,command=btn1clicked)
btn1.pack(side=LEFT,expand=True,fill=BOTH)
btn2 = Button(btnRowOne,text='2',font=('ariel',20),relief=GROOVE,border=0,command=btn2clicked)
btn2.pack(side=LEFT,expand=True,fill=BOTH)
btn3 = Button(btnRowOne,text='3',font=('ariel',20),relief=GROOVE,border=0,command=btn3clicked)
btn3.pack(side=LEFT,expand=True,fill=BOTH)
btn4 = Button(btnRowOne,text='4',font=('ariel',20),relief=GROOVE,border=0,command=btn4clicked)
btn4.pack(side=LEFT,expand=True,fill=BOTH)

btn5 = Button(btnRowTwo,text='5',font=('ariel',20),relief=GROOVE,border=0,command=btn5clicked)
btn5.pack(side=LEFT,expand=True,fill=BOTH)
btn6 = Button(btnRowTwo,text='6',font=('ariel',20),relief=GROOVE,border=0,command=btn6clicked)
btn6.pack(side=LEFT,expand=True,fill=BOTH)
btn7 = Button(btnRowTwo,text='7',font=('ariel',20),relief=GROOVE,border=0,command=btn7clicked)
btn7.pack(side=LEFT,expand=True,fill=BOTH)
btn8 = Button(btnRowTwo,text='8',font=('ariel',20),relief=GROOVE,border=0,command=btn8clicked)
btn8.pack(side=LEFT,expand=True,fill=BOTH)

btn9 = Button(btnRowThree,text='9',font=('ariel',20),relief=GROOVE,border=0,command=btn9clicked)
btn9.pack(side=LEFT,expand=True,fill=BOTH)
btn10 = Button(btnRowThree,text='0',font=('ariel',20),relief=GROOVE,border=0,command=btn0clicked)
btn10.pack(side=LEFT,expand=True,fill=BOTH)
btn11 = Button(btnRowThree,text='+',font=('ariel',20),relief=GROOVE,border=0,command=btnplusclicked)
btn11.pack(side=LEFT,expand=True,fill=BOTH)
btn12 = Button(btnRowThree,text='-',font=('ariel',20),relief=GROOVE,border=0,command=btnminusclicked)
btn12.pack(side=LEFT,expand=True,fill=BOTH)

btn13 = Button(btnRowFour,text='*',font=('ariel',20),relief=GROOVE,border=0,command=btnmul)
btn13.pack(side=LEFT,expand=True,fill=BOTH)
btn14 = Button(btnRowFour,text='/',font=('ariel',20),relief=GROOVE,border=0,command=btndiv)
btn14.pack(side=LEFT,expand=True,fill=BOTH)
btn15 = Button(btnRowFour,text='.',font=('ariel',20),relief=GROOVE,border=0,command=btndclicked)
btn15.pack(side=LEFT,expand=True,fill=BOTH)
btn16 = Button(btnRowFour,text='%',font=('ariel',20),relief=GROOVE,border=0,command=btnmoddiv)
btn16.pack(side=LEFT,expand=True,fill=BOTH)

btn17 = Button(btnRowFive,text='sqrt',font=('ariel',20),relief=GROOVE,border=0,command=sqrtx)
btn17.pack(side=LEFT,expand=True,fill=BOTH)
btn18 = Button(btnRowFive,text='X^2',font=('ariel',20),relief=GROOVE,border=0,command=power)
btn18.pack(side=LEFT,expand=True,fill=BOTH)
btn19 = Button(btnRowFive,text='C',font=('ariel',20),relief=GROOVE,border=0,command=btnrefre)
btn19.pack(side=LEFT,expand=True,fill=BOTH)
btn20 = Button(btnRowFive,text='=',font=('ariel',20),relief=GROOVE,border=0,command=result)
btn20.pack(side=LEFT,expand=True,fill=BOTH)
root.mainloop()