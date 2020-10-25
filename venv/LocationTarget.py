# Prediction of Attack Target page
# Support Vector Machine Cyber-Attack Prediction Program (SVM CAPP)__

# A GUI program (through Tkinter) utilizing SKLearn, SVM algorithm, to predict cybersecurity data via a Supervised
# dataset made of source and target data.  At this time the data is not made of completely real data, and the
# project is in the build/test phases.

# About Support Vector Machine (SVM)
# A support vector machine (SVM) is a type of Supervised machine learning classification algorithm.
# SVM differs from the other classification algorithms in the way that it chooses the decision boundary that maximizes
# the distance from the nearest data points of all the classes. An SVM doesn't merely find a decision boundary; it
# finds the most optimal decision boundary.
# (https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/)

# Utilizing SKlearn, pandas, numpy, xlrd APIs and also using a subclass of exception: import warnings (to prevent a
# Future Error warning from popping up; appears is due to possible future updates).

# Resources for original template build:
# https://www.youtube.com/watch?reload=9&v=bwZ3Qiuj3i8
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
# https://github.com/candi955/LottoProject   (my initial SVM project build and template for this project)

# Resources utilized for dataset creation:
# https://datacatalog.worldbank.org/dataset/world-development-indicators
# https://datacatalog.worldbank.org/dataset/global-economic-monitor
# https://csis-prod.s3.amazonaws.com/s3fs-public/190904_Significant_Cyber_Events_List.pdf
# https://www.csis.org/programs/technology-policy-program/significant-cyber-incidents



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

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#------------ListBox Country/Region/Code Dictionaries--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated Code
# reference: https://www.w3schools.com/python/python_dictionaries.asp

# List 1 (Origin country/region)
listOriginDictionary = {"Africa_China":{"Code": 6},
                "Australia":{"Code": 18},
                "Azerbaijan":{"Code": 23},
                "Brazil":{"Code": 27},
                "China":{"Code": 36},
                "China_North_Korea":{"Code": 39},
                "China_Pakistan":{"Code": 40},
                "China_Russia":{"Code": 41},
                "Czech_Republic":{"Code": 43},
                "Decentralized_International_Hacktivist_Group":{"Code": 45},
                "Eastern_Europe":{"Code": 48},
                "Egypt":{"Code": 49},
                "Gaza":{"Code": 66},
                "Gaza_Former_Soviet_Union_Lebanon":{"Code": 67},
                "Germany":{"Code": 69},
                "India":{"Code": 74},
                "Individuals":{"Code": 77},
                "Individuals_Ukraine":{"Code": 83},
                "Individuals_Unlisted":{"Code": 84},
                "International":{"Code": 89},
                "Iran":{"Code": 90},
                "Iran_North_Korea_Russia":{"Code": 92},
                "Iran_Russia":{"Code": 93},
                "Iran_Unlisted":{"Code": 95},
                "Iraq":{"Code": 96},
                "ISIS":{"Code": 99},
                "Israel":{"Code": 100},
                "Israel_USA":{"Code": 103},
                "Lebanon":{"Code": 110},
                "Mexico":{"Code": 115},
                "Middle_East":{"Code": 116},
                "Morocco":{"Code": 119},
                "Multiple":{"Code": 120},
                "Nation_State_Actor_Eastern_Europe":{"Code": 122},
                "Nation_State_Actor_Unlisted":{"Code": 123},
                "Non_State_Actor_Unlisted":{"Code": 127},
                "North_Korea":{"Code": 129},
                "Pakistan":{"Code": 132},
                "Russia":{"Code": 136},
                "Russia_Ukraine":{"Code": 137},
                "Russia_Ukraine_USA":{"Code": 138},
                "Saudi_Arabia":{"Code": 139},
                "South_Korea":{"Code": 145},
                "South_Korea_USA":{"Code": 146},
                "State_Sponsored_Actor_Unlisted":{"Code": 148},
                "Syria":{"Code": 151},
                "Taiwan":{"Code": 152},
                "Taiwan_USA":{"Code": 153},
                "Turkey":{"Code": 156},
                "UAE":{"Code": 157},
                "UK":{"Code": 158},
                "UK_USA":{"Code": 159},
                "Unlisted":{"Code": 1},
                "USA":{"Code": 162},
                "Vietnam":{"Code": 166},
                "Western_World":{"Code": 167},
                "Yemen":{"Code": 169}}

# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictOne = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# List 2 (Month of attack in Code numbers)

listMonthDictionary = {"January":{"code": 1}, # list option 0
                "February":{"Code": 2}, # list option 1
                "March":{"Code": 3}, # list option 2
                "April":{"Code": 4}, # list option 3
                "May":{"Code": 5}, # list option 4
                "June":{"Code": 6}, # list option 5
                "July":{"Code": 7}, # list option 6
                "August":{"Code": 8}, # list option 7
                "September":{"Code": 9}, # list option 8
                "October":{"Code": 10}, # list option 9
                "November":{"Code": 11}, # list option 10
                "December":{"Code": 12}, # list option 11
                "Unlisted":{"Code": 13}} # list option 12

# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
#pdDictTwo = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
cyberExcel = xlrd.open_workbook('TargetAttackPredictionDataWithCodes_CleanedUp_20Apr2020_2400pm.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
    cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

    # Removing target row from source dataset, with the -1, and removing source data from target data column, so that the -1
    # will only show the last column in the target data
    sources = cyberSheetData[:, :-1]
    target = cyberSheetData[:, len(cyberSheetData[0]) - 1]

    # Deleting header column from dataframe, both source and target data
    sourceNoHeader = np.delete(sources, (0), axis=0)
    targetNoHeader = np.delete(target, (0), axis=0)

    X = sourceNoHeader
    y = targetNoHeader


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

    model = svm.SVC(kernel='linear')
    model.fit(X_train, y_train.ravel())
    y_pred = model.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)


#-----Creating Tkinter Setup (root) for GUI----------------------------------------------------------------------------
root = tk.Tk()
root.title('SVM Prediction: Target Attack')
#root.geometry("1000x1000")
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')
# Tabs and Frames
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Attack Target Prediction')

tab_control.pack(expand=1, fill='both')

# Tkinter listbox with root functions
# reference: http://effbot.org/tkinterbook/listbox.htm
listbox = Listbox(root, selectmode=SINGLE)


#---Creating Tkinter functions----------------------------------------------------------------------------------------

