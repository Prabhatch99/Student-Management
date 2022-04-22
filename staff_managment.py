from tkinter import *
from tkinter import ttk
import pymysql
class Staff:
    def __init__(self,root):
        self.root=root
        self.root.configure(bg="light gray")
        self.root.title("Staff Management System")
        self.root.geometry("1267x685+0+0")

        def homepage():
            self.root.destroy()
            import clg_front


        #frame for heading---------
        Manage_frame=Frame(self.root,bd=4,relief=SOLID,bg="light blue")
        Manage_frame.place(x=0,y=1,width=1279,height=85)


        title=Label(Manage_frame,text="Staff Management System",bd=7 ,relief=SUNKEN,width=40,
                    font=("times new roman",35,"bold"),bg="light blue",fg="black")
        title.pack(side=LEFT)

        home_button = Button(Manage_frame,fg="black",bg="tomato",text="HOME PAGE >>",
             font=("times new roman",12,"bold"),activebackground="yellow" ,
             height=1,width=19,command=homepage)
        home_button.pack(side=RIGHT)

        ###ALl variables for Database
        self.employee_id_var = StringVar()
        self.name_var = StringVar()
        self.subject_name_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.salary_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()



        #Mange frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=5,y=100,width=510,height=585)

        m_title=Label(Manage_Frame,text="Manage Staff Members",bg="light blue",fg="black",
                      font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_empid=Label(Manage_Frame,text="Employee Id:",bg="light blue",fg="black",
                      font=("times new roman",20,"bold"))
        lbl_empid.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_empid=Entry(Manage_Frame,textvariable=self.employee_id_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_empid.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name:", bg="light blue",fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman", 15, "bold"),
                         bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_subjectname = Label(Manage_Frame, text="Subject Name:", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_subjectname.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_subjectname = Entry(Manage_Frame,textvariable=self.subject_name_var, font=("times new roman", 15, "bold"),
                         bd=5, relief=GROOVE)
        txt_subjectname.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame,textvariable=self.gender_var, text="Gender:", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 13),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_contactno = Label(Manage_Frame, text="Contact No:", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_contactno.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contactno = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"),
                         bd=5, relief=GROOVE)
        txt_contactno.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_salary = Label(Manage_Frame, text="Salary:", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_salary.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_salary = Entry(Manage_Frame,textvariable=self.salary_var, font=("times new roman", 15, "bold"),
                         bd=5, relief=GROOVE)
        txt_salary.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address:", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame,width=20,height=3, font=("times new roman", 15, "bold"),
                         bd=5, relief=GROOVE)
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #------BUTTON FRAME____
        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light blue")
        btn_frame.place(x=20,y=510,width=425)

        Addbtn=Button(btn_frame,text="Add",font=("Arial bold",10),activebackground='yellow',width=9,
                      command=self.add_staff).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame, text="Update",font=("Arial bold",10),activebackground='yellow', width=9,
                         command=self.update_data).grid(row=0,column=1,padx=5,pady=5)
        deletebtn= Button(btn_frame, text="Delete",font=("Arial bold",10),activebackground='yellow', width=9,
                          command=self.delete_data).grid(row=0, column=2,padx=10, pady=10)
        clearbtn= Button(btn_frame, text="Clear",font=("Arial bold",10),activebackground='yellow', width=9,
                         command=self.clear).grid(row=0, column=3,padx=10, pady=10)







        #Detail____frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        Detail_Frame.place(x=520,y=100,width=750,height=585)

        lbl_search = Label(Detail_Frame, text="Search By", bg="light blue",fg="black",
                            font=("times new roman", 20,"bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")


        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,
                        font=("times new roman", 12, ), state='readonly')
        combo_search['values'] = ("Employee_ID", "Name", "Subject_name")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_txt,
                           font=("times new roman",10,"bold"),bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame,command=self.search_data, text="Search",
                           font=("Arial bold",10),activebackground='yellow',
                           width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)

        showallbtn=Button(Detail_Frame,command=self.fetch_data,text="Show All",
                           font=("Arial bold",10),activebackground='yellow',
                           width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
        



       #------Table-Frame-----
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="GRAY")
        Table_Frame.place(x=10, y=70, width=730, height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Staff_table = ttk.Treeview(Table_Frame,columns=("id","name","subject","gender","contact","salary","address"),
                                     xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Staff_table.xview)
        scroll_y.config(command=self.Staff_table.yview)
        self.Staff_table.heading("id",text="Employee Id")
        self.Staff_table.heading("name",text="Name")
        self.Staff_table.heading("subject",text="Subject Name")
        self.Staff_table.heading("gender",text="Gender")
        self.Staff_table.heading("contact",text="Contact No")
        self.Staff_table.heading("salary",text="Salary")
        self.Staff_table.heading("address",text="Address")
        self.Staff_table.column("id",width=100)
        self.Staff_table.column("name",width=100)
        self.Staff_table.column("subject", width=100)
        self.Staff_table.column("gender", width=100)
        self.Staff_table.column("contact", width=100)
        self.Staff_table.column("salary", width=100)
        self.Staff_table.column("address", width=150)
        self.Staff_table['show']='headings'
        self.Staff_table.pack(fill=BOTH,expand=1)
        self.Staff_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_staff(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into staff_managment values(%s,%s,%s,%s,%s,%s,%s)",(self.employee_id_var.get(),
                                                                         self.name_var.get(),
                                                                         self.subject_name_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.salary_var.get(),
                                                                         self.txt_Address.get('1.0',END)
                                                                         ))
        con.commit()
        self.fetch_data()
        con.close()


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="",database="stm")
        cur = con.cursor()
        cur.execute("select * from staff_managment")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Staff_table.delete(*self.Staff_table.get_children())
            for row in rows:
                self.Staff_table.insert('',END,values=row)

            con.commit()
        con.close()



    def clear(self):
        self.employee_id_var.set("")
        self.name_var.set("")
        self.subject_name_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.salary_var.set("")
        self.txt_Address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.Staff_table.focus()
        contents=self.Staff_table.item(cursor_row)
        row=contents['values']
        self.employee_id_var.set(row[0])
        self.name_var.set(row[1])
        self.subject_name_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.salary_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update staff_managment set name=%s,subject_name=%s,gender=%s,contact=%s,salary=%s,address=%s where employee_id=%s",(
                                                            self.name_var.get(),
                                                           self.subject_name_var.get(),
                                                          self.gender_var.get(),
                                                         self.contact_var.get(),
                                                         self.salary_var.get(),
                                               self.txt_Address.get('1.0', END),
                                                          self.employee_id_var.get()
                                                                              ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()



    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="",database="stm")
        cur = con.cursor()
        cur.execute("delete from staff_managment where employee_id=%s",self.employee_id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="",database="stm")
        cur = con.cursor()
        cur.execute("select * from staff_managment where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Staff_table.delete(*self.Staff_table.get_children())
            for row in rows:
                self.Staff_table.insert('',END,values=row)

            con.commit()
        con.close()





root=Tk()
object=Staff(root)
root.mainloop()
