from Tkinter import *
from tkColorChooser import askcolor
from tkFileDialog import *
import tkMessageBox
import json
import signal
import sys

root = Tk()
v = IntVar()
v.set(0)
color = "GREEN"
rdbtncount = 1
colors = 0
workarea = 0
rdbtn = range(1,17)
label = range(1,17)
btns= range(0,256)
masterbtn = 0
cancelbtn = 0
btnsvari= range(0,256)
btnsvarj= range(0,256)
btnsvark= range(0,256)
btnsvarl= range(0,256)
recolorvar = 0
fromvari = 0
fromvarj = 0
fromvark = 0
fromvarl = 0
occuvar= range(0,256)
btnshovered= range(0,256)
netzbez1var = StringVar()
netzbez1var.set("2A02:0568:00")
netzbez2var = StringVar()
netzbez2var.set("00:: /")
netzbez3var = StringVar()
netzbez3var.set("32")
rdbtnstartaddr= range(1,17)
rdbtnnetmask= range(1,17)
infolabelvar = StringVar()
infolabelvar.set("welcome")
infolabelvarbuffer = infolabelvar.get()

# everything to be put into the menubar
class MyMenu:
    global root

    def __init__(self, master):
        # the menu itsself
        topmenu= Menu(master)
        # show it
        master.config(menu=topmenu)
        # a drop-down-menu under File
        fileMenu = Menu(topmenu, tearoff=1)
        topmenu.add_cascade(label="File", menu=fileMenu)
        # and one under help
        helpMenu = Menu(topmenu, tearoff=0)
        topmenu.add_cascade(label="Help", menu=helpMenu, state=DISABLED)
        
        # the content of the file menu
        fileMenu.add_command(label="load file", command=loadfile)
        fileMenu.add_command(label="save file", command=savefile)
        fileMenu.add_command(label="Quit", command=callback)

# thats it for the menubar


