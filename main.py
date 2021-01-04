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


P = runes.Primary()
S = runes.Secondary()
path = runes.Path()

path1, path2 = path.getPaths("precision","resolve")

print(path1)
print(path2)

select(path1)
select(path2)

#myselection = ["press the attack","overheal", "legend: bloodline", "cut Down"]

#for item in runes.Secondary.sourcery.values():
#    select(item)


#for i in range(len(myselection)):
#    select(P.precision[myselection[i]])
    

