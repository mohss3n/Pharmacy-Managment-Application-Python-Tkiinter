from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3


root = tk.Tk()
root.title("Mohssen Pharmacie")
root.geometry("1600x660")
root.resizable(False,False)
##root.configure(bg='green')##



conn = sqlite3.connect('mydb.db')
c = conn.cursor()

num = tk.IntVar()
name2 = tk.StringVar()
forn = tk.StringVar()
byp = tk.StringVar()
selp = tk.StringVar()
sellm = tk.StringVar()
searchid=tk.StringVar()
searchn=tk.IntVar()
delete1=tk.IntVar()
searchpp=tk.IntVar()


manager1=Frame(root,bg="white")

tit=Label(root,text="Mohssen Pharmacie",bg="#1AAECB",font=('monospace',15,'bold'),fg="white").pack(fill=X)

def chercher():
    print(searchpp.get())
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    for row in rows:
        if row[0] == searchpp.get():
            student_table.insert(parent='', index='end', iid=0, text='',
                                 values=(row[0], row[1], row[2], row[3], row[4], row[5]))
#inputs


manager1.place(x=0,y=330,width=340,height=325)
tit2=Label(manager1,text=" Search DATA",font=('Deco',12,'bold'),fg="white",bg="#2980B9")
tit2.pack(fill=X)
serts = Label(manager1,background="white",text="entre product id : ",font=('monospace',15,'bold')).place(x=20,y=30)
button = tk.Button(manager1, text="Search Stock",fg="white",bg="red",font=('monospace',14,'bold'), command=chercher).place(x=80,y=110,width=160,height=30)
manager=Frame(root,bg="white")
manager.place(x=0,y=30,width=340,height=295)
tit1=Label(manager,text="Product DATA",font=('Deco',12,'bold'),fg="white",bg="#2980B9")
tit1.pack(fill=X)
lbl1 = Label(manager,background="white",font=('monospace',12,'bold'),text="Entre Medicament ID:").pack()
numero= tk.Entry(manager, textvariable=num).pack()
name = Label(manager,background="white",font=('monospace',12,'bold'),text="entre Product Name").pack()
name2w = tk.Entry(manager, textvariable=name2).pack()
forn1 = Label(manager,background="white",font=('monospace',12,'bold'),text="entre Supplier name").pack()
fornw = tk.Entry(manager, textvariable=forn).pack()
byp1 = Label(manager,background="white",font=('monospace',12,'bold'),text="entre buying price").pack()
bypw = tk.Entry(manager, textvariable=byp).pack()
byp1 = Label(manager,background="white",font=('monospace',12,'bold'),text="entre selling price").pack()
selpw = tk.Entry(manager, textvariable=selp).pack()
searchsp= tk.Entry(manager1,textvariable=searchpp).place(x=75,y=60)

















def ajouter():
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''
              INSERT OR REPLACE INTO products (product_id, product_name,supplier,buying_price,selling_price)

                    VALUES

                    (?,?,?,?,?)''', (num.get(), name2.get(), forn.get(), byp.get(), selp.get())
              )
    conn.commit()




def supprimer():
    print(searchpp.get())
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    rows = cur.fetchall()
    sql_delete_query = ("DELETE FROM products WHERE product_id = ?")
    cur.execute(sql_delete_query,[searchpp.get()])
    conn.commit()
    print("Record deleted successfully ")
    for row in rows:
        print(row)







def modify():
    #print(nametop.get())
    conn = sqlite3.connect('test_database20.db')
    c = conn.cursor()
    c.execute(
        "UPDATE products SET  (product_name,supplier,buying_price,selling_price,Sales)= (?,?,?,?,?) WHERE pid_azz = ?",
        (num.get(),name2.get(), forn.get(), byp.get(), selp.get(), searchpp.get()))
    conn.commit()
    print("kkkk")



#button
button = tk.Button(manager1, text="Add Item", command=ajouter,fg="white",bg="green",font=('monospace',14,'bold'))
button.place(x=80,y=145,width=160,height=30)

exit_button=Button(manager1,text="EXIT",command=root.destroy,fg="white",bg="yellow",font=('monospace',14,'bold')).place(x=80,y=285,width=160,height=30)
reset=Button(manager1,text="RESET",fg="white",bg="blue",font=('monospace',14,'bold')).place(x=80,y=250,width=160,height=30)
modifi=Button(manager1,text="MODIFIER",fg="white",bg="purple" ,command=modify,font=('monospace',14,'bold')).place(x=80,y=215,width=160,height=30)


#table

datas=Frame(root,bg="red")
datas.place(x=350,y=30,width=1250,height=625)

student_table=ttk.Treeview(datas,
      columns=('ID','product name','Supplier','Buying Price','Selling Price'),
    )

student_table.place(x=0,y=0,width=1250,height=625)

#----title-----------------
student_table['show']='headings'
student_table.heading('ID',text='ID')
student_table.heading('product name',text='product name')
student_table.heading('Supplier',text='Supplier')
student_table.heading('Buying Price',text='Buying Price')
student_table.heading('Selling Price',text='Selling Price')


#---------------titles------------






sup1=tk.Button(manager1,text="DELETE",command=supprimer,fg="white",bg="orange",font=('monospace',14,'bold')).place(x=80,y=180,width=160,height=30)





root.mainloop()
