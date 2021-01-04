#uses"pip install pywin32"
#uses "pip install PyAutoGUI"
#uses "pip install beautifulsoup4"
#uses "pip install requests"
import os
import win32gui
import pyautogui
import runes

def readfile(name):
    path = name + ".txt"
    with open(path) as f:
        lines = f.read().splitlines()
    
    return lines

#get file
file = input("enter file name: ")
print(" ")
print("READING FILE: ",file)
input = readfile(file)




#finds league window brings it to the front
leagueWindow = win32gui.FindWindow("RCLIENT", None)
win32gui.SetForegroundWindow(leagueWindow )

winPos = win32gui.GetWindowRect(leagueWindow)
print("window displacement: x:",winPos[0]," y:",winPos[1])





#add window displacement to relative coords
def select(coord):
    pyautogui.moveTo( (coord[0]+winPos[0]), (coord[1]+winPos[1]) , duration= 0.5)
    pyautogui.click()


#input structure: (includes the name ones)
#[Path1,Path2,Primary runes,#,#,#,Secondaryrunes,#,#,modifyers,#,#]



Path = runes.Path()
P = runes.Primary()
S = runes.Secondary()
M = runes.modifyers()



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
print("PRIMARY: ",input[0])
print("SECONDARY: ",input[1])
pathPos1, pathPos2 = Path.getPaths(input[0],input[1])
select(pathPos1)
select(pathPos2)

#select primary runes
print("")
print("PRIMAY RUNES: ")

if input[0] == "precision":
    x = 2
    for i in range(4):
        print("Precision: ",input[x])
        select(P.precision.get(input[x]))
        x = x + 1
    pass

if input[0] == "domination":
    x = 2
    for i in range(4):
        print("Domination: ",input[x])
        select(P.domination.get(input[x]))
        x = x + 1 
    pass

if input[0] == "sorcery":
    x = 2
    for i in range(4):
        print("Sorcery: ",input[x])
        select(P.sorcery.get(input[x]))
        x = x + 1 
    pass

if input[0] == "resolve":
    x = 2
    for i in range(4):
        print("Resolve: ",input[x])
        select(P.resolve.get(input[x]))
        x = x + 1 
    pass

if input[0] == "inspiration":
    x = 2
    for i in range(4):
        print("Inspiration: ",input[x])
        select(P.inspiration.get(input[x]))
        x = x + 1 
    pass





#select secondary runes
print("")
print("SECONDARY RUNES: ")

if input[1] == "precision":
    x = 6
    for i in range(2):
        print("Precision: ",input[x])
        select(S.precision.get(input[x]))
        x = x + 1
    pass

if input[1] == "domination":
    x = 6
    for i in range(2):
        print("Domination: ",input[x])
        select(S.domination.get(input[x]))
        x = x + 1 
    pass

if input[1] == "sorcery":
    x = 6
    for i in range(2):
        print("Sorcery: ",input[x])
        select(S.sorcery.get(input[x]))
        x = x + 1 
    pass

if input[1] == "resolve":
    x = 6
    for i in range(2):
        print("Resolve: ",input[x])
        select(S.resolve.get(input[x]))
        x = x + 1 
    pass

if input[1] == "inspiration":
    x = 6
    for i in range(2):
        print("Inspiration: ",input[x])
        select(S.inspiration.get(input[x]))
        x = x + 1 
    pass


#select modifyers
print(" ")
print("MODIFYERS: ")


print("Offence: ", input[8])
select(M.offense[input[8]])

print("Flex: ", input[9])
select(M.flex[input[9]])

print("Defence :", input[10])
select(M.defence[input[10]])


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
    

