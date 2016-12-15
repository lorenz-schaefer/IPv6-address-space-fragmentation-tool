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
color = "mediumseagreen"
rdbtncount = 1
colors = 0
workarea = 0
level1frame= range(0, 4)
level2frame= range(0, 4)
level3frame= range(0, 4)
level4frame= range(0, 4)
changeframe0 = False
changeframe1 = False
changeframe2 = False
changeframe3 = False
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
lastvalues= range(0,256)
lowest_subnets_list = []
btnshovered= range(0,256)
address1var = StringVar()
address1var.set("2001:0DB8:00")
address2var = StringVar()
address2var.set("00:: /")
address3var = StringVar()
address3var.set("32")
rdbtnstartaddr= range(1,17)
rdbtnnetmask= range(1,17)
rdbtngridpos= range(4, 36, 2)
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
        topmenu.add_cascade(label="Help", menu=helpMenu)
       
        # the content of the file menu
        fileMenu.add_command(label="load file", command=loadfile)
        fileMenu.add_command(label="save file", command=savefile)
        fileMenu.add_command(label="Quit", command=callback)

        # the content of the help menu
        helpMenu.add_command(label="display shortcuts", command=display_shortcuts)
# thats it for the menubar


class IPGrid:
    def __init__(self, master):
        global colors
        global level1frame
        global level2frame
        global level3frame
        global level4frame
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
        make_occuvar()
        i=0
        workarea = Frame(master)
        colors = Frame(workarea)
        colors.config(borderwidth=2, relief=RIDGE, width=30, height=30)
        bildframe = Frame(workarea)
        addressframe = Frame(bildframe)
        buttons = Frame(bildframe, border=3, relief=FLAT, bg="lightgray")
        counter = 0
        for i in range(0,4):
            level1frame[i] = Frame(buttons, border=3, bg="lightgray")#was: lightblue1
            if i > 1:
                rowvar = 1
            else:
                rowvar = 0
            if i == 1 or i == 3:
                colvar = 1
            else:
                colvar = 0
            level1frame[i].grid(row=rowvar, column=colvar, sticky=(N, E, W, S))
            level1frame[i].grid_columnconfigure(colvar, weight=1)
            level1frame[i].grid_rowconfigure(rowvar, weight=1)
            for j in range(0,4):
                level2frame[j] = Frame(level1frame[i], border=2, bg="lightgray")#was: lightblue2
                if j > 1:
                    rowvar = 1
                else:
                    rowvar = 0
                if j == 1 or j == 3:
                    colvar = 1
                else:
                    colvar = 0
                level2frame[j].grid(row=rowvar, column=colvar)
                level2frame[j].grid_columnconfigure(colvar, weight=1)
                level2frame[j].grid_rowconfigure(rowvar, weight=1)
                for k in range(0,4):
                    level3frame[k] = Frame(level2frame[j], border=1, bg="lightgray") #was: lightblue4
                    if k > 1:
                        rowvar = 1
                    else:
                        rowvar = 0
                    if k == 1 or k == 3:
                        colvar = 1
                    else:
                        colvar = 0
                    level3frame[k].grid(row=rowvar, column=colvar)
                    level3frame[k].grid_columnconfigure(colvar, weight=1)
                    level3frame[k].grid_rowconfigure(rowvar, weight=1)
                    for l in range(0,4):
                        level4frame[l] = Frame(level3frame[k], border = 2, bg="lightgray")
                        if l > 1:
                            rowvar = 1
                        else:
                            rowvar = 0
                        if l == 1 or l == 3:
                            colvar = 1
                        else:
                            colvar = 0
                        level4frame[l].grid(row=rowvar, column=colvar)
                        level4frame[l].grid_columnconfigure(colvar, weight=1)
                        level4frame[l].grid_rowconfigure(rowvar, weight=1)
                        btns[counter] = Button(level4frame[l],
                                               text=str.format("{0:02X}",counter),
                                               background="lightgray",
                                               activebackground="lightgray",
                                               bd=2,
                                               command=lambda li=counter: recolor(li))
                        btns[counter].pack()
                        #btns[counter].grid(row=rowvar, column=colvar, sticky=(N,E,W,S), padx=1, pady=1)
                        #btns[counter].grid_columnconfigure(colvar, weight=1)
                        #btns[counter].grid_rowconfigure(rowvar, weight=1)
                        btns[counter].bind("<Enter>", lambda e,li=counter: hover(li))
                        btns[counter].bind("<Leave>", lambda e,li=counter: unhover(li))
                        level4frame[l].bind("<Enter>", lambda e, li=256: hover(li))
                        level4frame[l].bind("<Leave>", lambda e, li=256: unhover(li))
                        level3frame[k].bind("<Enter>", lambda e, li=256: hover(li))
                        level3frame[k].bind("<Leave>", lambda e, li=256: unhover(li))
                        level2frame[j].bind("<Enter>", lambda e, li=256: hover(li))
                        level2frame[j].bind("<Leave>", lambda e, li=256: unhover(li))
                        level1frame[i].bind("<Enter>", lambda e, li=256: hover(li))
                        level1frame[i].bind("<Leave>", lambda e, li=256: unhover(li))
                        btnsvari[counter]=i
                        btnsvarj[counter]=j
                        btnsvark[counter]=k
                        btnsvarl[counter]=l
                        occuvar[counter].append(0)
                        counter = counter + 1

        bildframe.pack(expand=0, fill="x", side=RIGHT)
        colors.pack(expand=1, fill=BOTH, side=LEFT)
        buttons.pack(expand=1, fill=BOTH, side=BOTTOM)
        workarea.pack(expand=1, fill=BOTH, side=BOTTOM)
        Button(colors,
               text="delete subnet",
               command=delete).grid(row=4, sticky=W+E)
        cancelbtn = Button(colors,
                           text="cancel",
                           command=cancel).grid(row=1, sticky=W+E)
        Button(colors,
               text='select color',
               command=getcolor).grid(row=2, sticky=W+E)
        masterbtn = Button(colors,
                           text='create new button',
                           bg=color,
                           activebackground=color,
                           command=newbutton)
        masterbtn.grid(row=3, sticky=W+E)
        infolabel = Label(colors,
                          textvariable=infolabelvar,
                          justify=LEFT,
                          height=4,
                          width=19,
                          wraplength=135,
                          relief=SUNKEN)
        infolabel.grid(row=0, sticky=S, padx=1)
        addressframe.pack(side=TOP)
        address1label = Label(addressframe,
                             textvariable=address1var).pack(side=LEFT)
        address2label = Label(addressframe,
                             textvariable=address2var).pack(side=LEFT)
        address3label = Label(addressframe,
                             textvariable=address3var).pack(side=LEFT)
        master.bind("<Escape>", cancel)
        master.bind("<o>", loadfile)
        master.bind("<s>", savefile)
        master.bind("<d>", delete)
        master.bind("<n>", newbutton)


