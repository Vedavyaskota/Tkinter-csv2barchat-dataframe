#vedayvas bar chat
import tkinter
from tkinter import *
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title("data to bar chart")
root['bg'] = 'white'

df = pd.read_csv("sample CSV file.csv")     #path

fig = plt.figure(figsize=(6,6) , dpi=100)
labels = data['Customer Name']
labelpos = np.arange(len(labels))
days = data['Lbl By Days']

plt.bar(labelpos, days , align='center', alpha=1.0)
plt.xticks(labelpos,labels)
plt.xlabel('Customer',fontsize=18)
plt.ylabel('Lbl By Days',fontsize=16)
plt.tight_layout(pad=5)
plt.title('Lbl By Days')
plt.xticks(rotation=90, horizontalalignment="center" )

for index, datapoints in enumerate(days):
    plt.text(x=index , y=datapoints + 0.3 , s=f"{datapoints}",fontdict=dict(fontsize=10),ha='center',va='bottom')

#plt.show()

canvasbar = FigureCanvasTkAgg(fig, master=root)
canvasbar.draw()
# canvasbar.get_tk_widget().place(relx=0.5,rely=0.5,anchor=CENTER)
canvasbar.get_tk_widget().pack(side=tkinter.RIGHT , fill=tkinter.BOTH)

root.mainloop()
