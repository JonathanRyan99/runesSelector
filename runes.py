class Path:
    primary = {
        "precision" : (300,275),
        "domination" : (350,275),
        "sorcery" : (400,275),
        "resolve" : (450,275),
        "inspiration" : (500,275)
    }
    secondary = {
        "r1" : (720,275),
        "r2" : (780,275),
        "r3" : (840,275),
        "r4" : (900, 275)
    }

    #secondary paths avaliblity is dependent on the first so have to calculate where it will be 
    def getPaths(self, primaryPath,SecondaryPath):
        orginal = ['precision','domination','sorcery','resolve','inspiration']
        ref = ['r1','r2','r3','r4']
    
        orginal.remove(primaryPath)
        
        SecondaryPath = ref[orginal.index(SecondaryPath)]

        return self.primary[primaryPath] , self.secondary[SecondaryPath]

    
    

class Primary:
    #NO CAPITALS!!! 
    #NAME : X , Y
    precision = {
        "press the attack" : (320,420),
        "lethal tempo" : (380,420),
        "fleet footwork" : (440,420),
        "conqueror" : (500,420),

        "overheal" : (320,540),
        "triumph" :	(400,540),
        "presence of mind" : (500,540),

        "legend: alacrity" : (320,650),
        "legend: tenacity" : (400,650),
        "legend: bloodline" : (500,650),

        "coup de grace" : (320,760),
        "cut down" : (400,760),
        "cast stand" : (500,760)
    }
    domination = {
        "electrocute" : (320,420),
        "predator" : (380,420),
        "dark harvest" : (440,420),
        "hail of blades" : (500,420),

        "cheap shot" : (320,540),
        "taste of blood" : (400,540),
        "sudden impact"	 : (500,540),

        "zombie ward" :	(320,650),
        "ghost poro" :	(400,650),
        "eyeball collection" : (500,650),

        "ravenous hunter" :	(320,760),
        "ingenious hunter" : (380,760),
        "relentless hunter" :	(440,760),
        "ultimate hunter" :	(500,760)
    }
    sorcery = {
        "summon aery" : (320,420),
        "arcane comet" : (400,420),
        "phase rush" : (500,420),

        "nullifiying orb" : (320,540),
        "manaflow band" :	(400,540),
        "nimbus cloak" : (500,540),

        "transcendence"	: (320,650),
        "celerity" : (400,650),
        "absolute focus" : (500,650),

        "scorch" : (320,760),
        "waterwalking" : (400,760),
        "gathering storm" : (500,760)
    }
    resolve = {
        "grasp of the undying" : (320,420),
        "aftershock" :	(400,420),
        "guardian" : (500,420),

        "demolish" : (320,540),
        "font of life" : (400,540),
        "shield bash" : (500,540),

        "conditioning" : (320,650),
        "second wind" : (400,650),
        "bone plating" : (500,650),

        "overgrowth" :	(320,760),
        "revitalize" : (400,760),
        "unflinching" : (500,760)
    }
    inspiration = {
        "glacial augment" :	(320,420),
        "unsealed spellbook" : (400,420),
        "prototype: omnistone" : (500,420),

        "hextech flashtraption" : (320,540),
        "magical footwear" : (400,540),
        "perfect timing" : (500,540),

        "future market"	: (320,	650),
        "minion dematerializer": (400,650),
        "biscuit delivery": (500,650),

        "cosmic insight" : (320,760),
        "approach velocity"	: (400,760),
        "time warp tonic" : (500,760)
    }


class Secondary:
    precision = {
        "overheal" : (730,380),
        "triumph" :	(810,380),
        "presence of mind" : (890,380),

        "legend: alacrity" : (730,480),
        "legend: tenacity" : (810,480),
        "legend: bloodline" : (890,480),

        "coup de grace" : (730,575),
        "cut down" : (810,575),
        "cast stand" : (890,575),

    }
    domination = {
        "cheap shot" : (730,380),
        "taste of blood" : (810,380),
        "sudden impact"	 : (890,380),

        "zombie ward" :	(730,480),
        "ghost poro" :	(810,480),
        "eyeball collection" : (890,480),

        "ravenous hunter" :	(720,575),
        "ingenious hunter" : (780,575),
        "relentless hunter" : (850,575),
        "ultimate hunter" :	(910,575)


    }
    sorcery = {
        "nullifiying orb" : (730,380),
        "manaflow band" :	(810,380),
        "nimbus cloak" : (890,380),

        "transcendence"	: (730,480),
        "celerity" : (810,480),
        "absolute focus" : (890,480),

        "scorch" : (730,575),
        "waterwalking" : (810,575),
        "gathering storm" : (890,575)


    }
    resolve = {
        "demolish" : (730,380),
        "font of life" : (810,380),
        "shield bash" : (890,380),

        "conditioning" : (730,480),
        "second wind" : (810,480),
        "bone plating" : (890,480),

        "overgrowth" :	(730,575),
        "revitalize" : (810,575),
        "unflinching" : (890,575)


    }
    inspiration = {
        "hextech flashtraption" : (730,380),
        "magical footwear" : (810,380),
        "perfect timing" : (890,380),

        "future market"	: (730,480),
        "minion dematerializer": (810,480),
        "biscuit delivery": (890,480),

        "cosmic insight" : (730,575),
        "approach velocity"	: (810,575),
        "time warp tonic" : (890,575)
    }


class Bonus: 
    offense = {
    "adaptive force" : (730,650),
    "attack speed" : (810,650),
    "ability haste" : (890,650),
    }
    
    flex = {
    "adaptive force" : (730,700),
    "armour" : (810,700),
    "magic resist" : (890,700),
    }

    defence = {
    "health" : (730,760),
    "armor" : (810,760),
    "magic resist" : (890,760)
    }