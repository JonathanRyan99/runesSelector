#uses"pip install pywin32"
#uses "import pyautogui"

import win32gui
import pyautogui


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

#precise,press the attack,triumph,bloodline,cutdown
x = [300,320,400,500,400]
y = [275,420,540,650,760]

for i in range(len(x)):
    select(x[i],y[i])
    

