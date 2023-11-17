from tkinter import *

root = Tk()
root.geometry("348x470")
root.title("sample calculator")

def one():
    a = text.get()
    if a==0:
        text.set("1")
    else:
        text.set(str(a)+"1")
    return
def two():
    a=text.get()
    if a==0:
        text.set("2")
    else:
        text.set(str(a)+"2")
    return
def three():
    a=text.get()
    if a==0:
        text.set("3")
    else:
        text.set(str(a)+"3")
    return
def four():
    a=text.get()
    if a==0:
        text.set("4")
    else:
        text.set(str(a)+"4")
    return
def five():
    a=text.get()
    if a==0:
        text.set("5")
    else:
        text.set(str(a)+"5")
    return
def six():
    a=text.get()
    if a==0:
        text.set("6")
    else:
        text.set(str(a)+"6")
    return
def seven():
    a=text.get()
    if a==0:
        text.set("7")
    else:
        text.set(str(a)+"7")
    return
def eight():
    a=text.get()
    if a==0:
        text.set("8")
    else:
        text.set(str(a)+"8")
    return
def nine():
    a=text.get()
    if a==0:
        text.set("9")
    else:
        text.set(str(a)+"9")
    return
def zero():
    a=text.get()
    if a==0:
        text.set("0")
    else:
        text.set(str(a)+"0")
    return

def add():
    a=text.get()
    text.set("0")
    text1.set(a)
    text2.set(1)
    return
def sub():
    a=text.get()
    text.set("0")
    text1.set(a)
    text2.set(2)
    return
def multiply():
    a=text.get()
    text.set("0")
    text1.set(a)
    text2.set(3)
    return
def divide():
    a=text.get()
    text.set("0")
    text1.set(a)
    text2.set(4)
    return

def equalto():
    a=text.get()
    b=text1.get()
    c=text2.get()
    if c==1:
        ans = b+a
    if c==2:
        ans = b-a
    if c==3:
        ans= a*b
    if c==4:
        ans= a/b
    text.set(ans)
    return
def cleartext():
    a=text.set("0")
    return
def cleartext2():
    a=text.set("")
    return
def cleartext3():
    a=text.set("0")
    return
text = IntVar()
text1 = IntVar()
text2 = IntVar()
f1 = Frame(root, bg="#f04", bd=20)
f1.pack(fill=BOTH)

l1 = Label(f1, text="Calculator", bg="#f04", fg="#fff", font=("arial", 18))
l1.pack()

f2 = Frame(root, bg="#fea", bd=20)
f2.pack(fill=BOTH)

f3 = Frame(root, bg="#fea", bd=5)
f3.pack(fill=BOTH)

f4 = Frame(root, bg="#fea", bd=5)
f4.pack(fill=BOTH)

f5 = Frame(root, bg="#fea", bd=5)
f5.pack(fill=BOTH)

f6 = Frame(root, bg="#fea", bd=5)
f6.pack(fill=BOTH)

f7 = Frame(root, bg="#fea", bd=5)
f7.pack(fill=BOTH)

t11 = Entry(f2, width=60, bd=10, relief="flat", textvariable=text)
t11.pack()
t12 = Entry(f2, width=60, bd=10, relief="flat", textvariable=text1)
t12.pack_forget()
t13 = Entry(f2, width=60, bd=10, relief="flat", textvariable=text2)
t13.pack_forget()

b1 = Button(f3, text="%", width=5, bg="black", fg="white", bd=10, relief="flat")
b1.grid(row=0, column=0, padx=10, pady=5)

b2 = Button(f3, text="off", width=5, bg="black", fg="white", bd=10, relief="flat",command=cleartext2)
b2.grid(row=0, column=1, padx=10, pady=5)

b3 = Button(f3, text="on", width=5, bg="black", fg="white", bd=10, relief="flat",command=cleartext3)
b3.grid(row=0, column=2, padx=10, pady=5)

b4 = Button(f3, text="clear", width=5, bg="black", fg="white", bd=10, relief="flat",command=cleartext)
b4.grid(row=0, column=3, padx=10, pady=5)

b1 = Button(f4, text="7", width=5, bg="black", fg="white", bd=10, relief="flat",command=seven)
b1.grid(row=0, column=0, padx=10, pady=5)

b2 = Button(f4, text="8", width=5, bg="black", fg="white", bd=10, relief="flat", command=eight)
b2.grid(row=0, column=1, padx=10, pady=5)

b3 = Button(f4, text="9", width=5, bg="black", fg="white", bd=10, relief="flat", command=nine)
b3.grid(row=0, column=2, padx=10, pady=5)

b4 = Button(f4, text="*", width=5, bg="black", fg="white", bd=10, relief="flat", command=multiply)
b4.grid(row=0, column=3, padx=10, pady=5)

b1 = Button(f5, text="4", width=5, bg="black", fg="white", bd=10, relief="flat", command=four)
b1.grid(row=0, column=0, padx=10, pady=5)

b2 = Button(f5, text="5", width=5, bg="black", fg="white", bd=10, relief="flat", command=five)
b2.grid(row=0, column=1, padx=10, pady=5)

b3 = Button(f5, text="6", width=5, bg="black", fg="white", bd=10, relief="flat",command=six)
b3.grid(row=0, column=2, padx=10, pady=5)

b4 = Button(f5, text="-", width=5, bg="black", fg="white", bd=10, relief="flat",command=sub)
b4.grid(row=0, column=3, padx=10, pady=5)

b1 = Button(f6, text="1", width=5, bg="black", fg="white", bd=10, relief="flat", command=one)
b1.grid(row=0, column=0, padx=10, pady=5)

b2 = Button(f6, text="2", width=5, bg="black", fg="white", bd=10, relief="flat", command=two)
b2.grid(row=0, column=1, padx=10, pady=5)

b3 = Button(f6, text="3", width=5, bg="black", fg="white", bd=10, relief="flat", command=three)
b3.grid(row=0, column=2, padx=10, pady=5)

b4 = Button(f6, text="+", width=5, bg="black", fg="white", bd=10, relief="flat", command=add)
b4.grid(row=0, column=3, padx=10, pady=5)

b1 = Button(f7, text="/", width=5, bg="black", fg="white", bd=10, relief="flat", command=divide)
b1.grid(row=0, column=0, padx=10, pady=5)

b2 = Button(f7, text="0", width=5, bg="black", fg="white", bd=10, relief="flat", command=zero)
b2.grid(row=0, column=1, padx=10, pady=5)

b3 = Button(f7, text=".", width=5, bg="black", fg="white", bd=10, relief="flat")
b3.grid(row=0, column=2, padx=10, pady=5)

b4 = Button(f7, text="=", width=5, bg="blue", fg="white", bd=10, relief="flat" ,command=equalto)
b4.grid(row=0, column=3, padx=10, pady=5)


root.mainloop()
