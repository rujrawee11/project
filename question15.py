from tkinter import *
def question15():  
    def sel():
        """1 ans"""
        if str(var.get()) == "1":
            print("no")

        elif str(var.get()) == "2":
            print("no")

        elif str(var.get()) == "3":
            print("YES")
            
        elif str(var.get()) == "4":
            print("no")
    """1 ans"""
    root = Tk()
    root.title("question")#ชื่อ
    root.geometry("600x500")
    root.option_add("*font","Opun-Mai-Thin 10 bold")
    frame = Frame(root)
    frame.config(background="#C6E0E0")
    frame.place(width=600, height=500, x=0, y=0)
    root.option_add("*foreground", "navy")
    label1 = Label(frame, text="QUESTION ?", width=15, height = 2, bg="white")
    label1.grid(column=0,row=0, columnspan=2,padx=15,pady=30)
    label2 = Label(frame, text=" error ที่เกิดจากความผิดพลาดของ algorithm \nของผู้เขียนโปรแกรมคือข้อใด?", width=50, height = 5, bg="white")
    label2.grid(column=0, row=1, columnspan=3, padx=10,pady=3)
    var = IntVar()
    r1 = Radiobutton(frame, text="Runtime Errors", width=15, height=3, variable=var, value=1,
                    bg="white", activebackground='red', command=sel)#คำตอบแรก
    r1.grid(column=0, row=2, padx=75, pady=30)
    r2 = Radiobutton(frame, text="Syntax Errors", width=15, height=3 ,variable=var, value=2,
                    bg="white", activebackground='red', command=sel)  # คำตอบสอง
    r2.grid(column=1, row=2, padx=75, pady=15)
    r3 = Radiobutton(frame, text="Semantic  Errors", width=15, height=3, variable=var, value=3,
                    bg="white", activebackground='green', command=sel)  # คำตอบสาม
    r3.grid(column=0, row=3, padx=15, pady=15)
    r4 = Radiobutton(frame, text="Value  Errors", width=15, height=3, variable=var, value=3,
                    bg="white", activebackground='red', command=sel)  # คำตอบสี่
    r4.grid(column=1, row=3, padx=15, pady=15)
    label = Label(root)
    label.pack()
    root.mainloop()
question15()