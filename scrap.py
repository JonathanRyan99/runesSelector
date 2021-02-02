from bs4 import BeautifulSoup
import requests


def mobifireBuild(url):

    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    runeBlock = soup.find("div",{"class": "view-guide__build__runes"})



    #get primary runes
    primaryRuneBlock = runeBlock.find("div", {"class": "new-runes__primary"})
    primaryPath = primaryRuneBlock.get("path")
    primaryRunesHtml = primaryRuneBlock.find_all("span")
    primaryRunes = []
    for i in range(len(primaryRunesHtml)):
        primaryRunes.append(primaryRunesHtml[i].text)

    primaryRunes.pop(0)#first span is "" as its the Path icon on site

    
    #get secondary runes
    secondaryRuneBlock = runeBlock.find("div", {"class": "new-runes__secondary"})
    secondaryPath = secondaryRuneBlock.get("path")
    secondaryRunesHtml = secondaryRuneBlock.find_all("span")
    secondaryRunes = []
    for i in range(len(secondaryRunesHtml)):
        secondaryRunes.append(secondaryRunesHtml[i].text)
    
    secondaryRunes.pop(0)#first span is "" as its the Path icon on site

    #get bonus runes
    bonusBlock = runeBlock.find("div", {"class": "new-runes__shards"})
    bonusHtml = bonusBlock.find_all("span")
    bonus = []

    bonusDict = {
        "diamond" : "adaptive force",
        "axe" : "attack speed",
        "time" : "ability haste",
        "shield" : "armor",
        "heart" : "health",
        "circle" : "magic resist"
    }

    #bonus span tags differ from acutal names so must be converted
    for i in range(len(bonusHtml)):
        bonus.append( bonusDict[bonusHtml[i].get("shard-type")] )
    

    #construct rune page for main program

    runePage = []
    runePage.append(primaryPath)
    runePage.append(secondaryPath)
    runePage.extend(primaryRunes)
    runePage.extend(secondaryRunes)
    runePage.extend(bonus)
    

    #main runes script is all lower case 
    runePage = [element.lower() for element in runePage]
    #url, parts can be case sensitive best to just preserve it
    runePage.append(url)
    
    return runePage