# Creating listbox functions
# https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry
# https://www.youtube.com/watch?v=XJqUu85sMrA
# https://note.nkmk.me/en/python-tuple-list-unpack/
# List 1 function to place list and then transfer answer to textbox, for origin country/region choice
def get_selDummyOne():
    for i in List1.curselection():
        if i == 0:
            Africa_Chinalist = listOriginDictionary.get("Africa_China")
            for k, v in Africa_Chinalist.items():
                Africa_ChinaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Africa_ChinaCode))
        if i == 1:
            Australialist = listOriginDictionary.get("Australia")
            for k, v in Australialist.items():
                AustraliaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AustraliaCode))
        if i == 2:
            Azerbaijanlist = listOriginDictionary.get("Azerbaijan")
            for k, v in Azerbaijanlist.items():
                AzerbaijanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AzerbaijanCode))
        if i == 3:
            Brazillist = listOriginDictionary.get("Brazil")
            for k, v in Brazillist.items():
                BrazilCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (BrazilCode))
        if i == 4:
            Chinalist = listOriginDictionary.get("China")
            for k, v in Chinalist.items():
                ChinaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ChinaCode))
        if i == 5:
            China_North_Korealist = listOriginDictionary.get("China_North_Korea")
            for k, v in China_North_Korealist.items():
                China_North_KoreaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_North_KoreaCode))
        if i == 6:
            China_Pakistanlist = listOriginDictionary.get("China_Pakistan")
            for k, v in China_Pakistanlist.items():
                China_PakistanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_PakistanCode))
        if i == 7:
            China_Russialist = listOriginDictionary.get("China_Russia")
            for k, v in China_Russialist.items():
                China_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_RussiaCode))
        if i == 8:
            Czech_Republiclist = listOriginDictionary.get("Czech_Republic")
            for k, v in Czech_Republiclist.items():
                Czech_RepublicCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Czech_RepublicCode))
        if i == 9:
            Decentralized_International_Hacktivist_Grouplist = listOriginDictionary.get("Decentralized_International_Hacktivist_Group")
            for k, v in Decentralized_International_Hacktivist_Grouplist.items():
                Decentralized_International_Hacktivist_GroupCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Decentralized_International_Hacktivist_GroupCode))
        if i == 10:
            Eastern_Europelist = listOriginDictionary.get("Eastern_Europe")
            for k, v in Eastern_Europelist.items():
                Eastern_EuropeCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Eastern_EuropeCode))
        if i == 11:
            Egyptlist = listOriginDictionary.get("Egypt")
            for k, v in Egyptlist.items():
                EgyptCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (EgyptCode))
        if i == 12:
            Gazalist = listOriginDictionary.get("Gaza")
            for k, v in Gazalist.items():
                GazaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (GazaCode))
        if i == 13:
            Gaza_Former_Soviet_Union_Lebanonlist = listOriginDictionary.get("Gaza_Former_Soviet_Union_Lebanon")
            for k, v in Gaza_Former_Soviet_Union_Lebanonlist.items():
                Gaza_Former_Soviet_Union_LebanonCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Gaza_Former_Soviet_Union_LebanonCode))
        if i == 14:
            Germanylist = listOriginDictionary.get("Germany")
            for k, v in Germanylist.items():
                GermanyCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (GermanyCode))
        if i == 15:
            Indialist = listOriginDictionary.get("India")
            for k, v in Indialist.items():
                IndiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IndiaCode))
        if i == 16:
            Individualslist = listOriginDictionary.get("Individuals")
            for k, v in Individualslist.items():
                IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IndividualsCode))
        if i == 17:
            Individuals_Ukrainelist = listOriginDictionary.get("Individuals_Ukraine")
            for k, v in Individuals_Ukrainelist.items():
                Individuals_UkraineCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_UkraineCode))
        if i == 18:
            Individuals_Unlistedlist = listOriginDictionary.get("Individuals_Unlisted")
            for k, v in Individuals_Unlistedlist.items():
                Individuals_UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_UnlistedCode))
        if i == 19:
            Internationallist = listOriginDictionary.get("International")
            for k, v in Internationallist.items():
                InternationalCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (InternationalCode))
        if i == 20:
            Iranlist = listOriginDictionary.get("Iran")
            for k, v in Iranlist.items():
                IranCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IranCode))
        if i == 21:
            Iran_North_Korea_Russialist = listOriginDictionary.get("Iran_North_Korea_Russia")
            for k, v in Iran_North_Korea_Russialist.items():
                Iran_North_Korea_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Iran_North_Korea_RussiaCode))

        if i == 22:
            Iran_Russialist = listOriginDictionary.get("Iran_Russia")
            for k, v in Iran_Russialist.items():
                Iran_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Iran_RussiaCode))
        if i == 23:
            Iran_Unlistedlist = listOriginDictionary.get("Iran_Unlisted")
            for k, v in Iran_Unlistedlist.items():
                Iran_UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Iran_UnlistedCode))
        if i == 24:
            Iraqlist = listOriginDictionary.get("Iraq")
            for k, v in Iraqlist.items():
                IraqCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IraqCode))
        if i == 25:
            ISISlist = listOriginDictionary.get("ISIS")
            for k, v in ISISlist.items():
                ISISCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ISISCode))
        if i == 26:
            Israellist = listOriginDictionary.get("Israel")
            for k, v in Israellist.items():
                IsraelCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IsraelCode))
        if i == 27:
            Israel_USAlist = listOriginDictionary.get("Israel_USA")
            for k, v in Israel_USAlist.items():
                Israel_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Israel_USACode))
        if i == 28:
            Lebanonlist = listOriginDictionary.get("Lebanon")
            for k, v in Lebanonlist.items():
                LebanonCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (LebanonCode))
        if i == 29:
            Mexicolist = listOriginDictionary.get("Mexico")
            for k, v in Mexicolist.items():
                MexicoCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (MexicoCode))
        if i == 30:
            Middle_Eastlist = listOriginDictionary.get("Middle_East")
            for k, v in Middle_Eastlist.items():
                Middle_EastCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Middle_EastCode))
        if i == 31:
            Moroccolist = listOriginDictionary.get("Morocco")
            for k, v in Moroccolist.items():
                MoroccoCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (MoroccoCode))
        if i == 32:
            Multiplelist = listOriginDictionary.get("Multiple")
            for k, v in Multiplelist.items():
                MultipleCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (MultipleCode))
        if i == 33:
            Nation_State_Actor_Eastern_Europelist = listOriginDictionary.get("Nation_State_Actor_Eastern_Europe")
            for k, v in Nation_State_Actor_Eastern_Europelist.items():
                Nation_State_Actor_Eastern_EuropeCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Nation_State_Actor_Eastern_EuropeCode))
        if i == 34:
            Nation_State_Actor_Unlistedlist = listOriginDictionary.get("Nation_State_Actor_Unlisted")
            for k, v in Nation_State_Actor_Unlistedlist.items():
                Nation_State_Actor_UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Nation_State_Actor_UnlistedCode))
        if i == 35:
            Non_State_Actor_Unlistedlist = listOriginDictionary.get("Non_State_Actor_Unlisted")
            for k, v in Non_State_Actor_Unlistedlist.items():
                Non_State_Actor_UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Non_State_Actor_UnlistedCode))
        if i == 36:
            North_Korealist = listOriginDictionary.get("North_Korea")
            for k, v in North_Korealist.items():
                North_KoreaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (North_KoreaCode))
        if i == 37:
            Pakistanlist = listOriginDictionary.get("Pakistan")
            for k, v in Pakistanlist.items():
                PakistanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (PakistanCode))
        if i == 38:
            Russialist = listOriginDictionary.get("Russia")
            for k, v in Russialist.items():
                RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (RussiaCode))
        if i == 39:
            Russia_Ukrainelist = listOriginDictionary.get("Russia_Ukraine")
            for k, v in Russia_Ukrainelist.items():
                Russia_UkraineCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Russia_UkraineCode))
        if i == 40:
            Russia_Ukraine_USAlist = listOriginDictionary.get("Russia_Ukraine_USA")
            for k, v in Russia_Ukraine_USAlist.items():
                Russia_Ukraine_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Russia_Ukraine_USACode))
        if i == 41:
            Saudi_Arabialist = listOriginDictionary.get("Saudi_Arabia")
            for k, v in Saudi_Arabialist.items():
                Saudi_ArabiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Saudi_ArabiaCode))
        if i == 42:
            South_Korealist = listOriginDictionary.get("South_Korea")
            for k, v in South_Korealist.items():
                South_KoreaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (South_KoreaCode))
        if i == 43:
            South_Korea_USAlist = listOriginDictionary.get("South_Korea_USA")
            for k, v in South_Korea_USAlist.items():
                South_Korea_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (South_Korea_USACode))
        if i == 44:
            State_Sponsored_Actor_Unlistedlist = listOriginDictionary.get("State_Sponsored_Actor_Unlisted")
            for k, v in State_Sponsored_Actor_Unlistedlist.items():
                State_Sponsored_Actor_UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (State_Sponsored_Actor_UnlistedCode))
        if i == 45:
            Syrialist = listOriginDictionary.get("Syria")
            for k, v in Syrialist.items():
                SyriaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (SyriaCode))
        if i == 46:
            Taiwanlist = listOriginDictionary.get("Taiwan")
            for k, v in Taiwanlist.items():
                TaiwanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (TaiwanCode))
        if i == 47:
            Taiwan_USAlist = listOriginDictionary.get("Taiwan_USA")
            for k, v in Taiwan_USAlist.items():
                Taiwan_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Taiwan_USACode))
        if i == 48:
            Turkeylist = listOriginDictionary.get("Turkey")
            for k, v in Turkeylist.items():
                TurkeyCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (TurkeyCode))
        if i == 49:
            UAElist = listOriginDictionary.get("UAE")
            for k, v in UAElist.items():
                UAECode = "{}".format(v)
                dummyNumberOne.insert(1.0, (UAECode))
        if i == 50:
            UKlist = listOriginDictionary.get("UK")
            for k, v in UKlist.items():
                UKCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (UKCode))
        if i == 51:
            UK_USAlist = listOriginDictionary.get("UK_USA")
            for k, v in UK_USAlist.items():
                UK_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (UK_USACode))
        if i == 52:
            Unlistedlist = listOriginDictionary.get("Unlisted")
            for k, v in Unlistedlist.items():
                UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (UnlistedCode))
        if i == 53:
            USAlist = listOriginDictionary.get("USA")
            for k, v in USAlist.items():
                USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (USACode))
        if i == 54:
            Vietnamlist = listOriginDictionary.get("Vietnam")
            for k, v in Vietnamlist.items():
                VietnamCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (VietnamCode))
        if i == 55:
            Western_Worldlist = listOriginDictionary.get("Western_World")
            for k, v in Western_Worldlist.items():
                Western_WorldCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Western_WorldCode))
        if i == 56:
            Yemenlist = listOriginDictionary.get("Yemen")
            for k, v in Yemenlist.items():
                YemenCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (YemenCode))



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
        win.wm_title("Prediction accuracy of target prediction page")

        popUpLabel = tk.Label(win, text="Please see the accuracy percentage of the Target Prediction algorithm below:\n")
        popUpLabel.grid(row=0, column=0)


        # Display Boxes for Results
        dataSetDisplay = ScrolledText(win, height=2, width=30)
        dataSetDisplay.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        # decimal form of predication accuracy percentage
        #dataSetDisplay.insert(4.0, str(accuracy_score(y_test, y_pred)))
        # percentage form of predication accuracy percentage
        acc = accuracy_score(y_test, y_pred)
        dataSetDisplay.insert(4.0, str("%.0f%%"%(acc*100)))

    else:
        mbox.showerror("Error", "Returning to the main menu.")
        import mainPage

