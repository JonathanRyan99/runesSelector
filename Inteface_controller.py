#uses"pip install pywin32"
#uses "pip install PyAutoGUI"
#uses "pip install beautifulsoup4"
#uses "pip install requests"

import pywintypes # Not used, but need it for win32gui to import correctly
import win32gui
import pyautogui
import runes
import time

#this is to find the local directory pyinstaller points to the archive where its made need to do this to get around it
#look at docs for explaination "runtime-infomation"


def RuneBuilder(userRunes):
    #time selection execution
    start_time = time.time()
    #userRunes array structure
    #[PrimaryPath,SecondaryPath,Prune,Prune,Prune,Prune,Srune,Srune,Srune,bonus,bonus,bonus]


    #finds league window brings it to the front    CURRENTLY CRASHES IF IT CANT
    leagueWindow = win32gui.FindWindow("RCLIENT", None)
    win32gui.SetForegroundWindow(leagueWindow )

    winPos = win32gui.GetWindowRect(leagueWindow)
    print("window displacement: x:",winPos[0]," y:",winPos[1])





    #add window displacement to relative coords and click
    def select(coord):
        pyautogui.moveTo( (coord[0]+winPos[0]), (coord[1]+winPos[1]) , duration= 0.1)
        pyautogui.click()

    #use this if the interface/window takes time load
    def selectCustom(coord,speed):
        pyautogui.moveTo( (coord[0]+winPos[0]), (coord[1]+winPos[1]) , duration= speed)
        pyautogui.click()


    Path = runes.Path()
    P = runes.Primary()
    S = runes.Secondary()
    B = runes.Bonus()



    #league interface coords
    exitButton = (1460,100)
    save = (640,163)
    editButton = (550,860)
    nameBar = (702,850)
    choosenSlot = (700,600)

    #opens up the rune editor
    print(" ")
    print("OPENING RUNE EDTOR")
    selectCustom(nameBar, 0.2)
    selectCustom(choosenSlot, 0.2)
    selectCustom(editButton, 0.2)



    #select Paths
    print(" ")
    print("PATHS: ")
    print("PRIMARY: ",userRunes[0])
    print("SECONDARY: ",userRunes[1])
    pathPos1, pathPos2 = Path.getPaths(userRunes[0],userRunes[1])
    selectCustom(pathPos1, 0.5)
    selectCustom(pathPos2, 0.5)

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

    print("")
    print("--- %s seconds ---" % (time.time() - start_time))
    
        

