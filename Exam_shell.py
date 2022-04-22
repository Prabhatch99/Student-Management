from tkinter import *
from tkinter import ttk
import pymysql
class Exam:
    def __init__(self,root):
        self.root=root
        self.root.configure(bg="gray")
        self.root.title("Exam Management System")
        self.root.geometry("1350x700+0+0")





        # function for moving back to home page========>>

        def homepage():
            self.root.destroy()
            import clg_front

        #frame for heading---------
        Manage_frame=Frame(self.root,bd=4,relief=SOLID,bg="light green")
        Manage_frame.place(x=0,y=1,width=1279,height=85)

        title = Label(Manage_frame, text="Exam Management System", bd=7,
                      relief=SUNKEN, width=40,
                      font=("times new roman", 35, "bold"),
                      bg="light green", fg="black")
        title.pack(side=LEFT)


        home_button = Button(Manage_frame,fg="black",bg="tomato",text="HOME PAGE >>",
             font=("times new roman",12,"bold"),activebackground="yellow" ,
             height=1,width=19,command=homepage)
        home_button.pack(side=RIGHT)



        ###ALl variables for Database
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.fathers_name_var = StringVar()
        self.obtained_marks_var = StringVar()
        self.total_marks_var = StringVar()
        self.percentage_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()



        #Mange frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light green")
        Manage_Frame.place(x=5,y=100,width=510,height=585)

        m_title=Label(Manage_Frame,text="Manage Student Marks",bg="light green", bd=4, relief=RIDGE  ,fg="black",
                      font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_rollnumber=Label(Manage_Frame,text="Roll Number:",bg="light green",fg="black",
                      font=("times new roman",20,"bold"))
        lbl_rollnumber.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_rollnumber=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("Arial",15,"bold"),bd=4,relief=GROOVE)
        txt_rollnumber.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name:", bg="light green",fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.name_var, font=("Arial", 15, "bold"),
                         bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_fathername = Label(Manage_Frame, text="Father's Name:", bg="light green", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_fathername.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_fathername = Entry(Manage_Frame,textvariable=self.fathers_name_var, font=("times new roman", 15, "bold"),
                         bd=4, relief=GROOVE)
        txt_fathername.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_obtainedmark = Label(Manage_Frame, text="Obtained Marks:", bg="light green", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_obtainedmark.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_obtainedmarks = Entry(Manage_Frame,textvariable=self.obtained_marks_var, font=("times new roman", 15, "bold"),
                         bd=4, relief=GROOVE)
        txt_obtainedmarks.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_totalmarks = Label(Manage_Frame, text="Total Marks:", bg="light green", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_totalmarks.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_totalmarks = Entry(Manage_Frame,textvariable=self.total_marks_var,
                               font=("times new roman", 15, "bold"),
                         bd=4, relief=GROOVE)
        txt_totalmarks.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_percentage = Label(Manage_Frame, text="Percentage %:", bg="light green", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_percentage.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_percentage = Entry(Manage_Frame,textvariable=self.percentage_var, font=("times new roman", 15, "bold"),
                         bd=4, relief=GROOVE)
        txt_percentage.grid(row=7, column=1, pady=10, padx=20, sticky="w")

       

        #------BUTTON FRAME____
        btn_frame=Frame(Manage_Frame,bd=5,relief=SUNKEN,bg="black")
        btn_frame.place(x=20,y=450,width=425)

        Addbtn=Button(btn_frame,text="Add",font=("Arial bold",10),activebackground='yellow',
                      width=9,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame, text="Update",font=("Arial bold",10),activebackground='yellow',
                         width=9,command=self.update_data).grid(row=0,column=1,padx=5,pady=5)
        deletebtn= Button(btn_frame, text="Delete",font=("Arial bold",10),activebackground='yellow',
                          width=9,command=self.delete_data).grid(row=0, column=2,padx=10, pady=10)
        clearbtn= Button(btn_frame, text="Clear",font=("Arial bold",10),activebackground='yellow',
                         width=9,command=self.clear).grid(row=0, column=3,padx=10, pady=10)
        

        #Detail____frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light green")
        Detail_Frame.place(x=520,y=100,width=750,height=585)

        lbl_search = Label(Detail_Frame, text="Search By", bg="light green",fg="black",
                            font=("times new roman", 20,"bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")


        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,
                        font=("times new roman", 12, ), state='readonly')
        combo_search['values'] = ("Roll_no", "Name", "Father's name")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=20,
                        font=("times new roman",10,"bold"),bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=13, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search",font=("Arial bold",10),activebackground='yellow' ,
                           width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn= Button(Detail_Frame, text="Show All",font=("Arial bold",10),activebackground='yellow',
                           width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=13)
        
     #------Table-Frame-----
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="GRAY")
        Table_Frame.place(x=10, y=70, width=730, height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("rollnumber","name","fathername","obtainedmark","totalmark","percentage"),
                                     xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("rollnumber",text="Roll Number")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("fathername",text="Father Name")
        self.Student_table.heading("obtainedmark",text="Obtained Marks")
        self.Student_table.heading("totalmark",text="Total Marks")
        self.Student_table.heading("percentage",text="Percentage %")
        self.Student_table.column("rollnumber",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("fathername", width=100)
        self.Student_table.column("obtainedmark", width=100)
        self.Student_table.column("totalmark", width=100)
        self.Student_table.column("percentage", width=100)
        self.Student_table['show']='headings'
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into exam_shell values(%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.fathers_name_var.get(),
                                                                         self.obtained_marks_var.get(),
                                                                         self.total_marks_var.get(),
                                                                         self.percentage_var.get()
                                                                         ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="",database="stm")
        cur = con.cursor()
        cur.execute("select * from exam_shell")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

            con.commit()
        con.close()


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.fathers_name_var.set("")
        self.obtained_marks_var.set("")
        self.total_marks_var.set("")
        self.percentage_var.set("")


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.fathers_name_var.set(row[2])
        self.obtained_marks_var.set(row[3])
        self.total_marks_var.set(row[4])
        self.percentage_var.set(row[5])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update exam_shell set name=%s,fathers_name=%s,obtained_marks=%s,total_marks=%s,percentage=%s where Roll_no=%s",(
                                                            self.name_var.get(),
                                                           self.fathers_name_var.get(),
                                                          self.obtained_marks_var.get(),
                                                         self.total_marks_var.get(),
                                                         self.percentage_var.get(),
                                                          self.Roll_No_var.get()
                                                                              ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="",database="stm")
        cur = con.cursor()
        cur.execute("delete from exam_shell where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="",database="stm")
        cur = con.cursor()
        cur.execute("select * from exam_shell where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

            con.commit()
        con.close()

root=Tk()
object=Exam(root)
root.mainloop()

