# 1. Merge all of the various files from people posted on the discussion board into a single file with a Python script.
def Mergeall():
    male = []
    female = []
# Read in all the txt files classified by male and female
    for i in range(1,18):
        with open('female'+str(i)+'.txt','r') as f:
            female.extend([(item) for item in (f)])
            
    for i in range(1,18):
        with open('male'+str(i)+'.txt','r') as m:
            male.extend([(item) for item in (m)])
# Format the items
    for i,item in enumerate(female):
        if item[0] == 'A':
            female[i] = "She's " + item
            
    for i,item in enumerate(male):
        if item[0] != 'H':
            male[i] = "He's " + item
# Return the results
    all = male + female
    return all, male, female

# 2. finds the best and worst character of each gender (based on sentiment analysis) and groups them together into the original format of the joke
from textblob import TextBlob

def Bestworst(male, female):
    sentimale = []
    sentifemale = []
# Calculate sentiment for each items
    for i,item in enumerate(male):
        sentimale.append(TextBlob(item).sentiment[0])
    for i,item in enumerate(female):
        sentifemale.append(TextBlob(item).sentiment[0])
# Find out the best and worst items
    bestfemale = female[sentifemale.index(max(sentifemale))]
    worstfemale = female[sentifemale.index(min(sentifemale))]
    bestmale = male[sentimale.index(max(sentimale))]
    worstmale = male[sentimale.index(min(sentimale))]
# Groups them together into the original format of the joke
    best = bestmale + bestfemale
    worst = worstmale + worstfemale + 'They fight crime!'
# Return the results
    return best, worst

# 3. finds the 10 most common descriptions for characters
from collections import Counter

def mostcommon(male, female):
# Merge all the descriptions together
    description = []
    for i,item in enumerate(male):
        description.extend(item.split(' ')[2:4])
    for i,item in enumerate(female):
        description.extend(item.split(' ')[3:5])
# Count the most common 10 descriptions
    C = Counter(description)
# Return the results
    return [word for word,cnt in C.most_common(10)]

# Run the scripts
all, male, female = readfile()
best, worst = Bestworst(male, female)
mostcommon = mostcommon(male, female)

