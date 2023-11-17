from tkinter import *  

root = Tk()
root.geometry("500x700")
root.title("Project")

f1 = Frame(root, bg="#f04", bd=20)
f1.pack(fill=BOTH)

l1 = Label(f1, text="student registration", bg="#f04", fg="#fff", font=("arial", 18))
l1.pack()

f2 = Frame(root, bg="#fea", bd=20)
f2.pack(fill=BOTH)

l11 = Label(f2, text="student Name", bg="#fea", fg="#f04", font=("arial", 14))
l11.pack()

t11 = Entry(f2, width=40)
t11.pack()

l12 = Label(f2, text="course", bg="#fea", fg="#f04", font=("arial", 14))
l12.pack()

t11 = Entry(f2, width=40)
t11.pack()

l12 = Label(f2, text="Year", bg="#fea", fg="#f04", font=("arial", 14))
l12.pack()

t12 = Entry(f2, width=40, bd=10, relief=SOLID)
t12.pack()

l12 = Label(f2, text="reg no", bg="#fea", fg="#f04", font=("arial", 14))
l12.pack()

t12 = Entry(f2, width=40, bd=10, relief=GROOVE)
t12.pack()

l12 = Label(f2, text="DOB", bg="#fea", fg="#f04", font=("arial", 14))
l12.pack()

t12 = Entry(f2, width=40, bd=10, relief=SUNKEN)
t12.pack()

l12 = Label(f2, text="Mail ID", bg="#fea", fg="#f04", font=("arial", 14))
l12.pack()

t12 = Entry(f2, width=40, bd=10, relief="flat")
t12.pack(padx=10, pady=10)

b1 = Button(f2, text="Register", width=30, bg="green", fg="yellow", bd=5, relief=RIDGE, activebackground="blue", height=2)
b1.pack()

top.mainloop()  
