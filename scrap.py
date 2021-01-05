from bs4 import BeautifulSoup
import requests


def mobifireBuild(url):

    #url = input("please link mobifire page: ")
    #url = "https://www.mobafire.com/league-of-legends/build/10-23-hanjaros-velkoz-supporting-your-way-to-challenger-553890"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    runeBlock = soup.find("div",{"class": "view-guide__build__runes"})




    primaryRuneBlock = runeBlock.find("div", {"class": "new-runes__primary"})
    primaryPath = primaryRuneBlock.get("path")
    primaryRunesHtml = primaryRuneBlock.find_all("span")
    primaryRunes = []
    for i in range(len(primaryRunesHtml)):
        primaryRunes.append(primaryRunesHtml[i].text)

    primaryRunes.pop(0)

    #print(primaryPath)
    #print(primaryRunes)

    print("")

    secondaryRuneBlock = runeBlock.find("div", {"class": "new-runes__secondary"})
    secondaryPath = secondaryRuneBlock.get("path")
    secondaryRunesHtml = secondaryRuneBlock.find_all("span")
    secondaryRunes = []
    for i in range(len(secondaryRunesHtml)):
        secondaryRunes.append(secondaryRunesHtml[i].text)
    secondaryRunes.pop(0)


    #print(secondaryPath)
    #print(secondaryRunes)


    bonusDict = {
        "diamond" : "adaptive force",
        "axe" : "attack speed",
        "time" : "ability haste",
        "shield" : "armor",
        "heart" : "health",
        #magic resist
    }

    bonusBlock = runeBlock.find("div", {"class": "new-runes__shards"})
    bonusHtml = bonusBlock.find_all("span")
    bonus = []
    #bonus span tags differ from acutal names so must be converted
    for i in range(len(bonusHtml)):
        bonus.append( bonusDict[bonusHtml[i].get("shard-type")] )
    #print(bonus)



    #construct the input rune page for main program

    runePage = []
    runePage.append(primaryPath)
    runePage.append(secondaryPath)
    runePage.extend(primaryRunes)
    runePage.extend(secondaryRunes)
    runePage.extend(bonus)

    #main runes script is all lower case so conversion is necessary
    runePage = [element.lower() for element in runePage]
    #print(runePage)
    return runePage

