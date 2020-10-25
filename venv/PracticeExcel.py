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


# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictTwo = pd.Dataroot(listMonthDictionary)
#pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
#pd.set_option('display.max_columns', 1000)
#pd.set_option('display.width', 1000)

# ----------Opening and creating Dataroot-----------------------------------------------------------------------
# pulling excel file and creating variable
whiteBall1Excel = xlrd.open_workbook('LottoNumList25Jun1997_20Sep2020_Table_AllFloats.xlsx')
# Creating variable to convert excel file to a dataroot (using pandas)
sheets = whiteBall1Excel.sheets()
for sheet in sheets:
    whiteBall1SheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

    #  [rows:, :columns]
    # Singling out last 4 columns, all rows (weekday,month,day,year) for source data
    sources = whiteBall1SheetData[:,-4 :]
    # Singling out the 1st column, all rows (White Ball 1) as target data
    target = whiteBall1SheetData[:, :1]

    # Deleting header column from dataroot, both source and target data
    sourceNoHeader = np.delete(sources, (0), axis=0)
    targetNoHeader = np.delete(target, (0), axis=0)

    X = sourceNoHeader
    y = targetNoHeader

    #In case you want to check the dataset to make sure source and targets are being placed into program calculations
    # correctly:
    print("Source values Weekday, Month, Day, Year:")
    print(X)
    print("\n\n")
    print("Target values Whiteball 1:")
    print(y)