class IPGrid:
    def __init__(self, master):
        global colors
        global btns
        global masterbtn
        global cancelbtn
        global btnsvari
        global btnsvarj
        global btnsvark
        global btnsvarl
        global occuvar
        global v
        global infolabelvar
        i=0
        workarea = Frame(master)
        colors = Frame(workarea)
        colors.config(borderwidth=2, relief=RIDGE, width=30, height=30)
        bildframe = Frame(workarea)
        netzbezframe = Frame(bildframe)
        buttons = Frame(bildframe, border=1, relief=FLAT, bg="lightgray")
        counter = 0
        for i in range(0,4):
            ebene1frame = Frame(buttons, border=4, bg="lightblue1")
            if i > 1:
                rowvar = 1
            else:
                rowvar = 0
            if i == 1 or i == 3:
                colvar = 1
            else:
                colvar = 0
            ebene1frame.grid(row=rowvar, column=colvar, sticky=(N,E,W,S))
            ebene1frame.grid_columnconfigure(colvar, weight=1)
            ebene1frame.grid_rowconfigure(rowvar, weight=1)
            for j in range(0,4):
                ebene2frame = Frame(ebene1frame, border=3, bg="lightblue2")
                if j > 1:
                    rowvar = 1
                else:
                    rowvar = 0
                if j == 1 or j == 3:
                    colvar = 1
                else:
                    colvar = 0
                ebene2frame.grid(row=rowvar, column=colvar)
                ebene2frame.grid_columnconfigure(colvar, weight=1)
                ebene2frame.grid_rowconfigure(rowvar, weight=1)
                for k in range(0,4):
                    ebene3frame = Frame(ebene2frame, border=2, bg="lightblue4")
                    if k > 1:
                        rowvar = 1
                    else:
                        rowvar = 0
                    if k == 1 or k == 3:
                        colvar = 1
                    else:
                        colvar = 0
                    ebene3frame.grid(row=rowvar, column=colvar)
                    ebene3frame.grid_columnconfigure(colvar, weight=1)
                    ebene3frame.grid_rowconfigure(rowvar, weight=1)
                    for l in range(0,4):
                        btns[counter] = Button(ebene3frame,
                                               text=str.format("{0:02X}",counter),
                                                background="lightblue3",
                                                activebackground="lightblue3",
                                                bd=2,
                                                command=lambda li=counter: recolor(li))
                        if l > 1:
                            rowvar = 1
                        else:
                            rowvar = 0
                        if l == 1 or l == 3:
                            colvar = 1
                        else:
                            colvar = 0
                        btns[counter].grid(row=rowvar, column=colvar, sticky=(N,E,W,S), padx=1, pady=1)
                        btns[counter].grid_columnconfigure(colvar, weight=1)
                        btns[counter].grid_rowconfigure(rowvar, weight=1)
                        btns[counter].bind("<Enter>", lambda e,li=counter: hover(li))
                        btns[counter].bind("<Leave>", lambda e,li=counter: unhover(li))
                        ebene3frame.bind("<Enter>", lambda e,li=256: hover(li))
                        ebene3frame.bind("<Leave>", lambda e,li=256: unhover(li))
                        ebene2frame.bind("<Enter>", lambda e,li=256: hover(li))
                        ebene2frame.bind("<Leave>", lambda e,li=256: unhover(li))
                        ebene1frame.bind("<Enter>", lambda e,li=256: hover(li))
                        ebene1frame.bind("<Leave>", lambda e,li=256: unhover(li))
                        btnsvari[counter]=i
                        btnsvarj[counter]=j
                        btnsvark[counter]=k
                        btnsvarl[counter]=l
                        occuvar[counter]=0
                        counter = counter + 1

        bildframe.pack(expand=0, fill="x", side=RIGHT)
        colors.pack(expand=0, fill=BOTH, side=LEFT)
        buttons.pack(expand=1, fill=BOTH, side=BOTTOM)
        workarea.pack(expand=1, fill=BOTH, side=BOTTOM)
        Button(colors,
               text="delete subnet",
               command=delete).pack(anchor=W)
        cancelbtn = Button(colors,
                           text="cancel",
                           command=cancel).pack(anchor=W)
        Button(colors,
               text='select color',
               command=getcolor).pack(anchor=W)
        masterbtn = Button(colors,
                           text='create new button',
                           bg=color,
                           activebackground=color,
                           command=newbutton)
        masterbtn.pack(anchor=W,expand=0)
        infolabel = Label(colors,
                          textvariable=infolabelvar,
                          justify=LEFT,
                          wraplength=135)
        infolabel.pack(anchor=S,expand=1, side=BOTTOM)
        netzbezframe.pack(side=TOP)
        netzbez1 = Label(netzbezframe,
                        textvariable=netzbez1var).pack(side=LEFT)
        netzbez2 = Label(netzbezframe,
                        textvariable=netzbez2var).pack(side=LEFT)
        netzbez3 = Label(netzbezframe,
                        textvariable=netzbez3var).pack(side=LEFT)
        master.bind("<Escape>", cancel)
        master.bind("<o>", loadfile)
        master.bind("<s>", savefile)
        master.bind("<d>", delete)
        master.bind("<n>", newbutton)

def loadfile(event=None):
    global btns
    global occuvar
    global rdbtncount
    global rdbtn
    global label
    global netzbez1var
    global netzbez2var
    global netzbez3var
    global infolabelvar
    #clearing up the space
    for counter in range(0,256):
        btns[counter].config(background="lightblue3")
        btns[counter].config(activebackground="lightblue3")
        occuvar[counter] = 0
    for counter in range(1,rdbtncount):
        if isinstance( rdbtn[counter], Radiobutton):
            rdbtn[counter].destroy()
            label[counter].destroy()
    
    #loading in the variables
    loadfile = ""
    loadfile = askopenfilename(filetypes=[("JSON","*.json")])
    with open(loadfile) as json_data_file:
        loaddict = json.load(json_data_file)
    readrdbtn= range(1, 17)
    rdbtncount = loaddict["rdbtncount"]
    netzbez1var.set(loaddict["netzbez1var"])
    netzbez2var.set(loaddict["netzbez2var"])
    netzbez3var.set(loaddict["netzbez3var"])
    rdbtnstartaddr = loaddict["rdbtnstartaddr"]
    rdbtnnetmask = loaddict["rdbtnnetmask"]
    rdbtnbg = loaddict["rdbtnbg"]
    rdbtntext = loaddict["rdbtntext"]
    labeltext = loaddict["labeltext"]
    #building up by the loaded data
    for counter in range(1,rdbtncount):
        rdbtn[counter] = Radiobutton(colors,
                                     text=rdbtntext[counter],
                                     variable=v,
                                     bg=rdbtnbg[counter],
                                     activebackground=rdbtnbg[counter],
                                     value=counter,
                                     command=lambda li=counter: deleterdbtn(li))
        rdbtn[counter].pack(anchor=W)
        label[counter] = Label(colors,
                               text=labeltext[counter],
                               bg=rdbtnbg[counter],
                               wraplength=135)
        label[counter].pack(anchor=E)
        rdbtn[counter].select()
    for counter1 in range(1,rdbtncount):
        if int(rdbtnnetmask[counter1]) == int(netzbez3var.get()):
            netsize = 256
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 1:
            netsize = 128
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 2:
            netsize = 64
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 3:
            netsize = 32
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 4:
            netsize = 16
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 5:
            netsize = 8
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 6:
            netsize = 4
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 7:
            netsize = 2
        elif int(rdbtnnetmask[counter1]) == int(netzbez3var.get()) + 8:
            netsize = 1
        else:
            netsize = 0
            print "ERROR: mask not legitimate or not assigned"
        for counter2 in range(rdbtnstartaddr[counter1],(rdbtnstartaddr[counter1] + netsize)):
            btns[counter2].config(bg=rdbtn[counter1].cget("bg"))
            btns[counter2].config(activebackground=rdbtn[counter1].cget("bg"))
            occuvar[counter2] = rdbtn[counter1].cget("value")
    infolabelvar.set("loaded " + loadfile)

    
