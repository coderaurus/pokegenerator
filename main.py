# -*- coding: cp1252 -*-
from tkinter import *
import sys
from random import *


#exits the program
def lopeta():
    ikkuna.destroy()
    sys.exit(0)

#show proper stats for selected lvl
def changeLvl():
    #print(str(lvl.get())+" and with -5: "+str(int(lvl.get())-5))
    #print("lenght of attackValue "+str(len(attackValue)))
    strAtkV.set("Attack: " + str(attackValue[int(lvl.get())-5]))
    strDefV.set("Defense: " + str(defenseValue[int(lvl.get())-5]))
    strSAtkV.set("Sp. Attack: " + str(sAttackValue[int(lvl.get())-5]))
    strSDefV.set("Sp. Defense: " + str(sDefenseValue[int(lvl.get())-5]))
    strSpeedV.set("Speed: " + str(speedValue[int(lvl.get())-5]))
    ##print("AtkValuen index: " + str(attackValue.index(attackValue[int(lvl.get())-5])))
    strHP.set("HP: "+ str(HPValue[int(lvl.get())-5]))
    strPP.set("PP: "+ str(PPValue[int(lvl.get())-5]))
    strAccuracy.set("Accuracy: "+str(accuracyValue[int(lvl.get())-5]))
    strsAccuracy.set("Sp. Accuracy: "+str(sAccuracyValue[int(lvl.get())-5]))
    strEvasion.set("Evasion: "+str(evasionValue[int(lvl.get())-5]))
    strsEvasion.set("Sp. Evasion: "+str(sEvasionValue[int(lvl.get())-5]))
    return

#calculate difference between stats
def calcDiff(stat, diff):
    # "is it bigger than" -boolean
    isit = False
       
    if(stat == "attackValue"):
        if(attackValue[-1] > defenseValue[-1] + diff):
            isit = True
        elif(attackValue[-1] > sDefenseValue[-1] + diff):
            isit = True
        elif(attackValue[-1] > sAttackValue[-1] + diff):
            isit = True
        elif(attackValue[-1] > speedValue[-1] + diff):
            isit = True
        
    if(stat == "defenseValue"):
        if(defenseValue[-1] > attackValue[-1] + diff):
            isit = True
        elif(defenseValue[-1] > sDefenseValue[-1] + diff):
            isit = True
        elif(defenseValue[-1] > sAttackValue[-1] + diff):
            isit = True
        elif(defenseValue[-1] > speedValue[-1] + diff):
            isit = True
        
    if(stat == "sAttackValue"):
        if(sAttackValue[-1] > defenseValue[-1] + diff):
            isit = True
        elif(sAttackValue[-1] > sDefenseValue[-1] + diff):
            isit = True
        elif(sAttackValue[-1] > attackValue[-1] + diff):
            isit = True
        elif(sAttackValue[-1] > speedValue[-1] + diff):
            isit = True
        
    if(stat == "sDefenseValue"):
        if(sDefenseValue[-1] > defenseValue[-1] + diff):
            isit = True
        elif(sDefenseValue[-1] > attackValue[-1] + diff):
            isit = True
        elif(sDefenseValue[-1] > sAttackValue[-1] + diff):
            isit = True
        elif(sDefenseValue[-1] > speedValue[-1] + diff):
            isit = True
        
    if(stat == "speedValue"):
        if(speedValue[-1] > defenseValue[-1] + diff):
            isit = True
        elif(speedValue[-1] > sDefenseValue[-1] + diff):
            isit = True
        elif(speedValue[-1] > sAttackValue[-1] + diff):
            isit = True
        elif(speedValue[-1] > attackValue[-1] + diff):
            isit = True
    
    ##print("isit is: "+str(isit))
    return isit

