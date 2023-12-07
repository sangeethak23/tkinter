from tkinter import *  
 
root = Tk()
root.geometry("350x470")
root.title("sample calculator")

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

t11 = Entry(f2, width=60, bd=10, relief="flat")
t11.pack()

b1 = Button(f3, text="%", width=5, bg="black", fg="white", bd=10, relief="flat")
b1.grid(row=0,column=0, padx=10, pady=5)

b2 = Button(f3, text="CE", width=5, bg="black", fg="white", bd=10, relief="flat")
b2.grid(row=0,column=1, padx=10, pady=5)

b3 = Button(f3, text="C", width=5, bg="black", fg="white", bd=10, relief="flat")
b3.grid(row=0,column=2, padx=10, pady=5)

b4 = Button(f3, text="clear", width=5, bg="black", fg="white", bd=10, relief="flat")
b4.grid(row=0,column=3, padx=10, pady=5)

b1 = Button(f4, text="7", width=5, bg="black", fg="white", bd=10, relief="flat")
b1.grid(row=0,column=0, padx=10, pady=5)

b2 = Button(f4, text="8", width=5, bg="black", fg="white", bd=10, relief="flat")
b2.grid(row=0,column=1, padx=10, pady=5)

b3 = Button(f4, text="9", width=5, bg="black", fg="white", bd=10, relief="flat")
b3.grid(row=0,column=2, padx=10, pady=5)

b4 = Button(f4, text="*", width=5, bg="black", fg="white", bd=10, relief="flat")
b4.grid(row=0,column=3, padx=10, pady=5)

b1 = Button(f5, text="4", width=5, bg="black", fg="white", bd=10, relief="flat")
b1.grid(row=0,column=0, padx=10, pady=5)

b2 = Button(f5, text="5", width=5, bg="black", fg="white", bd=10, relief="flat")
b2.grid(row=0,column=1, padx=10, pady=5)

b3 = Button(f5, text="6", width=5, bg="black", fg="white", bd=10, relief="flat")
b3.grid(row=0,column=2, padx=10, pady=5)

b4 = Button(f5, text="-", width=5, bg="black", fg="white", bd=10, relief="flat")
b4.grid(row=0,column=3, padx=10, pady=5)

b1 = Button(f6, text="1", width=5, bg="black", fg="white", bd=10, relief="flat")
b1.grid(row=0,column=0, padx=10, pady=5)

b2 = Button(f6, text="2", width=5, bg="black", fg="white", bd=10, relief="flat")
b2.grid(row=0,column=1, padx=10, pady=5)

b3 = Button(f6, text="3", width=5, bg="black", fg="white", bd=10, relief="flat")
b3.grid(row=0,column=2, padx=10, pady=5)

b4 = Button(f6, text="+", width=5, bg="black", fg="white", bd=10, relief="flat")
b4.grid(row=0,column=3, padx=10, pady=5)

b1 = Button(f7, text="/", width=5, bg="black", fg="white", bd=10, relief="flat")
b1.grid(row=0,column=0, padx=10, pady=5)

b2 = Button(f7, text="0", width=5, bg="black", fg="white", bd=10, relief="flat")
b2.grid(row=0,column=1, padx=10, pady=5)

b3 = Button(f7, text=".", width=5, bg="black", fg="white", bd=10, relief="flat")
b3.grid(row=0,column=2, padx=10, pady=5)

b4 = Button(f7, text="=", width=5, bg="blue", fg="white", bd=10, relief="flat")
b4.grid(row=0,column=3, padx=10, pady=5)