def make_occuvar():
    global occuvar
    for counter in range(0,256):
        locals()['level{0}list'.format(counter)] = list()
        #print locals()['level{0}list'.format(counter)[:]]
        occuvar[counter]=locals()['level{0}list'.format(counter)]


def display_shortcuts():
    tkMessageBox.showinfo(title="Shortcuts",message='D => "delete subnet"\nN => "new button"\nO => "open file"\nS => "save file"\nEsc => "cancel"')


def loadfile(event=None):
    global btns
    global occuvar
    global rdbtncount
    global rdbtn
    global label
    global address1var
    global address2var
    global address3var
    global infolabelvar
    global rdbtngridpos
    global level1frame
    global v
    #clearing up the space
    for counter in range(0,256):
        btns[counter].config(background="lightgray")
        btns[counter].config(activebackground="lightgray")
        btns[counter].master.config(bg="lightgray")
        btns[counter].master.master.config(bg="lightgray")
        btns[counter].master.master.master.config(bg="lightgray")
        btns[counter].master.master.master.master.config(bg="lightgray")
        btns[counter].master.master.master.master.master.config(bg="lightgray")
        while len(occuvar[counter]) != 0:
            occuvar[counter].pop()
        occuvar[counter].append(0)
    for counter in range(0,16):
        if isinstance(rdbtn[counter], Radiobutton):
            rdbtn[counter].destroy()
            label[counter].destroy()
   
    #loading in the variables
    loadfile = ""
    loadfile = askopenfilename(filetypes=[("JSON","*.json")])
    with open(loadfile) as json_data_file:
        loaddict = json.load(json_data_file)
    isrdbtn = loaddict["isrdbtn"]
    address1var.set(loaddict["address1var"])
    address2var.set(loaddict["address2var"])
    address3var.set(loaddict["address3var"])
    rdbtnstartaddr = loaddict["rdbtnstartaddr"]
    rdbtnnetmask = loaddict["rdbtnnetmask"]
    rdbtnbg = loaddict["rdbtnbg"]
    rdbtntext = loaddict["rdbtntext"]
    labeltext = loaddict["labeltext"]
    rdbtnvalue = loaddict["rdbtnvalue"]
    rdbtngridpos = loaddict["rdbtngridpos"]
    #building up by the loaded data
    for counter in range(0,16):
        if isrdbtn[counter] == True:
            rdbtn[counter] = Radiobutton(colors,
                                         text=rdbtntext[counter],
                                         variable=v,
                                         bg=rdbtnbg[counter],
                                         activebackground=rdbtnbg[counter],
                                         value=rdbtnvalue[counter],
                                         command=lambda li=rdbtnvalue[counter]: rdbtncommand(li))
            rdbtn[counter].grid(row=rdbtngridpos[counter], sticky=W)
            label[counter] = Label(colors,
                                   text=labeltext[counter],
                                   justify=LEFT,
                                   bg=rdbtnbg[counter],
                                   wraplength=135)
            label[counter].grid(row=rdbtngridpos[counter] + 1, sticky=W)
            rdbtn[counter].select()
            rdbtn[counter].bind("<Enter>", lambda e, li=counter: legendhover(li))
            label[counter].bind("<Enter>", lambda e, li=counter: legendhover(li))
            rdbtn[counter].bind("<Leave>", lambda e, li=counter: legendunhover(li))
            label[counter].bind("<Leave>", lambda e, li=counter: legendunhover(li))
    rdbtnposlist = [0] * 16
    for counter in range(0,16):
        for counter2 in range(0, 16):
            if rdbtngridpos[counter2] == sorted(rdbtngridpos)[counter]:
                rdbtnposlist[counter] = counter2
    for poscounter in rdbtnposlist:
        changeframe0 = False
        changeframe1 = False
        changeframe2 = False
        changeframe3 = False
        if isinstance(rdbtn[poscounter], Radiobutton) == True:
            if int(rdbtnnetmask[poscounter]) == int(address3var.get()):
                netsize = 256
                changeframe3 = True
                changeframe2 = True
                changeframe1 = True
                changeframe0 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 1:
                netsize = 128
                changeframe3 = True
                changeframe2 = True
                changeframe1 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 2:
                netsize = 64
                changeframe3 = True
                changeframe2 = True
                changeframe1 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 3:
                netsize = 32
                changeframe3 = True
                changeframe2 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 4:
                netsize = 16
                changeframe3 = True
                changeframe2 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 5:
                netsize = 8
                changeframe3 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 6:
                netsize = 4
                changeframe3 = True
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 7:
                netsize = 2
            elif int(rdbtnnetmask[poscounter]) == int(address3var.get()) + 8:
                netsize = 1
            else:
                netsize = 0
                print "ERROR: mask not legitimate or not assigned"
            for counter2 in range(rdbtnstartaddr[poscounter],(rdbtnstartaddr[poscounter]+ netsize)):
                btns[counter2].config(bg=rdbtnbg[poscounter])
                btns[counter2].config(activebackground=rdbtnbg[poscounter])
                occuvar[counter2].append(rdbtnvalue[poscounter])
                btns[counter2].master.config(background=rdbtnbg[poscounter])
                if changeframe3 == True:
                    btns[counter2].master.master.config(background=rdbtnbg[poscounter])
                    if changeframe2 == True:
                        btns[counter2].master.master.master.config(background=rdbtnbg[poscounter])
                        if changeframe1 == True:
                            btns[counter2].master.master.master.master.config(background=rdbtnbg[poscounter])
                            if changeframe0 == True:
                                btns[counter2].master.master.master.master.master.config(background=rdbtnbg[poscounter])
    bool1 = True
    for counter in range(1, 17):
        if bool1 == True and not isinstance(rdbtn[counter], Radiobutton):
            rdbtncount = counter
            bool1 = False
    setstandardcolor()
    infolabelvar.set("loaded " + loadfile)


