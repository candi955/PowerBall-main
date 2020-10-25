# Below is a code guide for the list functions (so that the Find/Replace tool can be used to replace 'Blank' with
# the desired list choice in the code on LocationTarget.py

# List function guide for placing dictionary into listbox and then transfer answer to textbox, for origin
# country/region choice

def get_selDummyOne():
    for i in List1.curselection():

        # Below is the part to be copied/pasted and Find/Replace used to put in proper entry
        if i == 0:
            BlankExamplelist = listOneDictionary.get("BlankExample")
            for k, v in BlankExamplelist.items():
                BlankExampleBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (BlankExampleBinary))

def get_selDummyTwo():
    for i in List2.curselection():

        # Below is the part to be copied/pasted and Find/Replace used to put in proper entry
        if i == 0:
            BlankExamplelist = listTwoDictionary.get("BlankExample")
            for k, v in BlankExamplelist.items():
                BlankExampleBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (BlankExampleBinary))