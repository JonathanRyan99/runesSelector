#uses"pip install pywin32"
#uses "pip install PyAutoGUI"
#uses "pip install beautifulsoup4"
#uses "pip install requests"
import os
import win32gui
import pyautogui
import runes
import scrap

def readfile():
    name = input("file name: ")
    path = name + ".txt"
    with open(path) as f:
        lines = f.read().splitlines()    
    return lines

#uses file
#userRunes = readfile()

#uses link
url = input("mobafire link: ")
userRunes = scrap.mobifireBuild(url)


#finds league window brings it to the front
leagueWindow = win32gui.FindWindow("RCLIENT", None)
win32gui.SetForegroundWindow(leagueWindow )

winPos = win32gui.GetWindowRect(leagueWindow)
print("window displacement: x:",winPos[0]," y:",winPos[1])





#add window displacement to relative coords
def select(coord):
    pyautogui.moveTo( (coord[0]+winPos[0]), (coord[1]+winPos[1]) , duration= 0.5)
    pyautogui.click()


#userRunes structure: (includes the name ones)
#[Path1,Path2,Primary runes,#,#,#,Secondaryrunes,#,#,modifyers,#,#]



Path = runes.Path()
P = runes.Primary()
S = runes.Secondary()
B = runes.Bonus()



#open rune editor
exitButton = (1460,100)
save = (640,163)
editButton = (550,860)
nameBar = (702,850)
choosenSlot = (700,600)

#opens up the rune editor
print(" ")
print("OPENING RUNE EDTOR")
select(nameBar)
select(choosenSlot)
select(editButton)



#selectable locations for paths
print(" ")
print("PATHS: ")
print("PRIMARY: ",userRunes[0])
print("SECONDARY: ",userRunes[1])
pathPos1, pathPos2 = Path.getPaths(userRunes[0],userRunes[1])
select(pathPos1)
select(pathPos2)

#select primary runes
print("")
print("PRIMAY RUNES: ")

if userRunes[0] == "precision":
    x = 2
    for i in range(4):
        print("Precision: ",userRunes[x])
        select(P.precision.get(userRunes[x]))
        x = x + 1
    pass

if userRunes[0] == "domination":
    x = 2
    for i in range(4):
        print("Domination: ",userRunes[x])
        select(P.domination.get(userRunes[x]))
        x = x + 1 
    pass

if userRunes[0] == "sorcery":
    x = 2
    for i in range(4):
        print("Sorcery: ",userRunes[x])
        select(P.sorcery.get(userRunes[x]))
        x = x + 1 
    pass

if userRunes[0] == "resolve":
    x = 2
    for i in range(4):
        print("Resolve: ",userRunes[x])
        select(P.resolve.get(userRunes[x]))
        x = x + 1 
    pass

if userRunes[0] == "inspiration":
    x = 2
    for i in range(4):
        print("Inspiration: ",userRunes[x])
        select(P.inspiration.get(userRunes[x]))
        x = x + 1 
    pass





#select secondary runes
print("")
print("SECONDARY RUNES: ")

if userRunes[1] == "precision":
    x = 6
    for i in range(2):
        print("Precision: ",userRunes[x])
        select(S.precision.get(userRunes[x]))
        x = x + 1
    pass

if userRunes[1] == "domination":
    x = 6
    for i in range(2):
        print("Domination: ",userRunes[x])
        select(S.domination.get(userRunes[x]))
        x = x + 1 
    pass

if userRunes[1] == "sorcery":
    x = 6
    for i in range(2):
        print("Sorcery: ",userRunes[x])
        select(S.sorcery.get(userRunes[x]))
        x = x + 1 
    pass

if userRunes[1] == "resolve":
    x = 6
    for i in range(2):
        print("Resolve: ",userRunes[x])
        select(S.resolve.get(userRunes[x]))
        x = x + 1 
    pass

if userRunes[1] == "inspiration":
    x = 6
    for i in range(2):
        print("Inspiration: ",userRunes[x])
        select(S.inspiration.get(userRunes[x]))
        x = x + 1 
    pass


#select modifyers
print(" ")
print("BONUS: ")


print("Offence: ", userRunes[8])
select(B.offense[userRunes[8]])

print("Flex: ", userRunes[9])
select(B.flex[userRunes[9]])

print("Defence :", userRunes[10])
select(B.defence[userRunes[10]])


print(" ")
print("SAVE AND EXIT")
select(save)
select(exitButton)


print("")
print("PROGRAM FINSIHED")






#print(path1)
#print(path2)

#select(path1)
#select(path2)

#myselection = ["press the attack","overheal", "legend: bloodline", "cut Down"]

#for item in runes.Secondary.sourcery.values():
#    select(item)

#for item in runes.modifyers.offense.values():
#   select(item)

#for i in range(len(myselection)):
#    select(P.precision[myselection[i]])
    