# creating a method so that the user can tab from one dummy number textbox to the next, instead of clicking
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

#---- Creating functions to run the main prediction program ----------------------------------------------------------

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
            # Dummy User Choice 5 -
            dummyTextFive = dummyNumberFive.get('1.0', tk.END)
            # Dummy 6 User Choice 6 -
            dummyTextSix = dummyNumberSix.get('1.0', tk.END)

            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = float(dummyTextOne)
            dummyValues.dummyTextTwo = float(dummyTextTwo)
            dummyValues.dummyTextThree = float(dummyTextThree)
            dummyValues.dummyTextFour = float(dummyTextFour)
            dummyValues.dummyTextFive = float(dummyTextFive)
            dummyValues.dummyTextSix = float(dummyTextSix)

        # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
        # is made, the program brings the user back to the main menu by calling the Predictions class and menu
        # method
        except ValueError:
            # error message variable
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        # Removed the if statements for exception due to planning to change this option to list-option

        else:
            # breaking the loop to avoid infinite loop
            break

# the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
# is called at the beginning of the finalPrediction method (for the user-input variables)
def finalPrediction():

    while True:
        try:
            #calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour, dummyValues.dummyTextFive, dummyValues.dummyTextSix])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            tab1_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            break

# Below is the creation of textbox entries; however am planning to make dummy number option a label option
def clear_display_result():
    tab1_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)
    dummyNumberFive.delete(1.0, END)
    dummyNumberSix.delete(1.0, END)
    # when boxes are cleared, bringing the option focus for the user back to the initial textbox
    dummyNumberOne.focus()

