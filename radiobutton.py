from tkinter import *
def radiobutton():
    """1 ans"""
    root = Tk()
    root.title("question")#ชื่อ
    root.geometry("600x500")
    root.option_add("*font","tahoma 10 bold")
    frame = Frame(root)
    frame.config(background="cyan")
    frame.place(width=600, height=500, x=0, y=0)
    root.option_add("*foreground", "navy")
    label1 = Label(frame, text="question", width=45, height = 3);
    label1.grid(column=0,row=0, columnspan=2,padx=15,pady=30)
    label2 = Label(frame, text="detail ans", width=50, height = 5, bg="white")
    label2.grid(column=0, row=1, columnspan=3, padx=10,pady=3)
    var = IntVar()
    r1 = Radiobutton(frame, text="major", width=15, height=3, variable=var, value=1)#คำตอบแรก
    r1.grid(column=0, row=2, padx=75, pady=30)
    r2 = Radiobutton(frame, text="senior", width=15, height=3 ,variable=var, value=2)  # คำตอบสอง
    r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(frame, text="senior", width=15, height=3, variable=var, value=3)  # คำตอบสาม
    r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(frame, text="senior", width=15, height=3, variable=var, value=4)  # คำตอบสาม
    r4.grid(column=1, row=3, padx=15, pady=15)
    var.set(1)
    root.mainloop()
radiobutton()
