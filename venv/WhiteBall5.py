# White Ball 5 prediction page
# reference: https://stackoverflow.com/questions/40526496/vertical-scrollbar-for-root-in-tkinter-python
# A good resource for Test/Train split (for test_size and random_state):
# https://machinelearningmastery.com/train-test-split-for-evaluating-machine-learning-algorithms/
# A good resource for the Lottery Winning Numbers in AZ:
# https://www.lottostrategies.com/cgi-bin/winning_by_state_period
# https://www.lottostrategies.com/cgi-bin/winning_select_state/203/AZ/arizona-lottery-numbers-archive.html

# ---------Imports----------------------------------------------------------------------------------------------------
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

# ------------ListBox Country/Region/Code Dictionaries--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated Code
# reference: https://www.w3schools.com/python/python_dictionaries.asp

# List 1 (Weekday)
listWeekDayDictionary = {"Sunday": {"Code": 1},
                        "Monday": {"Code": 2},
                        "Tuesday": {"Code": 3},
                        "Wednesday": {"Code": 4},
                        "Thursday": {"Code": 5},
                        "Friday": {"Code": 6},
                        "Saturday": {"Code": 7}}



# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictOne = pd.Dataroot(listWeekDayDictionary)
#pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
#pd.set_option('display.max_columns', 1000)
#pd.set_option('display.width', 1000)

# List 2 (Month and associated number)

listMonthDictionary = {"January": {"code": 1},  # list option 0
                       "February": {"Code": 2},  # list option 1
                       "March": {"Code": 3},  # list option 2
                       "April": {"Code": 4},  # list option 3
                       "May": {"Code": 5},  # list option 4
                       "June": {"Code": 6},  # list option 5
                       "July": {"Code": 7},  # list option 6
                       "August": {"Code": 8},  # list option 7
                       "September": {"Code": 9},  # list option 8
                       "October": {"Code": 10},  # list option 9
                       "November": {"Code": 11},  # list option 10
                       "December": {"Code": 12}}  # list option 11


# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictTwo = pd.Dataroot(listMonthDictionary)
#pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
#pd.set_option('display.max_columns', 1000)
#pd.set_option('display.width', 1000)

# ----------Opening and creating Dataroot-----------------------------------------------------------------------
# pulling excel file and creating variable
WhiteBall5Excel = xlrd.open_workbook('LottoNumList25Jun1997_20Sep2020_Table_AllFloats.xlsx')
# Creating variable to convert excel file to a dataroot (using pandas)
sheets = WhiteBall5Excel.sheets()
for sheet in sheets:
    WhiteBall5SheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

    #  [rows:, :columns]
    # Singling out last 4 columns, all rows (weekday,month,day,year) for source data
    sources = WhiteBall5SheetData[:,-4:]
    # Singling out the column, all rows (White Ball 5) as target data (row 4 to 5 really means
    # it will only print/pull from row 5)
    target = WhiteBall5SheetData[:, 4:5]

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
    print("Target values WhiteBall 5:")
    print(y)


    # test size and random states can be updated to check for most accurate prediction
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.80, random_state=20)

    model = svm.SVC(kernel='linear')
    model.fit(X_train, y_train.ravel())
    y_pred = model.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)


# ---Creating Tkinter functions----------------------------------------------------------------------------------------

# Creating listbox functions
# https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry
# https://www.youtube.com/watch?v=XJqUu85sMrA
# https://note.nkmk.me/en/python-tuple-list-unpack/
# List 1 function to place list and then transfer answer to textbox, for White Ball 5 choice
def get_WeekDayList():
    for i in List1.curselection():
        if i == 0:
            Sundaylist = listWeekDayDictionary.get("Sunday")
            for k, v in Sundaylist.items():
                SundayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (SundayCode))
        if i == 1:
            MondayList = listWeekDayDictionary.get("Monday")
            for k, v in MondayList.items():
                MondayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (MondayCode))
        if i == 2:
            Tuesdaylist = listWeekDayDictionary.get("Tuesday")
            for k, v in Tuesdaylist.items():
                TuesdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (TuesdayCode))
        if i == 3:
            Wednesdaylist = listWeekDayDictionary.get("Wednesday")
            for k, v in Wednesdaylist.items():
                WednesdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (WednesdayCode))
        if i == 4:
            Thursdaylist = listWeekDayDictionary.get("Thursday")
            for k, v in Thursdaylist.items():
                ThursdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ThursdayCode))
        if i == 5:
            Fridaylist = listWeekDayDictionary.get("Friday")
            for k, v in Fridaylist.items():
                FridayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (FridayCode))
        if i == 6:
            Saturdaylist = listWeekDayDictionary.get("Saturday")
            for k, v in Saturdaylist.items():
                SaturdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (SaturdayCode))