def mainMenu():

    while True:
        try:

            # Creating a messagebox for when the user clicks to exit the program, with exception prevention
            if mbox.askokcancel("Quit", "Do you want to quit?"):
                #root.destroy()
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

#------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

# This option will eventually be a dropbox option, rather than fill in the blanks
l3 = Label(tab1, text='Please enter six situational choices in the cells below, and then click the Prediction button'+
                      'to see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)

#--------------------- Dummy 1 Listbox and Textbox Attack Origin-------------------------------------------------------
#Listbox of Dummy Numbers
dummyOneListBox = Listbox(tab1) # height=1, width=50, yscrollcommand=TRUE)
dummyOneListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyOneListBox.grid(row=2, column=0, padx=5, pady=5, ipadx=250, ipady=0)

List1 = Listbox(dummyOneListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listOriginDictionary:
    List1.insert(END, '{}: {}'.format(key, listOriginDictionary[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = Text(tab1, height=2, width=50)
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 2 Listbox and Textbox  (Attack Target) ----------------------------------------------------
#Listbox of Dummy Numbers
dummyTwoListBox = Listbox(tab1, height=2, width=50, yscrollcommand=SCROLL)
dummyTwoListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyTwoListBox.grid(row=4, column=0, columnspan=1, padx=5, pady=5, ipadx=250, ipady=0)

List2 = Listbox(dummyTwoListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listMonthDictionary:
    List2.insert(END, '{}: {}'.format(key, listMonthDictionary[key]))
    List2.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberTwo = Text(tab1, height=2, width=50)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 3 Listbox and Textbox Attack Month--------------------------------------------------------

dummyNumberThree = Text(tab1, height=2, width=50)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 4 Listbox and Textbox Attack Year----------------------------------------------------------

dummyNumberFour = Text(tab1, height=2, width=50)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 5 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberFive = Text(tab1, height=2, width=50)
dummyNumberFive.bind("<Tab>", focus_next_widget)
dummyNumberFive.grid(row=6, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 6 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberSix = Text(tab1, height=2, width=50)
dummyNumberSix.bind("<Tab>", focus_next_widget)
dummyNumberSix.grid(row=7, column=1, columnspan=1, padx=5, pady=5)

#-------Tkinter Buttons------------------------------------------------------------------------------------------------

# Tab 2
# Accuracy Button
AccuracyButton = Button(tab1, text='Prediction Accuracy', command=lambda:writeAccuracy(1), width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=0, column=1, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

DummyOneButtonSubmit = Button(tab1, text="Submit Attack Origin", command=lambda: get_selDummyOne(), width=20, bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=3, column=0, padx=15, pady=15)

# List 2 Origin country/region choice button

DummyTwoButtonSubmit = Button(tab1, text="Submit Month", command=lambda: get_selDummyTwoMonth(), width=20, bg='purple', fg='#fff')
DummyTwoButtonSubmit.grid(row=5, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab1, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='blue', fg='#fff')
PredictionButton.grid(row=6, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab1, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=1, column=1, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab1, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=0, column=0, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab1, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=8, column=0, padx=5, pady=5)

#------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results

# Prediction results window in tab 3
tab1_display = Text(tab1, height=1)
tab1_display.grid(row=7, column=0, columnspan=1, padx=5, pady=5)

# Keep window alive
mainloop()

# reference for making scroll tab