def savefile(event=None):
    global rdbtncount
    global address1var
    global address2var
    global address3var
    global rdbtnstartaddr
    global rdbtnnetmask
    global rdbtn
    global label
    global infolabelvar
    global rdbtngridpos
    rdbtnbg = [0] * 16
    rdbtntext = [0] * 16
    labeltext = [0] * 16
    rdbtnvalue = [0] * 16
    isrdbtn = [False] * 16
    for counter in range(0, 16):
        if isinstance(rdbtn[counter], Radiobutton):
            rdbtnbg[counter] = rdbtn[counter].cget("bg")
            rdbtntext[counter] = rdbtn[counter].cget("text")
            labeltext[counter] = label[counter].cget("text")
            rdbtnvalue[counter] = rdbtn[counter].cget("value")
            isrdbtn[counter] = True
    savedict = {"isrdbtn": isrdbtn,
                "rdbtngridpos": rdbtngridpos,
                "address1var": address1var.get(),
                "address2var": address2var.get(),
                "address3var": address3var.get(),
                "rdbtnstartaddr": rdbtnstartaddr,
                "rdbtnnetmask": rdbtnnetmask,
                "rdbtnbg": rdbtnbg,
                "rdbtnvalue": rdbtnvalue,
                "rdbtntext": rdbtntext,
                "labeltext": labeltext}
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