# List 2 function to place list and then transfer answer to textbox, for Month choice
def get_selDummyTwoMonth():
    for i in List2.curselection():
        if i == 0:
            Januarylist = listMonthDictionary.get("January")
            for k, v in Januarylist.items():
                JanuaryCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JanuaryCode))
        if i == 1:
            Februarylist = listMonthDictionary.get("February")
            for k, v in Februarylist.items():
                FebruaryCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (FebruaryCode))
        if i == 2:
            Marchlist = listMonthDictionary.get("March")
            for k, v in Marchlist.items():
                MarchCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (MarchCode))
        if i == 3:
            Aprillist = listMonthDictionary.get("April")
            for k, v in Aprillist.items():
                AprilCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (AprilCode))
        if i == 4:
            Maylist = listMonthDictionary.get("May")
            for k, v in Maylist.items():
                MayCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (MayCode))
        if i == 5:
            Junelist = listMonthDictionary.get("June")
            for k, v in Junelist.items():
                JuneCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JuneCode))
        if i == 6:
            Julylist = listMonthDictionary.get("July")
            for k, v in Julylist.items():
                JulyCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JulyCode))
        if i == 7:
            Augustlist = listMonthDictionary.get("August")
            for k, v in Augustlist.items():
                AugustCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (AugustCode))
        if i == 8:
            Septemberlist = listMonthDictionary.get("September")
            for k, v in Septemberlist.items():
                SeptemberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (SeptemberCode))
        if i == 9:
            Octoberlist = listMonthDictionary.get("October")
            for k, v in Octoberlist.items():
                OctoberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (OctoberCode))
        if i == 10:
            Novemberlist = listMonthDictionary.get("November")
            for k, v in Novemberlist.items():
                NovemberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (NovemberCode))
        if i == 11:
            Decemberlist = listMonthDictionary.get("December")
            for k, v in Decemberlist.items():
                DecemberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (DecemberCode))
        if i == 12:
            Unlistedlist = listMonthDictionary.get("Unlisted")
            for k, v in Unlistedlist.items():
                UnlistedCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (UnlistedCode))



# the accuracy score method
def writeAccuracy(buttonClicks):
    if buttonClicks == 1:
        # Creating pop up window for dataset
        # reference: https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        win = tk.Toplevel()
        win.wm_title("White Ball 5 prediction page")

        popUpLabel = tk.Label(win,
                              text="Please see the accuracy percentage of the WhiteBall 5 Prediction algorithm below:\n")
        popUpLabel.grid(row=0, column=0)

        # Display Boxes for Results
        dataSetDisplay = ScrolledText(win, height=2, width=30)
        dataSetDisplay.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        # decimal form of predication accuracy percentage
        # dataSetDisplay.insert(4.0, str(accuracy_score(y_test, y_pred)))
        # percentage form of predication accuracy percentage
        acc = accuracy_score(y_test, y_pred)
        dataSetDisplay.insert(4.0, str("%.0f%%" % (acc * 100)))

    else:
        mbox.showerror("Error", "Returning to the main menu.")
        import mainPage


# creating a method so that the user can tab from one dummy number textbox to the next, instead of clicking
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return ("break")


# ---- Creating functions to run the main prediction program ----------------------------------------------------------

# the dummy number value method, for tab 3 input entries from the user
def dummyValues():
    while True:
        try:
            # Getting user-input for dummy numbers to be used in the algorithm
            # Dummy User Choice 1 -
            dummyTextOne = dummyNumberOne.get('1.0', tk.END)
            # Dummy User Choice 2 -
            dummyTextTwo = dummyNumberTwo.get('1.0', tk.END)
            # Dummy User Choice 3 -
            dummyTextThree = dummyNumberThree.get('1.0', tk.END)
            # Dummy User Choice 4 -
            dummyTextFour = dummyNumberFour.get('1.0', tk.END)


            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = float(dummyTextOne)
            dummyValues.dummyTextTwo = float(dummyTextTwo)
            dummyValues.dummyTextThree = float(dummyTextThree)
            dummyValues.dummyTextFour = float(dummyTextFour)


        # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
        # is made, the program brings the user back to the main menu by calling the Predictions class and menu
        # method
        except ValueError:
            # error message variable
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            # breaking the loop to avoid infinite loop
            break


# the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
# is called at the beginning of the finalPrediction method (for the user-input variables)
def finalPrediction():
    while True:
        try:
            # calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            root_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            break


# Textbox clear/delete function
def clear_display_result():
    root_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)

    # when boxes are cleared, bringing the option focus for the user back to the initial textbox
    dummyNumberOne.focus()


def mainMenu():
    while True:
        try:

            # Creating a messagebox for when the user clicks to exit the program, with exception prevention
            if mbox.askokcancel("Quit", "Do you want to quit?"):
                # root.destroy()
                root.protocol("WM_DELETE_WINDOW", mainMenu)
                root.destroy()
                import mainPage


        except ValueError:
            import mainPage
        else:
            break