def savefile(event=None):
    global rdbtncount
    global netzbez1var
    global netzbez2var
    global netzbez3var
    global rdbtnstartaddr
    global rdbtnnetmask
    global rdbtn
    global label
    global infolabelvar
    rdbtnbg = range(1,17)
    rdbtntext = range(1,17)
    labeltext = range(1,17)
    for counter in range(1,rdbtncount):
        if isinstance(rdbtn[counter], Radiobutton):
            rdbtnbg[counter]=rdbtn[counter].cget("bg")
            rdbtntext[counter]=rdbtn[counter].cget("text")
            labeltext[counter]=label[counter].cget("text")
    savedict = {"rdbtncount": rdbtncount,
                "netzbez1var" : netzbez1var.get(), "netzbez2var" : netzbez2var.get(), "netzbez3var" : netzbez3var.get(),
                "rdbtnstartaddr" : rdbtnstartaddr, "rdbtnnetmask" : rdbtnnetmask, "rdbtnbg" : rdbtnbg,
                "rdbtntext" : rdbtntext, "labeltext" : labeltext}
    savefile = ""
    savefile = asksaveasfilename(defaultextension='.json', filetypes=[("JSON","*.json")])
    with open(savefile, 'w') as outfile:
        json.dump(savedict, outfile)
    infolabelvar.set("saved to " + savefile)

def delete(event=None):
    global recolorvar
    global infolabelvar
    global infolabelvarbuffer
    recolorvar = 2
    infolabelvar.set("currently deleting")
    infolabelvarbuffer = infolabelvar.get()

def cancel(event=None):
    global btns
    global recolorvar
    global infolabelvar
    recolorvar = 0
    for counter in range(0,256):
        btns[counter].config(state=NORMAL)
    infolabelvar.set("cancelled")
    
