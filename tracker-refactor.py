# application imports
from src.helpers import *
from src.models.base.Raid import Raid
from src.models.base.Drop import Drop

# imports
import json
import tkinter as tk
from tkinter import IntVar, StringVar, PhotoImage, ttk
from ttkthemes import ThemedStyle

# debug imports?
from tkinter import messagebox

#save data to json
def saveData():
    #fixed schema def
    drop = {}
    drop['settings'] = {
        'resourceTab':  tabControl.select(),
        'goldTab':  tabControlBar.select(),
        'sandTab':  tabControlSand.select(),
        'settingsTab':  tabControlSettings.select(),
        'theme': theme.get()
    }
    drop['pbhl'] = {
        'raid': pbhlraidCount.get(),
        'noblue': noblueCount.get(),
        'coronaring': pbhlcoronaringCount.get(),
        'lineagering': pbhllineageringCount.get(),
        'intricacyring': pbhlintricacyringCount.get(),
        'goldbar': pbhlgoldbarCount.get(),
        'hornbefore':pbhlHornLastBarEntry.get(),
        'hornafter':pbhlCurrentHornEntry.get()
    }
    with open('data.json', 'w') as file:
        json.dump(drop,file, indent=4)

#pbhl left mouse button
def pbhlCallBack(item):
    #messagebox.showinfo(item)
    #print(item)

    pbhlraidCount.set(pbhlraidCount.get()+1)

    if(item=="noblue"):
        noblueCount.set(noblueCount.get()+1)
    elif(item == "coronaring"):
        pbhlcoronaringCount.set(pbhlcoronaringCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get()+1)
    elif(item == "lineagering"):
        pbhllineageringCount.set(pbhllineageringCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get() + 1)
    elif(item == "intricacyring"):
        pbhlintricacyringCount.set(pbhlintricacyringCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get() + 1)
    elif(item == "goldbar"):
        pbhlgoldbarCount.set(pbhlgoldbarCount.get()+1)
        pbhlblueCount.set(pbhlblueCount.get() + 1)

    pbhlbluePercent.set(value=str(round(pbhlblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
    pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

    if pbhlblueCount.get() == 0:
        pbhlcoronaringPercentage.set("0.0%")
        pbhllineageringPercentage.set("0.0%")
        pbhlintricacyringPercentage.set("0.0%")
        pbhlgoldbarPercentage.set("0.0%")
    else:
        pbhlcoronaringPercentage.set(str(round(pbhlcoronaringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhllineageringPercentage.set(str(round(pbhllineageringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlintricacyringPercentage.set(str(round(pbhlintricacyringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlgoldbarPercentage.set(str(round(pbhlgoldbarCount.get()/pbhlblueCount.get()*100,2)) + "%")

    saveData()

#pbhl back action button
def pbhlTakeBack(item):
    #messagebox.showinfo(item)
    #print(item)


    if(item=="noblue"):
        if noblueCount.get() == 0:
            return
        else:
            noblueCount.set(noblueCount.get()-1)
    elif(item == "coronaring"):
        if pbhlcoronaringCount.get() == 0:
            return
        else:
            pbhlcoronaringCount.set(pbhlcoronaringCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)
    elif(item == "lineagering"):
        if pbhllineageringCount.get() == 0:
            return
        else:
            pbhllineageringCount.set(pbhllineageringCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)
    elif(item == "intricacyring"):
        if pbhlintricacyringCount.get() == 0:
            return
        else:
            pbhlintricacyringCount.set(pbhlintricacyringCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)
    elif(item == "goldbar"):
        if pbhlgoldbarCount.get() == 0:
            return
        else:
            pbhlgoldbarCount.set(pbhlgoldbarCount.get()-1)
            pbhlblueCount.set(pbhlblueCount.get() - 1)

    pbhlraidCount.set(pbhlraidCount.get() - 1)
    #pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

    if pbhlraidCount.get() == 0 or pbhlblueCount.get() == 0:
        nobluePercentage.set("0.0%")
        pbhlcoronaringPercentage.set("0.0%")
        pbhllineageringPercentage.set("0.0%")
        pbhlintricacyringPercentage.set("0.0%")
        pbhlgoldbarPercentage.set("0.0%")
        pbhlbluePercent.set("0.0%")
        pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
    else:
        pbhlbluePercent.set(value=str(round(pbhlblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
        pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
        nobluePercentage.set(str(round(noblueCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlcoronaringPercentage.set(str(round(pbhlcoronaringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhllineageringPercentage.set(str(round(pbhllineageringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlintricacyringPercentage.set(str(round(pbhlintricacyringCount.get()/pbhlblueCount.get()*100,2)) + "%")
        pbhlgoldbarPercentage.set(str(round(pbhlgoldbarCount.get()/pbhlblueCount.get()*100,2)) + "%")

    saveData()

# PBHL reset
def pbhlresetCount():
    messageboxChoice = tk.messagebox.askquestion(title="Reset", message="Do you want to reset this tab?")

    if messageboxChoice == 'yes':
        pbhlraidCount.set(0)
        noblueCount.set(0)
        pbhlcoronaringCount.set(0)
        pbhllineageringCount.set(0)
        pbhlintricacyringCount.set(0)
        pbhlgoldbarCount.set(0)
        pbhlblueCount.set(0)

        if pbhlraidCount.get() == 0:
            nobluePercentage.set("0.0%")
            pbhlcoronaringPercentage.set("0.0%")
            pbhllineageringPercentage.set("0.0%")
            pbhlintricacyringPercentage.set("0.0%")
            pbhlgoldbarPercentage.set("0.0%")
            pbhlbluePercent.set("0.0%")
        else:
            pbhlbluePercent.set(value=str(round(pbhlblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
            nobluePercentage.set(str(round(noblueCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlcoronaringPercentage.set(str(round(pbhlcoronaringCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhllineageringPercentage.set(str(round(pbhllineageringCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlintricacyringPercentage.set(str(round(pbhlintricacyringCount.get() / pbhlraidCount.get() * 100, 2)) + "%")
            pbhlgoldbarPercentage.set(str(round(pbhlgoldbarCount.get() / pbhlraidCount.get() * 100, 2)) + "%")

        pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))
    else:
        return
    saveData()

def themeToggle(currentTheme):
    match currentTheme:
        case "black":
            themeSetting("arc")
            settingsThemeToggleButton.configure(textvariable=settingsThemeStringLight)
        case "clearlook":
            themeSetting("black")
            settingsThemeToggleButton.configure(textvariable=settingsThemeStringDark)
        case _:
            themeSetting("black")
            settingsThemeToggleButton.configure(textvariable=settingsThemeStringDark)

def themeSetting(themeColor):
    theme.set(themeColor)
    style.set_theme(theme.get())
    saveData()

def hornsDifference(e):
    if pbhlHornLastBarEntry.get() == "" and pbhlCurrentHornEntry.get() == "":
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + "0")
    elif pbhlHornLastBarEntry.get() == "":
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + str(abs(int(pbhlCurrentHornEntry.get()))))
    elif pbhlCurrentHornEntry.get() == "":
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + str(abs(int(pbhlHornLastBarEntry.get()))))
    else:
        pbhlHornsSinceLabel.set("Horns since:" + "\n" + str(abs(int(pbhlHornLastBarEntry.get()) - int(pbhlCurrentHornEntry.get()))))

    saveData()

# load data from json
with open('data.json') as file:
    drop = json.load(file)

# base GUI init
root = tk.Tk()
root.title("Drop Tracker")
root.iconphoto(True, PhotoImage(file=imgSrc("peek.png")))
root.attributes('-topmost', True)

def callBack(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False
vcmd = root.register(callBack)

# theme init
# if user is using old data.json, default is now dark theme 
try:
    drop['settings']['theme']
except KeyError:
    drop['settings']['theme'] = 'black';
    theme = StringVar(value=drop['settings']['theme'])
else:
    theme = StringVar(value=drop['settings']['theme'])
style = ThemedStyle(root)
style.set_theme(theme.get() or "arc")

#tab definition
tabControl = ttk.Notebook(root)

barTab = ttk.Frame(tabControl)
sandTab = ttk.Frame(tabControl)
settingsTab = ttk.Frame(tabControl)

tabControlBar = ttk.Notebook(barTab)
tabControlSand = ttk.Notebook(sandTab)
tabControlSettings = ttk.Notebook(settingsTab)

barImg = ImageTk.PhotoImage((Image.open(imgSrc("goldbar.png"))).resize((20,20),Image.LANCZOS))
sandImg = ImageTk.PhotoImage((Image.open(imgSrc("eternitysand.png"))).resize((20,20),Image.LANCZOS))
settingsImg = ImageTk.PhotoImage((Image.open(imgSrc("settingscog.png"))).resize((20,20),Image.LANCZOS))

tabControl.add(barTab, text="Bar Raids", image=barImg, compound="left")
tabControl.add(sandTab, text="Sand Raids", image=sandImg, compound="left")
tabControl.add(settingsTab, text='Settings', image=settingsImg, compound="left")
tabControl.pack(expand=1, fill="both")
tabControlBar.pack(expand=1, fill="both")

# bar tab 
pbhlTab = ttk.Frame(tabControlBar)
gohlTab = ttk.Frame(tabControlBar)
akashaTab = ttk.Frame(tabControlBar)
ubahaTab = ttk.Frame(tabControlBar)
tabControlBar.add(pbhlTab, text='PBHL')
tabControlBar.add(gohlTab, text='GOHL')
tabControlBar.add(akashaTab, text='Akasha')
tabControlBar.add(ubahaTab, text='UBHL')

# sand tab
revansTab = ttk.Frame(tabControlSand)
subahaTab = ttk.Frame(tabControlSand)
hexaTab = ttk.Frame(tabControlSand)
suluciTab = ttk.Frame(tabControlSand)
tabControlSand.add(revansTab, text='Revans')
tabControlSand.add(subahaTab, text='Subaha')
tabControlSand.add(hexaTab, text='Hexa')
tabControlSand.add(suluciTab, text='Luci 000')

# settings tab
settingsThemeString = StringVar(value="Change Theme")
settingsThemeStringDark = StringVar(value="Swap to Light Theme")
settingsThemeStringLight = StringVar(value="Swap to Dark Theme")

settingsThemeTitle = ttk.Label(settingsTab, textvariable=settingsThemeString, justify="left")
settingsThemeTitle.grid(column=0, columnspan=2, row=5, sticky= tk.NW)

settingsThemeToggleButton = ttk.Button(settingsTab)
match theme.get(): 
    case "black":
        settingsThemeToggleButton.configure(textvariable=settingsThemeStringDark)
    case "arc":
        settingsThemeToggleButton.configure(textvariable=settingsThemeStringLight)

settingsThemeToggleButton.bind('<Button-1>', lambda event: themeToggle(theme.get()))
settingsThemeToggleButton.grid(column=0, columnspan=2, row=6, sticky= tk.NW)

# logic gets moved to classes
pbhlRaid = Raid("pbhl")
pbhlRaid.image = imgSrc("pbhlCount.png", raid="pbhl")
pbhlRaid.drops = dict(
    noBlueChest = Drop("NoBlueChest", imgSrc("pbhlNobluechest.png", raid="pbhl")),
    blueChest = Drop("BlueChest", imgSrc("pbhlNobluechest.png", raid="pbhl")),
    coronationRing = Drop("CoronationRing", imgSrc("pbhlNobluechest.png", raid="pbhl")),
    lineageRing = Drop("LineageRing", imgSrc("pbhlNobluechest.png", raid="pbhl")),
    intricacyRing = Drop("IntricacyRing", imgSrc("pbhlNobluechest.png", raid="pbhl")),
    horn = Drop('Horn', imgSrc("pbhlNobluechest.png", raid="pbhl")),
    goldBar = Drop("GoldBar", imgSrc("pbhlNobluechest.png", raid="pbhl"))
)

print(pbhlRaid.drops.get('noBlueChest').image)

# Tab PBHL
pbhlraidCount = IntVar(value=drop['pbhl']['raid'])
noblueCount = IntVar(value=drop['pbhl']['noblue'])
pbhlcoronaringCount = IntVar(value=drop['pbhl']['coronaring'])
pbhllineageringCount = IntVar(value=drop['pbhl']['lineagering'])
pbhlintricacyringCount = IntVar(value=drop['pbhl']['intricacyring'])
pbhlgoldbarCount = IntVar(value=drop['pbhl']['goldbar'])
pbhlblueCount = IntVar(value=pbhlraidCount.get()-noblueCount.get())
pbhlbluePercent = StringVar(value="Dokkan")
pbhlblueText = StringVar(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

# PBHL
if pbhlblueCount.get() == 0:
    nobluePercentage = StringVar(value="0.0%")
    pbhlcoronaringPercentage = StringVar(value="0.0%")
    pbhllineageringPercentage = StringVar(value="0.0%")
    pbhlintricacyringPercentage = StringVar(value="0.0%")
    pbhlgoldbarPercentage = StringVar(value="0.0%")
    pbhlbluePercent = StringVar(value="0.0%")
else:
    nobluePercentage = StringVar(value=str(round(noblueCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlcoronaringPercentage = StringVar(value=str(round(pbhlcoronaringCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhllineageringPercentage = StringVar(value=str(round(pbhllineageringCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlintricacyringPercentage = StringVar(value=str(round(pbhlintricacyringCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlgoldbarPercentage = StringVar(value=str(round(pbhlgoldbarCount.get()/pbhlblueCount.get()*100,2)) + "%")
    pbhlbluePercent = StringVar(value=str(round(pbhlblueCount.get()/pbhlraidCount.get()*100,2)) + "%")

pbhlblueText.set(value="Total: " + str(pbhlblueCount.get()) + "\n" + "Drop Rate: " + str(pbhlbluePercent.get()))

# GUI Layout / render

# total pbhl raids
pbhlImg = tk.PhotoImage(file=imgSrc("pbhlCount.png", raid="pbhl"))
pbhlImg = resizeImage(pbhlImg, 50, 50)
pbhlLabel = ttk.Label(pbhlTab, image=pbhlImg).grid(column=0,row=1)
pbhlCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlraidCount).grid(column=0, row=2)

#umikin is stinky, maki too and udder and munching

# no blue chest
noblueImg = tk.PhotoImage(file=imgSrc("pbhlNobluechest.png", raid="pbhl"))
noblueImg = resizeImage(noblueImg, 50, 50)
# hollowkeyLabel = tttk.Label(akashaTab, text="Hollow key").grid(column=0,row=0)
noblueButton = ttk.Button(pbhlTab, image=noblueImg)
noblueButton.grid(column=1,row=1)
noblueCounterLabel = ttk.Label(pbhlTab, textvariable=noblueCount).grid(column=1,row=2)
#nobluePercentageLabel = ttk.Label(pbhlTab, textvariable=nobluePercentage).grid(column=1,row=3)
noblueButton.bind('<Button-1>', lambda event: pbhlCallBack("noblue"))
noblueButton.bind('<Button-2>', lambda event: pbhlTakeBack("noblue"))
noblueButton.bind('<Button-3>', lambda event: pbhlTakeBack("noblue"))

# pbhl corona ring
pbhlcoronaringImg = tk.PhotoImage(file=imgSrc("pbhlCoronationring.png", raid="pbhl"))
pbhlcoronaringImg = resizeImage(pbhlcoronaringImg, 50, 50)
# coronaringLabel = tttk.Label(akashaTab, text="Coronation Ring").grid(column=1,row=0)
pbhlcoronaringButton = ttk.Button(pbhlTab, image=pbhlcoronaringImg)
pbhlcoronaringButton.grid(column=2,row=1)
pbhlcoronaringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlcoronaringCount).grid(column=2,row=2)
pbhlcoronaringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlcoronaringPercentage).grid(column=2,row=3)
pbhlcoronaringButton.bind('<Button-1>', lambda event: pbhlCallBack("coronaring"))
pbhlcoronaringButton.bind('<Button-2>', lambda event: pbhlTakeBack("coronaring"))
pbhlcoronaringButton.bind('<Button-3>', lambda event: pbhlTakeBack("coronaring"))

# pbhl lineage ring
pbhllineageringImg = tk.PhotoImage(file=imgSrc("pbhlLineagering.png", raid="pbhl"))
pbhllineageringImg = resizeImage(pbhllineageringImg, 50, 50)
# lineageringLabel = tttk.Label(akashaTab, text="Lineage Ring").grid(column=2,row=0)
pbhllineageringButton = ttk.Button(pbhlTab, image=pbhllineageringImg)
pbhllineageringButton.grid(column=3,row=1)
pbhllineageringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhllineageringCount).grid(column=3,row=2)
pbhllineageringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhllineageringPercentage).grid(column=3,row=3)
pbhllineageringButton.bind('<Button-1>', lambda event: pbhlCallBack("lineagering"))
pbhllineageringButton.bind('<Button-2>', lambda event: pbhlTakeBack("lineagering"))
pbhllineageringButton.bind('<Button-3>', lambda event: pbhlTakeBack("lineagering"))

# pbhl intricacy ring
pbhlintricacyringImg = tk.PhotoImage(file=imgSrc("pbhlIntricacyring.png", raid="pbhl"))
pbhlintricacyringImg = resizeImage(pbhlintricacyringImg, 50, 50)
# intricacyringLabel = tttk.Label(akashaTab, text="Intricacy Ring").grid(column=3,row=0)
# intricacyringButton = ttk.Button(akashaTab, image=intricacyringImg, command=lambda:buttonCallBack("intricacyring")).grid(column=4,row=1)
pbhlintricacyringButton = ttk.Button(pbhlTab, image=pbhlintricacyringImg)
pbhlintricacyringButton.grid(column=4,row=1)
pbhlintricacyringCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlintricacyringCount).grid(column=4,row=2)
pbhlintricacyringPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlintricacyringPercentage).grid(column=4,row=3)
pbhlintricacyringButton.bind('<Button-1>', lambda event: pbhlCallBack("intricacyring"))
pbhlintricacyringButton.bind('<Button-2>', lambda event: pbhlTakeBack("intricacyring"))
pbhlintricacyringButton.bind('<Button-3>', lambda event: pbhlTakeBack("intricacyring"))

# pbhl gold bar
pbhlgoldbarImg = tk.PhotoImage(file=imgSrc("pbhlGoldbar.png", raid="pbhl"))
pbhlgoldbarImg = resizeImage(pbhlgoldbarImg, 50, 50)
# goldbarLabel = tttk.Label(akashaTab, text="Gold Bar").grid(column=4,row=0)
pbhlgoldbarButton = ttk.Button(pbhlTab, image=pbhlgoldbarImg)
pbhlgoldbarButton.grid(column=5,row=1)
pbhlgoldbarCounterLabel = ttk.Label(pbhlTab, textvariable=pbhlgoldbarCount).grid(column=5,row=2)
pbhlgoldbarPercentageLabel = ttk.Label(pbhlTab, textvariable=pbhlgoldbarPercentage).grid(column=5,row=3)
pbhlgoldbarButton.bind('<Button-1>', lambda event: pbhlCallBack("goldbar"))
pbhlgoldbarButton.bind('<Button-2>', lambda event: pbhlTakeBack("goldbar"))
pbhlgoldbarButton.bind('<Button-3>', lambda event: pbhlTakeBack("goldbar"))

# pbhl reset button
pbhlresetButton = ttk.Button(pbhlTab, text="Reset", command=lambda:pbhlresetCount(), width=12).grid(column=5, row=5)

# pbhl blue chest count/percentage
pbhlblueImg = tk.PhotoImage(file=imgSrc("pbhlBluechest.png", raid="pbhl"))
pbhlblueImg = resizeImage(pbhlblueImg, 25, 25)
pbhlblueLabel = ttk.Label(pbhlTab, image=pbhlblueImg)
pbhlblueLabel.grid(column=0,row=4, sticky= tk.W)

pbhlblueTextLabel = ttk.Label(pbhlTab, textvariable=pbhlblueText, justify="left")
pbhlblueTextLabel.grid(column=0, columnspan=2, row=5, sticky=tk.W)

# NEW STUFF

#pbhlHornsDifference = StringVar(value="Dokkan")

if drop['pbhl']['hornbefore'] == "" and drop['pbhl']['hornafter'] =="":
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + "0")
elif drop['pbhl']['hornbefore'] == "":
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + str(abs(int(drop['pbhl']['hornafter']))))
elif drop['pbhl']['hornafter'] == "":
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + str(abs(int(drop['pbhl']['hornbefore']))))
else:
    pbhlHornsSinceLabel = StringVar(value="Horns since:" + "\n" + str(abs(int(drop['pbhl']['hornbefore'])-int(drop['pbhl']['hornafter']))))

# Horn Count
pbhlhornImg = tk.PhotoImage(file=imgSrc("pbhlhorn.png", raid="pbhl"))
pbhlhornImg = resizeImage(pbhlhornImg, 25, 25)
pbhlhornLabel = ttk.Label(pbhlTab, image=pbhlhornImg)
pbhlhornLabel.grid(column=2, row=4, sticky= tk.W)

pbhlHornText = ttk.Label(pbhlTab, textvariable=pbhlHornsSinceLabel, justify="left")
pbhlHornText.grid(column=2, columnspan=2, row=5, sticky= tk.NW)

pbhlHornLastBarEntry = ttk.Entry(pbhlTab, width=15, validate='key', validatecommand=(vcmd, '%P'))
pbhlHornLastBarEntry.grid(column=3, columnspan=2, row=4)
pbhlHornLastBarEntry.insert(0, drop['pbhl']['hornbefore'])
pbhlHornLastBarEntry.bind("<KeyRelease>", hornsDifference)

pbhlCurrentHornEntry = ttk.Entry(pbhlTab, width=15, validate='key', validatecommand=(vcmd, '%P'))
pbhlCurrentHornEntry.grid(column=3, columnspan=2, row=5)
pbhlCurrentHornEntry.insert(0, drop['pbhl']['hornafter'])
pbhlCurrentHornEntry.bind("<KeyRelease>", hornsDifference)

# --- above logic gets moved to classes

match drop["settings"]["resourceTab"]: 
    case ".!notebook.!frame":
        tabControlBar.select(drop["settings"]["goldTab"])
    case ".!notebook.!frame2":
        tabControlSand.select(drop["settings"]["sandTab"])
    case ".!notebook.!frame3":
        tabControlSettings.select()
    case _:
        tabControlBar.select(drop["settings"]["goldTab"])

# program runs
root.mainloop()