def exitProgram():
    exit()


def flush(self):
    pass


# ----- Creating Tkinter Setup (root) for GUI #-----

root = tk.Tk()
root.title('White Ball 5 Prediction Page')
root.geometry("800x850")

# Creating a scrollbar on the application, in the root, canvas, and then frame
# Reference: https://www.youtube.com/watch?v=0WafQCaok6g
# Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create a Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add a Scrollbar to the Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure the Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
# Create another frame inside the Canvas
second_frame=Frame(my_canvas)
# Add that new frame to a window in the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


# ------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

# This option will eventually be a dropbox option, rather than fill in the blanks
l3 = Label(second_frame, text='Please enter choices in the cells below, and then click the Prediction button ' +
                       'to see your prediction results:', padx=5, pady=5)
l3.grid(row=0, column=0)

# Label year
labelWeek = Label(second_frame, text="Choose and submit the projected weekday:")
labelWeek.grid(row=2, column=0)

labelMonth = Label(second_frame, text="Choose and submit the projected month:")
labelMonth.grid(row=6, column=0)

labelYear = Label(second_frame, text="Enter the day of the month:")
labelYear.grid(row=10, column=0)

labelGrossPSD = Label(second_frame, text="Enter the year projected event in format 'YYYY':")
labelGrossPSD.grid(row=12, column=0)



predictionLabel = Label(second_frame, text="Prediction results White Ball 5:")
predictionLabel.grid(row=20, column=0)
# --------------------- Dummy 1 Listbox and Textbox White Ball 5-------------------------------------------------------
# Listbox of Dummy Numbers
dummyOneListBox = Listbox(second_frame)  # height=1, width=50, yscrollcommand=TRUE)
dummyOneListBox.bind("<Tab>", focus_next_widget)  # for user to tab between listboxes/textboxes
dummyOneListBox.grid(row=3, column=0, padx=5, pady=5, ipadx=3, ipady=0)

List1 = Listbox(dummyOneListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listWeekDayDictionary:
    List1.insert(END, '{}: {}'.format(key, listWeekDayDictionary[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = Text(second_frame, height=1, width=25)
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

# --------------------- Dummy 2 Listbox and Textbox  (Attack Target) ----------------------------------------------------
# Listbox of Dummy Numbers
dummyTwoListBox = Listbox(second_frame, height=2, width=50, yscrollcommand=SCROLL)
dummyTwoListBox.bind("<Tab>", focus_next_widget)  # for user to tab between listboxes/textboxes
dummyTwoListBox.grid(row=7, column=0, columnspan=1, padx=5, pady=5, ipadx=250, ipady=0)

List2 = Listbox(dummyTwoListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listMonthDictionary:
    List2.insert(END, '{}: {}'.format(key, listMonthDictionary[key]))
    List2.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberTwo = Text(second_frame, height=1, width=25)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=9, column=0, columnspan=1, padx=5, pady=5)

# --------------------- Dummy 3 Listbox and Textbox Attack Month--------------------------------------------------------

dummyNumberThree = Text(second_frame, height=2, width=50)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=11, column=0, columnspan=1, padx=5, pady=5)

# --------------------- Dummy 4 Listbox and Textbox Attack Year----------------------------------------------------------

dummyNumberFour = Text(second_frame, height=2, width=50)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=13, column=0, columnspan=1, padx=5, pady=5)



# -------Tkinter Buttons------------------------------------------------------------------------------------------------

# Tab 2
# Accuracy Button
AccuracyButton = Button(second_frame, text='Prediction Accuracy', command=lambda: writeAccuracy(1), width=20, bg='purple',
                        fg='#fff')
AccuracyButton.grid(row=19, column=0, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

# List 1 White Ball 5  choice buttons
DummyOneButtonSubmit = Button(second_frame, text="Submit Day of Week", command=lambda: get_WeekDayList(), width=20,
                              bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=4, column=0, padx=15, pady=15)

# List 2 White Ball 5  choice button
DummyTwoButtonSubmit = Button(second_frame, text="Submit Month", command=lambda: get_selDummyTwoMonth(), width=20, bg='purple',
                              fg='#fff')
DummyTwoButtonSubmit.grid(row=8, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(second_frame, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='blue', fg='#fff')
PredictionButton.grid(row=18, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(second_frame, text='Clear results and start over', command=clear_display_result, width=25,
                             bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=22, column=0, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(second_frame, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=23, column=0, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(second_frame, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=24, column=0, padx=5, pady=5)

# ------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results

# Prediction results window in tab 3
root_display = Text(second_frame, height=1)
root_display.grid(row=21, column=0, columnspan=1, padx=5, pady=5)

# --- start program ---

root.mainloop()