def recolor(self):
    global v
    global rdbtn
    global btns
    global recolorvar
    global fromvari
    global fromvarj
    global fromvark
    global fromvarl
    global occuvar
    global btnshovered
    global label
    global rdbtnstartaddr
    global rdbtnnetmask
    global infolabelvar
    global infolabelvarbuffer
    radiovar = v.get()
    assignedvar = 0
    for counter in range(0,256):
        if occuvar[counter] == radiovar:
            assignedvar = 1
    if recolorvar == 0 and occuvar[self] == 0 and assignedvar == 0:
        fromvari = btnsvari[self]
        fromvarj = btnsvarj[self]
        fromvark = btnsvark[self]
        fromvarl = btnsvarl[self]
        btns[self].config(relief=RIDGE)
        btnshovered[self] = 1
        rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 8 )
        rdbtnstartaddr[radiovar] = self
        for counter1 in range(0,256):
            btns[counter1].config(state=DISABLED)
            if occuvar[counter1] == 0 or occuvar[counter1] == radiovar:
                if (fromvari % 2) + fromvarj + fromvark + fromvarl == 0 and btnsvari[counter1] >= fromvari:
                    btns[counter1].config(state=NORMAL)
                if (fromvarj % 2) + fromvark + fromvarl == 0 and btnsvarj[counter1] >= fromvarj and btnsvari[counter1] == fromvari:
                    btns[counter1].config(state=NORMAL)
                if (fromvark % 2) + fromvarl == 0 and btnsvark[counter1] >= fromvark and btnsvarj[counter1] == fromvarj and btnsvari[counter1] == fromvari:
                    btns[counter1].config(state=NORMAL)
                if (fromvarl % 2) == 0 and btnsvarl[counter1] >= fromvarl and btnsvark[counter1] == fromvark and btnsvarj[counter1] == fromvarj and btnsvari[counter1] == fromvari:
                    btns[counter1].config(state=NORMAL)
                if (fromvarl % 2) == 1 and btnsvarl[counter1] == fromvarl and btnsvark[counter1] == fromvark and btnsvarj[counter1] == fromvarj and btnsvari[counter1] == fromvari:
                    btns[counter1].config(state=NORMAL)
        disabledmark = 0
        for disabledcounter in range(0,256):
            if btns[disabledcounter].cget("state") == DISABLED:
                disabledmark += 1
        if disabledmark == 256:
            for resetcounter in range(0,256):
                btns[resetcounter].config(state=NORMAL)
            recolorvar = 0
        else:
            recolorvar = 1
        infolabelvar.set("assign " + netzbez1var.get() + btns[rdbtnstartaddr[radiovar]].cget("text") + " /" + str(rdbtnnetmask[radiovar]) + " to: " + rdbtn[radiovar].cget("text"))
        infolabelvarbuffer = "currently assigning " + rdbtn[radiovar].cget("text")
    elif recolorvar == 0 and occuvar[self] == 0 and assignedvar == 1:
        if isinstance( rdbtn[radiovar], Radiobutton):
            infolabelvar.set(rdbtn[radiovar].cget("text") + " is already assigned elsewhere")
        else:
            infolabelvar.set("no subnet selected")
    elif recolorvar == 0 and occuvar[self] != 0 and assignedvar == 0:
        infolabelvar.set("this area is already assigned to " + rdbtn[occuvar[self]].cget("text"))
    elif recolorvar == 1:
        legitselectionvar = 0
        for checkcounter in range(0,256):
            if btns[checkcounter].cget("state") == DISABLED and fromvari <= btnsvari[checkcounter] and btnsvari[self] >= btnsvari[checkcounter] and fromvarj <= btnsvarj[checkcounter] and btnsvarj[self] >= btnsvarj[checkcounter] and fromvark <= btnsvark[checkcounter] and btnsvark[self] >= btnsvark[checkcounter] and fromvarl <= btnsvarl[checkcounter] and btnsvarl[self] >= btnsvarl[checkcounter]:
                legitselectionvar = 1
        if legitselectionvar == 0:
            for counter in range(0,256):
                if btnshovered[counter] == 1:
                    backcolor = rdbtn[radiovar].cget("background")
                    btns[counter].config(background=backcolor)
                    btns[counter].config(activebackground=backcolor)
                    occuvar[counter]=radiovar
        for revokecounter in range(0,256):
            btns[revokecounter].config(state=NORMAL)
        recolorvar = 0
        #netcounter = 0
        #counter = 0
        label[radiovar].config(text=netzbez1var.get() + btns[rdbtnstartaddr[radiovar]].cget("text")+ ":: /" + rdbtnnetmask[radiovar])
        infolabelvar.set("assigned " + rdbtn[radiovar].cget("text"))
    elif recolorvar == 2:
        resetlabel = 1
        for delcount in range(0,256):
            if btnshovered[delcount] == 1:
                if resetlabel == 1:
                    label[occuvar[delcount]].config(text="not assigned")
                    rdbtnstartaddr[occuvar[delcount]] = occuvar[delcount]
                    rdbtnnetmask[occuvar[delcount]] = occuvar[delcount]
                    infolabelvar.set("deleted " + rdbtn[occuvar[delcount]].cget("text"))
                    resetlabel = 0
                btns[delcount].config(bg="lightblue3")
                btns[delcount].config(activebackground="lightblue3")
                occuvar[delcount] = 0
        recolorvar = 0

