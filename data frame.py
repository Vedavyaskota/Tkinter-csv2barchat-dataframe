from tkinter import *
import pandas as pd
from tkinter import ttk

root=Tk()
root.geometry("700x500")

style = ttk.Style()
style.theme_use('clam')

my_frame = Frame(root)          #create frame
my_frame.pack(pady=20)

my_tree = ttk.Treeview(my_frame)            #create treeview

df = pd.read_csv("sample CSV file.csv")     #path

my_tree["column"] = list(df.columns)            #setup new treeview
my_tree["show"] = "headings"

for column in my_tree["column"]:                    #Loop thru column list
    my_tree.heading(column , text=column , anchor=CENTER)
    my_tree.column("Sno",width=30 , anchor=CENTER)
    my_tree.column("Customer Name",width=100)
    my_tree.column("PO No",width=80)
    my_tree.column("PO Date",width=80)
    my_tree.column("Buyer Name",width=100)
    my_tree.column("Lbl By Days",width=80)
    my_tree.column("Lbl Date",width=80)

df_rows = df.to_numpy().tolist()            #put data in treeview
for rows in df_rows:
    my_tree.insert("","end",value=rows)

my_tree.pack()                  #pack the treeview finally
root.mainloop()
