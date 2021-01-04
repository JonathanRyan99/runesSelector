from bs4 import BeautifulSoup
import requests

#url = input("please link mobifire page: ")
url = "https://www.mobafire.com/league-of-legends/build/10-23-hanjaros-velkoz-supporting-your-way-to-challenger-553890"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

runeBlock = soup.find("div",{"class": "view-guide__build__runes"})

primaryRuneBlock = soup.find("div", {"class": "new-runes__primary"})

#print(primaryRuneBlock)

primaryPath = primaryRuneBlock.get("path")
primaryRunesHtml = primaryRuneBlock.find_all("span")
primaryRunes = []
for i in range(len(primaryRunesHtml)):
    primaryRunes.append(primaryRunesHtml[i].text)

primaryRunes.pop(0)

print(primaryPath)
print(primaryRunes)