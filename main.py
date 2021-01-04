#uses"pip install pywin32"
#uses "import pyautogui"

import win32gui
import pyautogui
import runes


#finds league window brings it to the front
leagueWindow = win32gui.FindWindow("RCLIENT", None)
win32gui.SetForegroundWindow(leagueWindow )

winPos = win32gui.GetWindowRect(leagueWindow)
print("coordinates:")
print("top: ",winPos[0]) # x
print("left: ",winPos[1]) # y




def select(x,y):
    pyautogui.moveTo( (x+winPos[0]), (y+winPos[1]) , duration= 0.5)
    pyautogui.click()

def select(coord):
    pyautogui.moveTo( (coord[0]+winPos[0]), (coord[1]+winPos[1]) , duration= 0.5)
    pyautogui.click()

Path = runes.Path()
P = runes.Primary()
S = runes.Secondary()
M = runes.modifyers()



input1 = ["precision", "resolve","press the attack", "presence of mind", "legend: alacrity", "cut down", "demolish", "second wind", "overgrowth","attack speed","adaptive force","armor"]
input2 = ["domination","resolve","hail of blades","taste of blood","eyeball collection","ravenous hunter"]

input = input1

#selectable locations for paths
pathPos1, pathPos2 = Path.getPaths(input[0],input[1])
select(pathPos1)
select(pathPos2)



#select primary runes
if input[0] == "precision":
    x = 2
    for i in range(4):
        select(P.precision.get(input[x]))
        x = x + 1
    pass

if input[0] == "domination":
    x = 2
    for i in range(4):
        select(P.domination.get(input[x]))
        x = x + 1 
    pass

if input[0] == "sorcery":
    x = 2
    for i in range(4):
        select(P.sorcery.get(input[x]))
        x = x + 1 
    pass

if input[0] == "resolve":
    x = 2
    for i in range(4):
        select(P.resolve.get(input[x]))
        x = x + 1 
    pass

if input[0] == "inspiration":
    x = 2
    for i in range(4):
        select(P.inspiration.get(input[x]))
        x = x + 1 
    pass





#select secondary runes

if input[1] == "precision":
    x = 6
    for i in range(3):
        select(S.precision.get(input[x]))
        x = x + 1
    pass

if input[1] == "domination":
    x = 6
    for i in range(3):
        select(S.domination.get(input[x]))
        x = x + 1 
    pass

if input[1] == "sorcery":
    x = 6
    for i in range(3):
        select(S.sorcery.get(input[x]))
        x = x + 1 
    pass

if input[1] == "resolve":
    x = 6
    for i in range(3):
        select(S.resolve.get(input[x]))
        x = x + 1 
    pass

if input[1] == "inspiration":
    x = 6
    for i in range(3):
        select(S.inspiration.get(input[x]))
        x = x + 1 
    pass

#select modifyers
select(M.offense[input[9]])
select(M.flex[input[10]])
select(M.defence[input[11]])







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
    