#add special stats (hp, pp, ...)
#def addSS(i):
#    HPValue.append(attackValue[i] + defenseValue[i])
#    PPValue.append(sAttackValue[i] + sDefenseValue[i] + \
#        speedValue[i])
#    accuracyValue.append(attackValue[i] + speedValue[i])
#    sAccuracyValue.append(sAttackValue[i] + speedValue[i])
#    evasionValue.append(speedValue[i] + defenseValue[i])
#    sEvasionValue.append(speedValue[i] + sDefenseValue[i])
def setNature(value):
    #Hardy / Docile / Serious / Bashful / Quirky
    if value == 0 or value == 6 or value == 12 or value == 18 or value == 24: 
        return
    ## + ATTACK             + ATTACK
    elif value == 1:        #Lonely     (+atk,      -def)
        attackValue[0] += 5
        defenseValue[0] -= 5
    elif value == 2:        #Brave      (+atk,      -speed)
        attackValue[0] += 5
        speedValue[0] -= 5
    elif value == 3:        #Adamant    (+atk,      -sp atk)
        attackValue[0] += 5
        sAttackValue[0] -= 5
    elif value == 4:        #Naughty    (+atk,      -sp def)
        attackValue[0] += 5
        sDefenseValue[0] -= 5
    ## + DEFENSE            + DEFENSE
    elif value == 5:        #Bold       (+def,      -atk)
        defenseValue[0] += 5
        attackValue[0] -= 5
    elif value == 7:        #Relaxed    (+def,       -speed)
        defenseValue[0] += 5
        speedValue[0] -= 5
    elif value == 8:        #Impish     (+def,      -spAtk)
        defenseValue[0] += 5
        sAttackValue[0] -= 5
    elif value == 9:        #Lax        (+def,      -spDef)
        defenseValue[0] += 5
        sDefenseValue[0] -= 5
    ## + SPEED              + SPEED
    elif value == 10:       #Timid      (+speed,    -atk)
        speedValue[0] += 5
        attackValue[0] -= 5
    elif value == 11:       #Hasty      (+speed,    -def)
        speedValue[0] += 5
        defenseValue[0] -= 5
    elif value == 13:       #Jolly      (+speed,    -spAtk)
        speedValue[0] += 5
        sAttackValue[0] -= 5
    elif value == 14:       #Naive      (+speed,    -spDef)
        speedValue[0] += 5
        sDefenseValue[0] -= 5
    ## + SP ATTACK          + SP ATTACK
    elif value == 15:       #Modest     (+spAtk,    -atk)
        sAttackValue[0] += 5
        attackValue[0] -= 5
    elif value == 16:       #Mild       (+spAtk,    -def)
        sAttackValue[0] += 5
        defenseValue[0] -= 5
    elif value == 17:       #Quiet      (+spAtk,    -speed)
        sAttackValue[0] += 5
        speeedValue[0] -= 5
    elif value == 19:       #Rash       (+spAtk,    -spDef)
        sAttackValue[0] += 5
        attackValue[0] -= 5
    ## + SP DEFENSE         +SP DEFENSE
    elif value == 20:       #Calm       (+spDef,    -atk)
        sDefenseValue[0] +=5
        attackValue[0] -= 5
    elif value == 21:        #Gentle    (+spDef,    -def)
        sDefenseValue[0] +=5
        defenseValue[0] -= 5
    elif value == 22:       #Sassy      (+spDef,    -speed)
        sDefenseValue[0] +=5
        speedValue[0] -= 5
    elif value == 23:       #Careful    (+spDef,    -spAtk)
        spDefenseValue[0] +=5
        sAttackValue[0] -= 5
        