def update_lastvalues():
    global occuvar
    global lastvalues
    for counter in range(0,256):
        lastvalues[counter] = occuvar[counter].pop()
        occuvar[counter].append(int(lastvalues[counter]))


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
    global lastvalues
    global btnshovered
    global label
    global rdbtnstartaddr
    global rdbtnnetmask
    global infolabelvar
    global infolabelvarbuffer
    global changeframe0
    global changeframe1
    global changeframe2
    global changeframe3
    global rdbtngridpos
    global rdbtn
    global label
    radiovar = v.get()
    assignedvar = 0
    update_lastvalues()
    for counter in range(0,256):
        if lastvalues[counter] == radiovar:
            assignedvar = 1
    if recolorvar == 0 and assignedvar == 0:
        fromvari = btnsvari[self]
        fromvarj = btnsvarj[self]
        fromvark = btnsvark[self]
        fromvarl = btnsvarl[self]
        btns[self].config(relief=RIDGE)
        btnshovered[self] = 1
        rdbtnnetmask[radiovar] = str(int(address3var.get()) + 8)
        rdbtnstartaddr[radiovar] = self
        for counter1 in range(0,256):
            btns[counter1].config(state=DISABLED)
            if lastvalues[counter1] == lastvalues[self]: #or lastvalues[counter1] == 0 or lastvalues[counter1] == radiovar: commented out, cause seems obsolete
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
                if lastvalues[counter1] != 0:
                    if lastvalues[self] != lastvalues[counter1]:
                        btns[counter1].config(state=DISABLED)
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
        infolabelvar.set("assign " + address1var.get() + btns[rdbtnstartaddr[radiovar]].cget("text") + " /" + str(rdbtnnetmask[radiovar]) + " to: " + rdbtn[radiovar].cget("text"))
        infolabelvarbuffer = "currently assigning " + rdbtn[radiovar].cget("text")
    elif recolorvar == 0 and lastvalues[self] == 0 and assignedvar == 1:
        if isinstance( rdbtn[radiovar], Radiobutton):
            infolabelvar.set(rdbtn[radiovar].cget("text") + " is already assigned elsewhere")
        else:
            infolabelvar.set("no subnet selected")
    elif recolorvar == 0 and lastvalues[self] != 0 and assignedvar == 0:
        infolabelvar.set("this area is already assigned to " + rdbtn[lastvalues[self]].cget("text"))
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
                    btns[counter].master.config(background=backcolor)
                    if changeframe3 == True:
                        btns[counter].master.master.config(background=backcolor)
                        if changeframe2 == True:
                            btns[counter].master.master.master.config(background=backcolor)
                            if changeframe1 == True:
                                btns[counter].master.master.master.master.config(background=backcolor)
                                if changeframe0 == True:
                                    btns[counter].master.master.master.master.master.config(background=backcolor)
                    occuvar[counter].append(radiovar)
                    update_lastvalues()
            changeframe0 = False
            changeframe1 = False
            changeframe2 = False
            changeframe3 = False
        for revokecounter in range(0,256):
            btns[revokecounter].config(state=NORMAL)
        recolorvar = 0
        label[radiovar].config(text=address1var.get() + btns[rdbtnstartaddr[radiovar]].cget("text") + ":: /" + rdbtnnetmask[radiovar])
        if len(occuvar[self]) >= 3:
            label[radiovar].config(text="     +--> " + label[radiovar].cget("text"))
            rdbtn[radiovar].config(text="| " + rdbtn[radiovar].cget("text"))
            for counter in range(0, len(occuvar[self]) - 3):
                label[radiovar].config(text="     +" + label[radiovar].cget("text")[5:])
                rdbtn[radiovar].config(text="| " + rdbtn[radiovar].cget("text"))
            occuvarbuffer = occuvar[self].pop()
            occuvarbuffer2 = occuvar[self].pop()
            occuvar[self].append(occuvarbuffer2)
            occuvar[self].append(occuvarbuffer)
            for counter in range(0, 16):
                if rdbtngridpos[counter] > rdbtngridpos[occuvarbuffer2]:
                    rdbtngridpos[counter] += 2
                    if isinstance(rdbtn[counter], Radiobutton):
                        rdbtn[counter].grid(row=rdbtngridpos[counter])
                        label[counter].grid(row=rdbtngridpos[counter] + 1)
            rdbtngridpos[radiovar]=rdbtngridpos[occuvarbuffer2] + 2
            rdbtn[radiovar].grid(row=rdbtngridpos[radiovar])
            label[radiovar].grid(row=rdbtngridpos[radiovar] + 1)


        infolabelvar.set("assigned " + rdbtn[radiovar].cget("text"))
    elif recolorvar == 2:  # the delete process
        resetlabel = 1
        for delcount in range(0,256):
            if btnshovered[delcount] == 1:
                if resetlabel == 1:
                    while rdbtn[lastvalues[delcount]].cget("text")[:2] == "| ":
                        rdbtn[lastvalues[delcount]].config(text=rdbtn[lastvalues[delcount]].cget("text")[2:])
                    label[lastvalues[delcount]].config(text="not assigned")
                    rdbtnstartaddr[lastvalues[delcount]] = lastvalues[delcount]
                    rdbtnnetmask[lastvalues[delcount]] = lastvalues[delcount]
                    infolabelvar.set("deleted " + rdbtn[lastvalues[delcount]].cget("text"))
                    resetlabel = 0
                if btns[delcount].cget("background") == btns[delcount].master.cget("background"):
                    if btns[delcount].master.cget("background") == btns[delcount].master.master.cget("background"):
                        if btns[delcount].master.master.cget("background") == btns[delcount].master.master.master.cget("background"):
                            if btns[delcount].master.master.master.cget("background") == btns[delcount].master.master.master.master.cget("background"):
                                if btns[delcount].master.master.master.master.cget("background") == btns[delcount].master.master.master.master.master.cget("background"):
                                    btns[delcount].master.master.master.master.master.config(bg=btns[delcount].master.master.master.master.master.master.cget("background"))
                                btns[delcount].master.master.master.master.config(bg=btns[delcount].master.master.master.master.master.cget("background"))
                            btns[delcount].master.master.master.config(bg=btns[delcount].master.master.master.master.cget("background"))
                        btns[delcount].master.master.config(bg=btns[delcount].master.master.master.cget("background"))
                    btns[delcount].master.config(bg=btns[delcount].master.master.cget("background"))
                btns[delcount].config(bg=btns[delcount].master.cget("background"))
                btns[delcount].config(activebackground=btns[delcount].master.cget("background"))
                occuvar[delcount].pop()
        recolorvar = 0


