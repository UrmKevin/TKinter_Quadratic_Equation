from tkinter import *
from module1 import *

def solve(event):
    txt1.configure(bg="Grey")
    txt2.configure(bg="Grey")
    txt3.configure(bg="Grey")
    a=txt1.get()
    b=txt2.get()
    c=txt3.get()
    if (a.isdigit()==False and a.isalpha()==False) or a=="" or a.isalpha():
        txt1.configure(bg="pink")
    if (b.isdigit()==False and b.isalpha()==False) or b=="" or b.isalpha():
        txt2.configure(bg="pink")
    if (c.isdigit()==False and c.isalpha()==False) or c=="" or c.isalpha():
        txt3.configure(bg="pink")
    if a.isdigit() and b.isdigit() and c.isdigit():
        a=int(a)
        b=int(b)
        c=int(c)
        D=b**2-4*2*c
        answer.configure(text=D)
        if D>0:
            x1=(-b+D**0.5)/(2*a)
            x2=(-b-D**0.5)/(2*a)
            answer.configure(text=x1)
            answer.configure(text=x2)
        elif D<0:
            answer.configure(text="No equations")
        elif D==0:
            x=-b/(2*a)
            answer.configure(text=x)

window=Tk()
window.title("Solving quadratic quation")
window.geometry('700x400')

btn=Button(window,text="Solve",font="Arial 18",width=10,bg="Grey",fg="White",relief=RAISED)
#--------
btn.place(relx=0.8,rely=0.3,anchor='center')
btn.bind("<Button-1>",solve)

txt1=Entry(window,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER)# 1
txt2=Entry(window,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER)# 2
txt3=Entry(window,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER)# 3
#--------
txt1.place(relx=0.1,rely=0.3,anchor='center')# 1
txt2.place(relx=0.351,rely=0.3,anchor='center')# 2
txt3.place(relx=0.55,rely=0.3,anchor='center')# 3


lbl=Label(window,text="Решение квадратного уравнения",height=1,width=50,font=("Courier", 18),fg="Black",bg="Grey",relief="solid")
lbl_1=Label(window,text="x**2+",height=1,width=5,font=("Courier", 18),fg="Green")
lbl_2=Label(window,text="x+",height=1,width=2,font=("Courier", 18),fg="Green")
lbl_3=Label(window,text="=0",height=1,width=2,font=("Courier", 18),fg="Green")
answer=Label(window,text="",height=9,width=54,font=("Courier", 16),bg="Black",fg="White",anchor="w",relief="groove")
#--------
lbl_1.place(relx=0.23,rely=0.3,anchor='center')# x**2+
lbl_2.place(relx=0.45,rely=0.3,anchor='center')# x+
lbl_3.place(relx=0.65,rely=0.3,anchor='center')# =0
lbl.pack()
answer.place(relx=0.5,rely=0.75,anchor='center')


window.mainloop()
