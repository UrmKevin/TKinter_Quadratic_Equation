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
            txt_1=str(x1)
            txt_2=str(x2)
            answer.configure(text="x1 "+txt_1+"  x2 "+txt_2)
        elif D<0:
            answer.configure(text="No equations")
        elif D==0:
            x=-b/(2*a)
            answer.configure(text=x)

def graafik():
    graf,D,t

t=0
def veel():
    global t
    if t==0:
        window.geometry(str(window.winfo_width())+"x"+str(window.winfo_height()+200))
        btn_veel.config(text="Decrease window size")
        t=1
    else:
        window.geometry(str(window.winfo_width())+"x"+str(window.winfo_height()-200))
        btn_veel.config(text="Increase window size")
        t=0


window=Tk()
window.title("Solving quadratic quation")
window.geometry('700x400')
f1=Frame(window,width=700,height=400)
f1.pack(side=TOP)
f2=Frame(window,width=700,height=400)
f2.pack(side=TOP)

btn=Button(f1,text="Solve",font="Arial 18",width=10,bg="Grey",fg="Black",relief=RAISED)
btn_g=Button(f1,text="Graphic",font="Arial 18",width=10,bg="Grey",fg="Black",relief=RAISED,command=graafik)
btn_veel=Button(f1,text="Increase window size",font="Arial 18",width=54,bg="Grey",fg="White",relief=RAISED,command=veel)
#--------
btn.place(relx=0.8,rely=0.3,anchor='center')
btn_g.place(relx=0.8,rely=0.15,anchor='center')
btn.bind("<Button-1>",solve)
btn_veel.place(relx=0.5,rely=0.94,anchor='center')

txt1=Entry(f1,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER)# 1
txt2=Entry(f1,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER)# 2
txt3=Entry(f1,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER)# 3
#--------
txt1.place(relx=0.1,rely=0.3,anchor='center')# 1
txt2.place(relx=0.351,rely=0.3,anchor='center')# 2
txt3.place(relx=0.55,rely=0.3,anchor='center')# 3


lbl=Label(f1,text="Решение квадратного уравнения",height=1,width=50,font=("Courier", 18),fg="Black",bg="Grey",relief="solid")
lbl_1=Label(f1,text="x**2+",height=1,width=5,font=("Courier", 18),fg="Green")
lbl_2=Label(f1,text="x+",height=1,width=2,font=("Courier", 18),fg="Green")
lbl_3=Label(f1,text="=0",height=1,width=2,font=("Courier", 18),fg="Green")
answer=Label(f1,text="",height=8,width=54,font=("Courier", 16),bg="Black",fg="White",anchor="w",relief="groove")
#--------
lbl_1.place(relx=0.23,rely=0.3,anchor='center')# x**2+
lbl_2.place(relx=0.45,rely=0.3,anchor='center')# x+
lbl_3.place(relx=0.65,rely=0.3,anchor='center')# =0
lbl.place(relx=0.5,rely=0.0365,anchor='center')
answer.place(relx=0.5,rely=0.65,anchor='center')

var=IntVar()
r1=Radiobutton(f2,text="Whale",variable=var,var=1,font="Courier 18")#kala
r2=Radiobutton(f2,text="Glasses",variable=var,var=1,font="Courier 18")#kala
r3=Radiobutton(f2,text="Froggie",variable=var,var=1,font="Courier 18")#kala


window.mainloop()
