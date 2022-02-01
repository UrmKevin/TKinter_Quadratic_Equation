from tkinter import *
import matplotlib.pyplot as plt #Y=...
from numpy import * #[a,b]

t=""
D=-1
graf=False
def solve():
    global graf,D,t
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
            answer.configure(text="x1 "+txt_1+"\nx2 "+txt_2)
            graf=True
        elif D<0:
            answer.configure(text="No equations")
        elif D==0:
            x=-b/(2*a)
            answer.configure(text=x)
            graf=True
    return graf,D,t


def whale():
    x1=arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=arange(-15,-9.5, 0.5)
    y9=[1]*len(x9)
    x10=arange(3,4,0.5)
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def Umbrella():
    x1=arange(-12, 12.5, 0.5)
    y1=(-1/18)*x1*x1+12
    x2=arange(-4, 4.5, 0.5)
    y2=(-1/8)*x2*x2+6
    x3=arange(-12, -4.5, 0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=arange(4, 12.5, 0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=arange(-4, -0.3, 0.5)
    y5=2*(x5+3)**2-9
    x6=arange(-4, 0.2, 0.5)
    y6=1.5*(x6+3)**2-10
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()


def graafik():
    global graf,D,t
    graf,D,t=solve()
    if graf==True:
        a_=float(txt1.get())
        b_=float(txt2.get())
        c_=float(txt3.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x1 = arange(x0-10, x0+10, 0.5)#numpy(min max step [min,max])
        y1=a_*x1*x1+b_*x1+c_
        fig = plt.figure()
        plt.plot(x0,y0,x1,y1,'r-d')
        plt.title('Quadratic quation')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Parabola's peak ({x0},{y0})"
    else:
        text=f"Can't build a graphic"
    answer.configure(text=f"D={D}\n{t}\n{text}")

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
f1.place(x=0,y=0)
f2=Frame(window,width=700,height=400)
f2.place(x=0,y=400)

btn=Button(f1,text="Solve",font="Arial 18",width=10,bg="Grey",fg="Black",relief=RAISED,command=solve)
btn_g=Button(f1,text="Graphic",font="Arial 18",width=10,bg="Grey",fg="Black",relief=RAISED,command=graafik)
btn_veel=Button(f1,text="Increase window size",font="Arial 18",width=54,bg="Grey",fg="White",relief=RAISED,command=veel)
#--------
btn.place(relx=0.8,rely=0.3,anchor='center')
btn_g.place(relx=0.8,rely=0.15,anchor='center')
btn_veel.place(relx=0.5,rely=0.94,anchor='center')

txt1=Entry(f1,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER) # 1
txt2=Entry(f1,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER) # 2
txt3=Entry(f1,width=5,font="Arial 20",fg="Black",bg="Grey",justify=CENTER) # 3
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
r1=Radiobutton(f2,text="Whale",variable=var,value=1,font="Courier 18",command=whale)
r2=Radiobutton(f2,text="Glasses",variable=var,value=2,font="Courier 18")
r3=Radiobutton(f2,text="Tree",variable=var,value=3,font="Courier 18",command=Umbrella)
#--------
r1.place(relx=0,rely=0)
r3.place(relx=0.3,rely=0)


window.mainloop()