def lowest_subnets():
    global occuvar
    global lastvalues
    global lowest_subnets_list
    update_lastvalues()
    occuvarcounter = [0] * 16
    lastvaluescounter = [0] * 16
    for counter in range(0,256):
        for counter2 in range(1,17):
            if counter2 in occuvar[counter]:
                occuvarcounter[counter2 - 1] += 1
            if counter2 == lastvalues[counter]:
                lastvaluescounter[counter2 - 1] += 1
    lowest_subnets_list = []
    for counter in range(0,16):
        if occuvarcounter[counter] == lastvaluescounter[counter] and occuvarcounter[counter] != 0:
            lowest_subnets_list.append(counter + 1)


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
    global changeframe0
    global changeframe1
    global changeframe2
    global changeframe3
    global lastvalues
    global lowest_subnets_list
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
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 8)
            elif netcounter ==2 :
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 7)
            elif netcounter == 4:
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 6)
                changeframe3 = True
            elif netcounter == 8:
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 5)
                changeframe3 = True
            elif netcounter == 16:
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 4)
                changeframe3 = True
                changeframe2 = True
            elif netcounter == 32:
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 3)
                changeframe3 = True
                changeframe2 = True
            elif netcounter == 64:
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 2)
                changeframe3 = True
                changeframe2 = True
                changeframe1 = True
            elif netcounter == 128:
                rdbtnnetmask[radiovar] = str(int(address3var.get()) + 1)
                changeframe3 = True
                changeframe2 = True
                changeframe1 = True
            elif netcounter == 256:
                rdbtnnetmask[radiovar] = str(int(address3var.get()))
                changeframe3 = True
                changeframe2 = True
                changeframe1 = True
                changeframe0 = True
            else:
                rdbtnnetmask[radiovar] = "no legit netmask"
            infolabelvarbuffer = infolabelvar.get()
            infolabelvar.set("assign " + address1var.get() + btns[rdbtnstartaddr[radiovar]].cget("text") + " /" + rdbtnnetmask[radiovar] + " to: " + rdbtn[radiovar].cget("text"))

    elif recolorvar == 2:
        if self != 256:
            update_lastvalues()
            bool1 = True
            if lastvalues[self] != 0:
                lowest_subnets()
                for delcount in range(0,256):
                    if lastvalues[self] == lastvalues[delcount] and lastvalues[delcount] in lowest_subnets_list:
                        btns[delcount].config(relief=RIDGE)
                        btnshovered[delcount] = 1
                        if bool1 == True:
                            infolabelvarbuffer = infolabelvar.get()
                            infolabelvar.set("delete " + rdbtn[lastvalues[self]].cget("text"))
                            bool1 = False


