import math
import random

def combo(buttons):
    return comboWithMax(buttons, buttons)

def comboWithMax(buttons, maxPress):
    symbols = buttons #stores number of possible digits for syntactical reasons
    combo = ""
    unused = range(1, buttons+1, 1)
    while(buttons>0):
        press = weightedPress(buttons, maxPress)
        if (press == 0): #don't press anything
            if (buttons == 5):
                combo = "empty" #zero button combo
            buttons = 0
        else:
            buttons -= press
            if (combo != ""):
                combo += "-"
                
            holding = []
            for x in range(press):
                index = random.randrange(len(unused))
                num = unused[index]
                unused.remove(num)
                holding.append(num)
            first = True
            holding.sort() #prevents combos that look different but really are the same
            for num in holding:
                if (not first and symbols > 9): #make it readable with more digits than 0
                    combo += ","
                first = False
                combo += str(num)
    return combo

def comboWithPattern(buttons, pattern):
    symbols = buttons #stores number of possible digits for syntactical reasons
    combo = ""
    unused = range(1, buttons+1, 1)
    while(buttons>0 and len(pattern)>0):
        press = pattern.pop(0)
        if (press == 0): #don't press anything
            if (buttons == 5):
                combo = "empty" #zero button combo
            buttons = 0
        else:
            buttons -= press
            if (combo != ""):
                combo += "-"
                
            holding = []
            for x in range(press):
                index = random.randrange(len(unused))
                num = unused[index]
                unused.remove(num)
                holding.append(num)
            first = True
            holding.sort() #prevents combos that look different but really are the same
            for num in holding:
                if (not first and symbols > 9): #make it readable with more digits than 0
                    combo += ","
                first = False
                combo += str(num)
    return combo

def randomComboList(buttons, maxPress):
    combos = list()
    maxCombos = numCombosWithMax(buttons, maxPress)
    while (len(combos) < maxCombos):
        combo = comboWithMax(buttons, maxPress)
        if (combo not in combos):
            combos.append(combo)
    return combos

#generates a random number in range [0, buttons] that is weighted based on the possible number of combos per number of presses
def weightedPress(buttons, maxPress):
    total = numCombosWithMax(buttons, maxPress)
    rand = random.randrange(total)+1
    
    press = -1
    while (rand > 0):
        press += 1
        rand -= numCombosWithPressWithMax(buttons, press, maxPress)
    return press

#number of combos availbile for a given number of buttons and buttons pressed at once
def numCombosWithPressWithMax(buttons, press, maxPress):
    if (press == 0):
        return 1
    else:
        return combination(buttons, press) * numCombosWithMax(buttons-press, maxPress)
        
def numCombosWithPattern(buttons, pattern):
    if (len(pattern) == 0):
        return 1
    else:
        press = pattern.pop(0)
        return combination(buttons, press) * numCombosWithPattern(buttons-press, pattern)

#total number of combos availble for n buttons given the possiblity of all presses in the set [0,n]
def numCombosWithMax(buttons, maxPress):
    if (buttons == 0): return 1
    else:
        sum = 0
        #maxPress is max number of buttons pressed at once
        for press in xrange(0, min(buttons, maxPress)+1, 1):
            sum += numCombosWithPressWithMax(buttons, press, maxPress)
        return sum
    
def numCombos(buttons):
    return numCombosWithMax(buttons, buttons)
    
def combination(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
   
def printList(list):
    for item in list:
        print item
        
def randomComboListWithPattern(buttons, pattern):
    combos = list()
    maxCombos = numCombosWithPattern(buttons, pattern[:])
    while (len(combos) < maxCombos):
        combo = comboWithPattern(buttons, pattern[:])
        if (combo not in combos):
            #print combo
            combos.append(combo)
    return combos
        
#2 1 1
combos = randomComboListWithPattern(5, [2,1,1])
print len(combos)
print combos