def unhover(self):
    global recolorvar
    global fromvari
    global fromvarj
    global fromvark
    global fromvarl
    global btnshovered
    global infolabelvar
    global infolabelvarbuffer
    if self != 256:
        for hcount in range(0,256):
            if btns[hcount].cget("state") == NORMAL:
                btns[hcount].config(relief=RAISED)
                if btnshovered[hcount] == 1:
                    btnshovered[hcount] = 0
        if recolorvar == 1 or recolorvar == 2:
            infolabelvar.set(infolabelvarbuffer)
    else:
        for hcount in range(0,256):
            btns[hcount].config(relief=RAISED)
            if btnshovered[hcount] == 1:
                    btnshovered[hcount] = 0
    

def hover(self):
    global recolorvar
    global fromvari
    global fromvarj
    global fromvark
    global fromvarl
    global btnshovered
    global occuvar
    global infolabelvar
    global infolabelvarbuffer
    global btns
    global rdbtnnetmask
    global v
    radiovar = v.get()
    if recolorvar == 1:
        if self != 256:
            for hcount in range(0,256):
                if btns[hcount].cget("state") == NORMAL:
                    if fromvarl == btnsvarl[self] and fromvark == btnsvark[self] and fromvarj == btnsvarj[self] and fromvari == btnsvari[self]:
                        if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                            btns[hcount].config(relief=RIDGE)
                            btnshovered[hcount] = 1
                    elif fromvarl + 1 == btnsvarl[self] and (fromvarl % 2) == 0 and fromvark == btnsvark[self] and fromvarj == btnsvarj[self] and fromvari == btnsvari[self]:
                        if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                            btns[hcount].config(relief=RIDGE)
                            btnshovered[hcount] = 1
                    elif fromvarl == 0 and btnsvarl[self] == 3:
                        if fromvark  == btnsvark[self] and fromvarj == btnsvarj[self] and fromvari == btnsvari[self]:
                            if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                btns[hcount].config(relief=RIDGE)
                                btnshovered[hcount] = 1
                        elif fromvark + 1 == btnsvark[self] and fromvark % 2 == 0 and fromvarj == btnsvarj[self] and fromvari == btnsvari[self]:
                            if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                btns[hcount].config(relief=RIDGE)
                                btnshovered[hcount] = 1
                        elif fromvark == 0 and btnsvark[self] == 3:
                            if fromvarj == btnsvarj[self] and fromvari == btnsvari[self]:
                                if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                    btns[hcount].config(relief=RIDGE)
                                    btnshovered[hcount] = 1
                            elif fromvarj + 1 == btnsvarj[self] and fromvarj % 2 == 0 and fromvari == btnsvari[self]:
                                if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                    btns[hcount].config(relief=RIDGE)
                                    btnshovered[hcount] = 1
                            elif fromvarj == 0 and btnsvarj[self] == 3:
                                if fromvari == btnsvari[self]:
                                    if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                        btns[hcount].config(relief=RIDGE)
                                        btnshovered[hcount] = 1
                                elif fromvari +1 == btnsvari[self] and fromvari % 2 == 0:
                                    if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                        btns[hcount].config(relief=RIDGE)
                                        btnshovered[hcount] = 1
                                elif fromvari == 0 and btnsvari[self] == 3:
                                    if fromvari <= btnsvari[hcount] and btnsvari[self] >= btnsvari[hcount] and fromvarj <= btnsvarj[hcount] and btnsvarj[self] >= btnsvarj[hcount] and fromvark <= btnsvark[hcount] and btnsvark[self] >= btnsvark[hcount] and fromvarl <= btnsvarl[hcount] and btnsvarl[self] >= btnsvarl[hcount]:
                                        btns[hcount].config(relief=RIDGE)
                                        btnshovered[hcount] = 1
            netcounter = 0
            for counter in range(0,256):
                if btnshovered[counter] == 1:
                    netcounter += 1
            if netcounter == 1:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 8 )
            elif netcounter ==2 :
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 7 )
            elif netcounter == 4:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 6 )
            elif netcounter == 8:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 5 )
            elif netcounter == 16:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 4 )
            elif netcounter == 32:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 3 )
            elif netcounter == 64:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 2 )
            elif netcounter == 128:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()) + 1 )
            elif netcounter == 256:
                rdbtnnetmask[radiovar] = str( int(netzbez3var.get()))
            else:
                rdbtnnetmask[radiovar] = "no legit netmask"
            infolabelvarbuffer = infolabelvar.get()
            infolabelvar.set("assign " + netzbez1var.get() + btns[rdbtnstartaddr[radiovar]].cget("text") + " /" + rdbtnnetmask[radiovar] + " to: " + rdbtn[radiovar].cget("text"))

    elif recolorvar == 2:
        if self != 256:
            bool1 = True
            if occuvar[self] != 0:
                for delcount in range(0,256):
                    if occuvar[self] == occuvar[delcount]:
                        btns[delcount].config(relief=RIDGE)
                        btnshovered[delcount] = 1
                        if bool1 == True:
                            infolabelvarbuffer = infolabelvar.get()
                            infolabelvar.set("delete " + rdbtn[occuvar[self]].cget("text"))
                            bool1 = False