def rdbtncommand(self):
    global rdbtn
    global label
    global recolorvar
    global infolabelvar
    global rdbtncount
    global occuvar
    global lastvalues
    update_lastvalues()
    if recolorvar == 2:
        #for subcounter in range(0, 8):
        #    if rdbtn[self].cget("text")[:(subcounter * 2)] == "| " * subcounter:
        #        prefix = subcounter * 2
        #print "prefix: " + str(prefix)
        #for counter in range(1,17):
        #    if rdbtngridpos[self - 1] + 2 == rdbtngridpos[counter -1]:
        #        print counter
        #        if not rdbtn[counter].cget("text")[:(prefix + 2)] == "| " * (prefix + 1):
        #            print "made it"
        #        print counter
        infolabelvar.set("deleted " + rdbtn[self].cget("text") + " entirely")
        rdbtn[self].destroy()
        rdbtn[self] = self
        label[self].destroy()
        label[self] = self
        for delcount in range(0,256):
            if lastvalues[delcount] == self:
                if btns[delcount].cget("background") == btns[delcount].master.cget("background"):
                    if btns[delcount].master.cget("background") == btns[delcount].master.master.cget("background"):
                        if btns[delcount].master.master.cget("background") == btns[delcount].master.master.master.cget("background"):
                            if btns[delcount].master.master.master.cget("background") == btns[delcount].master.master.master.master.cget("background"):
                                if btns[delcount].master.master.master.master.cget("background") == btns[delcount].master.master.master.master.master.cget("background"):
                                    btns[delcount].master.master.master.master.master.config(bg=btns[delcount].master.master.master.master.master.master.cget("background"))
                                btns[delcount].master.master.master.master.config(bg=btns[delcount].master.master.master.master.master.cget("background"))
                            btns[delcount].master.master.master.config(bg=btns[delcount].master.master.master.master.cget("background"))
                        btns[delcount].master.master.config(bg=btns[delcount].master.master.master.cget("background"))
                    btns[delcount].master.config(bg=btns[delcount].master.master.cget("background"))
                btns[delcount].config(bg=btns[delcount].master.cget("background"))
                btns[delcount].config(activebackground=btns[delcount].master.cget("background"))
                btns[delcount].config(relief="raised")
                occuvar[delcount].pop()
        for counter in range(0,16):
            if isinstance(rdbtn[counter], Radiobutton):
                rdbtn[counter].select()
        recolorvar = 0


