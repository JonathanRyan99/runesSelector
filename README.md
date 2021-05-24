# runesSelector
create League of Legends rune pages on the fly in champ select

this application is capable of quickly creating and selecting a rune page in around 7 seconds

how to use:
have a rune page in the 6th slot called custom or dynamic as this is the one that will be remade everytime you run the program.

after downloading this application create a folder inside called "saves" this will store previously saved builds, without this folder only the build line will work.

Gui function:

the first input line of the application is Mobafire Link. input the mobafire link of the build you want to replicate the runes for and click "Build" 
this will scrape the runes from the webpage and automatically click in the game to construct and save this rune page.

Save as
so the first line gets the runepage and builds it so why do you need this?, well if you're on a free account and dont want to buy endless runepages you can just save the 
rune setup from the site to use at a later date with the save as function. just give it a name and click save. (this wont work if you dont supply a link in the mobafire link section
as it uses this to query the site.

once you've saved and restarted the application the name you chose will appear in the section to the left of the application. if you want to quickly build this page just select it
and press "Ok". it should then run through and make this page just like the build function.

the "link" button will automatically open a browser with the page of the build you selected,(the link of the page is tied to the save but will work if its dead) 
this is helpful as it shows you the full build it does not 
require the page being created inside of league either its stand alone.

Custom runepages:

create a txt file inside of Saves, call it what ever you want

each rune page is broken down into the following structure:

primary rune (eg. presision, sourcery)
secondary rune (eg. presision, sourcery)
primay rune components ( counqueror, triump)
secondary rune components ( legend: alacrity)
bouns runes (attack speed, adpative force)
mobafire link

example aatrox build: 
precision
domination
conqueror
triumph
legend: alacrity
last stand
sudden impact
ravenous hunter
attack speed
adaptive force
armor
https://www.mobafire.com/league-of-legends/build/world-ender-aatrox-jungle-extensive-guide-521297

be presise in your spelling all of these are specfically designed to work with Mobafire site,
so if in doubt use the names of the html elements that mobafire provides and this
should all work.

the mobafire link is not strictly necessary either,however the link option when selected may crash the application.

this was all compatiable with league of legends version V11.10 24/05/2021


