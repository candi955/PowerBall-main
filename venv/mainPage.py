# Main program page

# reference: https://stackoverflow.com/questions/40526496/vertical-scrollbar-for-frame-in-tkinter-python

#---------Imports----------------------------------------------------------------------------------------------------
# Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox

# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd


# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
fullLottoExcel = xlrd.open_workbook('LottoNumList25Jun1997_20Sep2020_Table_AllFloats.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = fullLottoExcel.sheets()
for sheet in sheets:
   lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
pd.set_option('display.max_rows', 3000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 11)
pd.set_option('display.width', 300)
pd.set_option('display.max_colwidth',23)

# creating dataframe for tkinter
df = pd.DataFrame(lottoSheetData)

#-----Tkinter functions----------------------------------------------------------------------------

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

#----- Creating Tkinter Setup (root) for GUI #-----


root = tk.Tk()
root.title('AZ Powerball Lottery Prediction Main Menu')

# --- create canvas with scrollbar ---

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- program functions ---
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def onButtonClick(buttonClicks):
    if buttonClicks == 1:
        import WhiteBall1
    if buttonClicks == 2:
        import WhiteBall2
    if buttonClicks == 3:
        import WhiteBall3
    if buttonClicks == 4:
        import WhiteBall4
    if buttonClicks == 5:
        import WhiteBall5
    if buttonClicks == 6:
        import RedBall
    if buttonClicks == 7:
        # Creating pop up window for dataset
        # reference: https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        win = tk.Toplevel()
        win.wm_title("Full AZ Powerball Lottery Prediction dataset used for prediction algorithm")

        popUpLabel = tk.Label(win, text="Dataset created by program author utilizing the website " +
                                        "https://www.lottostrategies.com/cgi-bin/winning_select_state/203/AZ/arizona" +
                                        "-lottery-numbers-archive.html")
        popUpLabel.grid(row=0, column=0)

        # Display Boxes for Results
        dataSetDisplay = ScrolledText(win, height=35, width=150)
        dataSetDisplay.grid(row=4, column=0, columnspan=5, padx=5, pady=5)
        dataSetDisplay.insert(1.0, pd.DataFrame(df))

    if buttonClicks == 8:
        exit()

def flush(self):
    pass


# --- add widgets in frame ---

labelOne = tk.Label(frame, text='Please click on one of the following program choices:', padx=5, pady=5, font="-size 10")
labelOne.pack()

WB1_PageButton = tk.Button(frame, text='Prediction of White Ball 1', command=lambda: onButtonClick(1),
                             height=2, width=30, bg='purple', fg='#fff')
WB1_PageButton.pack()

WB2_PageButton = tk.Button(frame, text='Prediction of White Ball 2', command= lambda: onButtonClick(2),
                             height=2, width=30, bg='purple', fg='#fff')
WB2_PageButton.pack()

WB3_PageButton = tk.Button(frame, text='Prediction of White Ball 3', command= lambda: onButtonClick(3),
                             height=2, width=30, bg='purple', fg='#fff')
WB3_PageButton.pack()

WB4_PageButton = tk.Button(frame, text='Prediction of White Ball 4', command= lambda: onButtonClick(4),
                             height=2, width=30, bg='purple', fg='#fff')
WB4_PageButton.pack()

WB5_PageButton = tk.Button(frame, text='Prediction of White Ball 5', command= lambda: onButtonClick(5),
                             height=2, width=30, bg='purple', fg='#fff')
WB5_PageButton.pack()

RedBallButton = tk.Button(frame, text='Prediction of Red Ball', command= lambda: onButtonClick(6),
                             height=2, width=30, bg='purple', fg='#fff')
RedBallButton.pack()

DataSetPageButton = tk.Button(frame, text='Original dataset', command= lambda: onButtonClick(7),
                             height=2, width=30, bg='blue', fg='#fff')
DataSetPageButton.pack()

ExitButton = tk.Button(frame, text='Exit program',
                          command=lambda: onButtonClick(8), height=2, width=30, bg='green', fg='#fff')
ExitButton.pack()

# --- start program ---

root.mainloop()