def rdbtncommand(self):
    global rdbtn
    global label
    global recolorvar
    global infolabelvar
    global rdbtncount
    if recolorvar == 2:
        infolabelvar.set("deleted " + rdbtn[self].cget("text") + " entirely")
        rdbtn[self].destroy()
        label[self].destroy()
        for counter in range(0,256):
            if occuvar[counter] == self:
                btns[counter].config(bg="lightblue3")
                btns[counter].config(activebackground="lightblue3")
                occuvar[counter] = 0
        for counter in range(1,17):
            if isinstance(rdbtn[counter], Radiobutton):
                rdbtn[counter].select()
        recolorvar = 0
        if self == rdbtncount - 1:
            rdbtncount = rdbtncount -1

def legendhover(self):
    for counter in range(0,256):
        if occuvar[counter] == self:
            btns[counter].config(relief="ridge")

def legendunhover(self):
    for counter in range(0,256):
        if occuvar[counter] == self:
            btns[counter].config(relief="raised")

def newbutton(event=None):
    global colors
    global workarea
    global okbtn
    global v
    top = colors.top = Toplevel(workarea)
    Label(top, text="set legend").pack()
    Label.e = Entry(top)
    Label.e.focus_set()
    Label.e.pack()
    okbtn = Button(top,
                   text="OK", command=ok).pack()
    Label.e.bind("<Return>", ok)
    
def ok(*event):
    global rdbtncount
    global v
    global rdbtn
    global label
    global color
    rdbtn[rdbtncount] = Radiobutton(colors,
                                  text=Label.e.get(),
                                  variable=v,
                                  bg=color,
                                  activebackground=color,
                                  value=rdbtncount,
                                  command=lambda li=rdbtncount: rdbtncommand(li))
    rdbtn[rdbtncount].pack(anchor=W)
    label[rdbtncount] = Label(colors,
                            text="not assigned",
                            bg=color,
                            wraplength=135)
    label[rdbtncount].pack(anchor=E)
    rdbtn[rdbtncount].bind("<Enter>", lambda e, li=rdbtncount: legendhover(li))
    label[rdbtncount].bind("<Enter>", lambda e, li=rdbtncount: legendhover(li))
    rdbtn[rdbtncount].bind("<Leave>", lambda e, li=rdbtncount: legendunhover(li))
    label[rdbtncount].bind("<Leave>", lambda e, li=rdbtncount: legendunhover(li))
    rdbtn[rdbtncount].select()
    standardcolors = ["green", "royal blue", "red", "yellow", "lime", "cyan", "salmon", "gold"]
    color = standardcolors[rdbtncount % len(standardcolors)]
    masterbtn.config(bg=color)
    masterbtn.config(activebackground=color)
    rdbtncount += 1
    colors.top.destroy()

def getcolor():
    global color
    global masterbtn
    color = askcolor(parent=root)[1]
    masterbtn.config(bg=color)
    masterbtn.config(activebackground=color)
    
def callback():
    global infolabelvar
    if ("saved to" or "welcome") not in infolabelvar.get():
        if tkMessageBox.askokcancel("Quit", "Quit without saving?"):
            root.destroy()
    else:
        root.destroy()

def exit_console(*signum, **frame):
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("Really quit? (y/n)?").lower().startswith('y'):
            sys.exit(0)

    except KeyboardInterrupt:
        sys.exit(0)

    signal.signal(signal.SIGINT, exit_console)


MyMenu(root)

original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_console())

root.protocol("WM_DELETE_WINDOW", callback)
root.minsize(width=1000,height=650)
root.maxsize(width=1000,height=650)
app = IPGrid(root)

root.mainloop()