#generate random stats
def generateStats():

    rNature = randint(0,24)
    ##print("Nature is "+str(rNature))
    strNature.set("Nature: "+str(nature[rNature]))
    
    attackValue.append(10)
    defenseValue.append(10)
    sAttackValue.append(10)
    sDefenseValue.append(10)
    speedValue.append(10)

    if(atkC.get() == True):
        attackValue[0] += 10
    if(defC.get() == True):
        defenseValue[0] += 10
    if(sAtkC.get() == True):
        sAttackValue[0] += 10
    if(sDefC.get() == True):
        sDefenseValue[0] += 10
    if(speedC.get() == True):
        speedValue[0] += 10

    setNature(rNature)
            
    HPValue.append(attackValue[0] + defenseValue[0])
    PPValue.append(sAttackValue[0] + sDefenseValue[0] + \
                    speedValue[0])
    accuracyValue.append(attackValue[0] + speedValue[0])
    sAccuracyValue.append(sAttackValue[0] + speedValue[0])
    evasionValue.append(speedValue[0] + defenseValue[0])
    sEvasionValue.append(speedValue[0] + sDefenseValue[0])

    i=1
    rNum = 0
    correctLvlup = False
    
    for i in range(94):
        correctLvlup = False
        while(correctLvlup == False):
            rNum = randint(0,4)
            print("I : "+str(i))
            if(rNum == 0):
                ##print("Check: "+str(atkC.get())+", calcDif:"+str(calcDiff("attackValue",40)))
                if(atkC.get() == True and calcDiff("attackValue",40) == False):
                    attackValue.append(attackValue[i] + 10)
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i])

                    correctLvlup = True

                    #addSS(i)
                        
                elif(atkC.get() == False and  calcDiff("attackValue",25) == False):
                    attackValue.append(attackValue[i] + 5)
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i])

                    correctLvlup = True

                    #addSS(i)
                print("AttakValue + 5")
                
            if(rNum == 1):
                if(defC.get() == True and calcDiff("defenseValue",40) == False):
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i] + 10)
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i])

                    correctLvlup = True
                        
                elif(calcDiff("defenseValue",25) == False):
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i]+ 5)
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i])

                    correctLvlup = True

                    #addSS(i)
                print("DefenseValue + 5")
                    
            if(rNum == 2):
                if(sAtkC.get() == True and calcDiff("sAttackValue",40) == False):
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i] + 10)
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i])

                    correctLvlup = True

                    #addSS(i)
                        
                elif(calcDiff("sAttackValue",25) == False):
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i] + 5)
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i])

                    correctLvlup = True
                    
                    #addSS(i)
                print("sAttakValue + 5")
                
            if(rNum == 3):
                if(sDefC.get() == True and calcDiff("sDefenseValue",40) == False):
                    
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i] + 10)
                    speedValue.append(speedValue[i])

                    correctLvlup = True

                    #addSS(i)
                        
                elif(calcDiff("sDefenseValue",25) == False):
                    
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i] + 5)
                    speedValue.append(speedValue[i])

                    correctLvlup = True

                    #addSS(i)
                print("sDefenseValue + 5")
            if(rNum == 4):
                if(speedC.get() == True and calcDiff("speedValue",40) == False):
                   
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i] + 10)

                    correctLvlup = True

                    #addSS(i)
                        
                elif(calcDiff("speedValue",25) == False):
                    
                    attackValue.append(attackValue[i])
                    defenseValue.append(defenseValue[i])
                    sAttackValue.append(sAttackValue[i])
                    sDefenseValue.append(sDefenseValue[i])
                    speedValue.append(speedValue[i] + 5)

                    correctLvlup = True

                    #addSS(i)
                print("speedValue + 5")   
            
            HPValue.append(attackValue[i] + defenseValue[i])
            PPValue.append(sAttackValue[i] + sDefenseValue[i] + \
                           speedValue[i])
            accuracyValue.append(attackValue[i] + speedValue[i])
            sAccuracyValue.append(sAttackValue[i] + speedValue[i])
            evasionValue.append(speedValue[i] + defenseValue[i])
            sEvasionValue.append(speedValue[i] + sDefenseValue[i])
            #print("Correctlvlup is *"+str(correctLvlup)+ "*, i = "+ str(i))   
        
        i += 1
    
def clearStats():

    strNature.set("")
    attackValue[:] = []
    defenseValue[:] = []
    sAttackValue[:] = []
    sDefenseValue[:] = []
    speedValue[:] = []
    HPValue[:] = []
    PPValue[:] = []
    accuracyValue[:] = []
    sAccuracyValue[:] = []
    evasionValue[:] = []
    sEvasionValue[:] = []
    
    return
            

def randomizeStats():
    checked = 0
    addOne = 1
    if(atkC.get() == True):
        checked += addOne
    if(defC.get() == True):
        checked += addOne
    if(sAtkC.get() == True):
        checked += addOne
    if(sDefC.get() == True):
        checked = checked + addOne
    if(speedC.get() == True):
        checked = checked + addOne
    ##print("Checked: "+ str(checked))
    if(checked > 2):
        messagebox.showerror(title="Error!", \
            message="You chose too many stats!")
    else:
        clearStats()
        generateStats()
        changeLvl()
        


#let's make create the window
ikkuna = Tk()
ikkuna.title("Pokemon Generator")
ikkuna.geometry("600x450")

#defining some values
strNature = StringVar()
strNature.set("Nature: ")

#values for checkbuttons
atkC = BooleanVar()
defC = BooleanVar()
sAtkC = BooleanVar()
sDefC = BooleanVar()
speedC = BooleanVar()

luku2 = IntVar()

#the real values for pokemon's stats
nature = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", \
          "Bold", "Docile", "Relaxed", "Impish", "Lax", \
          "Timid", "Hasty", "Serious", "Jolly", \
          "Naive", "Modest", "Mild", "Quiet", "Bashful", \
          "Rash", "Calm", "Gentle", "Sassy", "Careful", \
          "Quirky"]
