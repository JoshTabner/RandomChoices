import random

## Monkey Island Fight

insults = ["You fight like a dairy farmer!", "This is the END for you, you gutter crawling cur!",
           "I've spoken with apes more polite than you!", "Soon you'll be wearing my sword like a shish kebab!", "People fall at my feet when they see me coming!"]
comebacks = ["How appropriate. You fight like a cow!", "And I've got a little TIP for you, get the POINT?",
             "I'm glad to hear you attended your family reunion!", "First you'd better stop waving it like a feather duster.", "Even BEFORE they smell your breath?"]
choices = []
tempComebacks = []

choiceNum = 0
rInsult = random.choice(insults)
#print(rInsult)
rChoice = ""
for i in range(len(insults)):
    if insults[i] == rInsult:
        #print("after if")
        rChoice = comebacks[i]
        #print("RChoice: " + rChoice)
for i in range(len(comebacks)):
    if comebacks[i] == rChoice: continue
    tempComebacks.append(comebacks[i])
##choices.append(rChoice)

print("You are fighting an angry pirate!")
print("He insults you: '" + rInsult + "'")

##print(tempComebacks)
while choiceNum < 2:
    nChoice = random.choice(tempComebacks)
    choices.append(nChoice)
    tempComebacks.remove(nChoice)
    choiceNum += 1
##print(choices)
##print(tempComebacks)
##print(choices)
print(rChoice)
print(choices)
response = input("How will you respond?\n1. " + rChoice + "\n2. " + choices[0] + "\n3. " + choices[1])
