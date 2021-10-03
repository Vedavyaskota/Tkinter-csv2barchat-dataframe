from tkinter import *
import pandas as pd
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

root=Tk()
root.geometry("700x500")
root['bg'] = 'white'
root.state("zoomed")
root.title("data from csv file")
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))

style = ttk.Style()
style.theme_use('clam')

my_frame = Frame(root)          #create frame
my_frame.pack(pady=20)

my_tree = ttk.Treeview(my_frame)            #create treeview

df = pd.read_csv("sample CSV file.csv")     #path

my_tree["column"] = list(df.columns)            #setup new treeview
my_tree["show"] = "headings"

for column in my_tree["column"]:                    #Loop thru column list
    my_tree.heading(column , text=column , anchor=CENTER )
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

fig = plt.figure(figsize=(5, 5))            #creating barchat
labels = df['Customer Name']
labelpos = np.arange(len(labels))
days = df['Lbl By Days']

plt.bar(labelpos, days, align='center', alpha=1.0)
plt.xticks(labelpos, labels)
plt.xlabel('Customer', fontsize=18)
plt.ylabel('Lbl By Days', fontsize=16)
plt.tight_layout(pad=5) #w_pad=0.5 , h_pad=0.1
plt.title('Bar chat of csv file')
plt.xticks(rotation=90, horizontalalignment="center")

for index, datapoints in enumerate(days):               #to show value on top of bar
    plt.text(x=index, y=datapoints + 0.3, s=f"{datapoints}", fontdict=dict(fontsize=7), ha='center', va='bottom')

#plt.show()

canvasbar = FigureCanvasTkAgg(fig, master=root)         #to show barchat output in tkinder
canvasbar.draw()
canvasbar.get_tk_widget().place(relx=0.5,rely=0.65,anchor=CENTER)
# canvasbar.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

root.mainloop()
