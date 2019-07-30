#import stuff
import pandas
import numpy
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *


#init colors
lavender = 'lavender'
black = 'black'
grey = 'grey'
white = 'white'


#init tkinter window
root = tk.Tk()
root.title('Excel Line Graph Maker')
mainwindow = tk.Canvas(root, width = 300, height = 300, bg = lavender)
mainwindow.pack(fill="both", expand=True)


#button function
def getExcel():
	global datafile

	filepath = filedialog.askopenfilename()
	try:
		datafile = pandas.read_excel(filepath)
		if len(datafile.columns) == 2:
			x_label = datafile.columns[0]
			y_label = datafile.columns[1]
			x = datafile[x_label].tolist()
			y = datafile[y_label].tolist()
			plt.plot(x, y)
			plt.title(filepath)
			plt.xlabel(x_label)
			plt.ylabel(y_label)

			plt.show()
		else:
			popupwindow("Please select an excel file with 2 columns!")
	except:
		popupwindow("Please select an excel file!")


#def errormessage

def popupwindow(message):
	popup = tk.Tk()
	popup.wm_title("Error!")
	textlabel = tk.Label(popup, width=30, text=message, font=('helvetica', 10, 'bold'))
	textlabel.pack(side="top", fill="x", pady=10)
	okaybutton = tk.Button(popup, text="Okay", command=popup.destroy)
	okaybutton.pack()
	paddinglabel = tk.Label(popup, width=50, text="")
	paddinglabel.pack(side="bottom", fill="x", pady=10)

	popup.mainloop()

#build on top of window
message_1 = tk.Label(text='Excel Data Visualiser!\nCurrent version makes a line graph\nof 1 column of data.', bg = lavender, fg = black, font=('helvetica', 12, 'bold'))
browseButtonExcel = tk.Button(text = 'Import Excel File', command=getExcel, bg='grey', fg=white, font=('helvetica', 12, 'bold'))
mainwindow.create_window(150, 150, window=browseButtonExcel)
mainwindow.create_window(150, 50, window=message_1)


#loop
root.mainloop()