def legendhover(self):
    global occuvar
    global lastvalues
    update_lastvalues()
    for counter in range(0,256):
        if self in occuvar[counter]:
            btns[counter].config(relief="ridge")


def legendunhover(self):
    global occuvar
    global lastvalues
    update_lastvalues()
    for counter in range(0,256):
        if self in occuvar[counter]:
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
    global rdbtngridpos
    bool1 = True
    for counter in range(1, 17):
        if bool1 == True and not isinstance(rdbtn[counter],Radiobutton):
            rdbtncount = counter
            bool1 = False
    rdbtn[rdbtncount] = Radiobutton(colors,
                                  text=Label.e.get(),
                                  variable=v,
                                  bg=color,
                                  activebackground=color,
                                  value=rdbtncount,
                                  command=lambda li=rdbtncount: rdbtncommand(li))
    rdbtn[rdbtncount].grid(row=rdbtngridpos[rdbtncount], sticky=W)
    label[rdbtncount] = Label(colors,
                              text="not assigned",
                              bg=color,
                              justify=LEFT,
                              wraplength=135)
    label[rdbtncount].grid(row=rdbtngridpos[rdbtncount] + 1, sticky=W)
    rdbtn[rdbtncount].bind("<Enter>", lambda e, li=rdbtncount: legendhover(li))
    label[rdbtncount].bind("<Enter>", lambda e, li=rdbtncount: legendhover(li))
    rdbtn[rdbtncount].bind("<Leave>", lambda e, li=rdbtncount: legendunhover(li))
    label[rdbtncount].bind("<Leave>", lambda e, li=rdbtncount: legendunhover(li))
    rdbtn[rdbtncount].select()
    setstandardcolor()
    colors.top.destroy()


def setstandardcolor():
    global rdbtncount
    global color
    standardcolors = ["mediumseagreen", "royal blue", "indianred", "yellow", "lightgreen", "paleturquoise", "salmon", "gold"]
    color = standardcolors[rdbtncount % len(standardcolors)]
    masterbtn.config(bg=color)
    masterbtn.config(activebackground=color)


def getcolor():
    global color
    global masterbtn
    color = askcolor(parent=root)[1]
    masterbtn.config(bg=color)
    masterbtn.config(activebackground=color)


def callback():
    global infolabelvar
    if ("saved to" and "welcome" and "loaded") not in infolabelvar.get():
        if tkMessageBox.askokcancel("Quit", "Quit without saving?"):
            root.destroy()
    else:
        root.destroy()


MyMenu(root)


root.protocol("WM_DELETE_WINDOW", callback)
root.minsize(width=1020,height=680)
root.maxsize(width=1020,height=680)
app = IPGrid(root)

root.mainloop()