attackValue = []
defenseValue = []
sAttackValue = []
sDefenseValue = []
speedValue = []

HPValue = []
PPValue = []
accuracyValue = []
sAccuracyValue = []
evasionValue = []
sEvasionValue = []

generateStats()

strAtkV = StringVar()
strAtkV.set("Attack: " + str(attackValue[0]))

strDefV = StringVar()
strDefV.set("Defense: " + str(defenseValue[0]))

strSAtkV = StringVar()
strSAtkV.set("Sp. Attack: " + str(sAttackValue[0]))

strSDefV = StringVar()
strSDefV.set("Sp. Defense: " + str(sDefenseValue[0]))

strSpeedV = StringVar()
strSpeedV.set("Speed: " + str(speedValue[0]))

strHP = StringVar()
strHP.set("HP: "+ str(HPValue[0]))

strPP = StringVar()
strPP.set("PP: "+ str(PPValue[0]))

strAccuracy = StringVar()
strAccuracy.set("Accuracy: "+str(accuracyValue[0]))

strsAccuracy = StringVar()
strsAccuracy.set("Sp. Accuracy: "+str(sAccuracyValue[0]))

strEvasion = StringVar()
strEvasion.set("Evasion: "+str(evasionValue[0]))

strsEvasion = StringVar()
strsEvasion.set("Sp. Evasion: "+str(sEvasionValue[0]))

#-----------------
#--- U I


ruutu1 = Frame(ikkuna)
ruutu1.pack(side = LEFT, fill="both")
ruutu2 = Frame(ikkuna)
ruutu2.pack(side = RIGHT, fill="both")

#setting up label frames "stats" and "natural talent"
labelF = LabelFrame(ruutu1, text="Stats")
labelF.pack()

labelF2 = LabelFrame(ruutu2, text="Natural Talent")
labelF2.pack(side=TOP)


lvlL = Label(labelF, text="LVL:")
lvlL.pack()

lvl = Spinbox(labelF, from_=5, to=100, command = changeLvl)
lvl.pack()


lNature = Label(labelF, textvariable=strNature)
lNature.pack()

lSex = Label(labelF, text="Sex: Male")
lSex.pack()

lHP = Label(labelF, textvariable = strHP, fg="#999")
lHP.pack()

lPP = Label(labelF, textvariable = strPP, fg="#999")
lPP.pack()

lAtk = Label(labelF, textvariable = strAtkV)
lAtk.pack()

lDef = Label(labelF, textvariable = strDefV)
lDef.pack()

lsAtk = Label(labelF, textvariable = strSAtkV)
lsAtk.pack()

lsDef = Label(labelF, textvariable = strSDefV)
lsDef.pack()

lSpeed = Label(labelF, textvariable = strSpeedV)
lSpeed.pack()

lAccuracy = Label(labelF, textvariable = strAccuracy, fg="#999")
lAccuracy.pack()

lsAccuracy = Label(labelF, textvariable = strsAccuracy, fg="#999")
lsAccuracy.pack()

lEvasion = Label(labelF, textvariable = strEvasion, fg="#999")
lEvasion.pack()

lsEvasion = Label(labelF, textvariable = strsEvasion, fg="#999")
lsEvasion.pack()

#checkbuttons
AtkCheck = Checkbutton(labelF2, text = "Attack", \
                variable = atkC, \
                 height=2, \
                 width = 10)
AtkCheck.pack()

DefCheck = Checkbutton(labelF2, text = "Defense", \
                variable = defC, \
                height=2, width = 10)
DefCheck.pack()

sAtkCheck = Checkbutton(labelF2, text = "Sp. Attack", \
                variable = sAtkC, \
                height=2, width = 10)
sAtkCheck.pack()

sDefCheck = Checkbutton(labelF2, text = "Sp. Defense", \
                variable = sDefC, \
                height=2, width = 10)
sDefCheck.pack()

SpeedCheck = Checkbutton(labelF2, text = "Speed", \
                variable = speedC, \
                height=2, width = 10)
SpeedCheck.pack()

#generate button
btnGenerate = Button(ruutu2, text="Generate stats", \
                     width = 12, command = randomizeStats)
btnGenerate.pack()


lopeta_nappi = Button(ruutu2, text = "Lopeta", \
width = 12, command = lopeta)
lopeta_nappi.pack(side = BOTTOM)

ikkuna.mainloop()

