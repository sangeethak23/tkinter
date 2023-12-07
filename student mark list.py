from tkinter import *  
 
root = Tk()
root.geometry("350x700")
root.title("Student Mark List")


def total():
    a=t1.get()
    b=t2.get()
    c=t3.get()
    d=a+b+c
    t4.set(d)
    return

def average():
    a=t1.get()
    b=t2.get()
    c=t3.get()
    d=a+b+c
    e=d/3
    t4.set(e)
    return

def grade2():
    a=t1.get()
    b=t2.get()
    c=t3.get()
    if ((a+b+c)/3) >80:
        t4.set("Grade1")

    elif ((a+b+c)/3) >60:
        t4.set("Grade2")
    else:
        t4.set("Grade3")
    return

def result1():
    a=t1.get()
    b=t2.get()
    c=t3.get()
    if (a>=50 and b>=50 and c>=50):
        t4.set("Pass")
        t14.config(bg="green")
    else:
        t4.set("Fail")
        t14.config(bg="red")
    return


t1=IntVar()
t2=IntVar()
t3=IntVar()
t4=IntVar()


f1 = Frame(root, bg="#f04", bd=20)
f1.pack(fill=BOTH)

l1 = Label(f1, text="Student Mark List", bg="#f04", fg="#fff", font=("arial", 18))
l1.pack()

f2 = Frame(root, bg="#fea", bd=20)
f2.pack(fill=BOTH)

f3 = Frame(root, bg="#fea", bd=20)
f3.pack(fill=BOTH)

l11 = Label(f2, text="Tamil", bg="#fea", fg="#f04", font=("arial", 14))
l11.pack()

t11 = Entry(f2,textvariable=t1, width=60, bd=10)
t11.pack()

l22 = Label(f2, text="English", bg="#fea", fg="#f04", font=("arial", 14))
l22.pack()

t12 = Entry(f2,textvariable=t2, width=60, bd=10)
t12.pack()

l13 = Label(f2, text="Maths", bg="#fea", fg="#f04", font=("arial", 14))
l13.pack()

t13 = Entry(f2, textvariable=t3 ,width=60, bd=10)
t13.pack()

l14 = Label(f2, text="Answer", bg="blue", fg="white", font=("arial", 14))
l14.pack()

t14 = Entry(f2, textvariable=t4 ,width=60, bd=10)
t14.pack()

b1 = Button(f3, text="Average", width=5, bg="black", fg="white", bd=10, relief="flat", command=average)
b1.grid(row=0,column=0, padx=10, pady=5)

b2 = Button(f3, text="Total", width=5, bg="black", fg="white", bd=10, relief="flat", command=total)
b2.grid(row=0,column=1, padx=10, pady=5)

b3 = Button(f3, text="Grade", width=5, bg="black", fg="white", bd=10, relief="flat", command=grade2)
b3.grid(row=0,column=2, padx=10, pady=5)

b4 = Button(f3, text="Result", width=5, bg="black", fg="white", bd=10, relief="flat", command=result1)
b4.grid(row=0,column=3, padx=10, pady=5)

root.mainloop()