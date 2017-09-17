# Python 3.5

def wordify (hours, minutes):
    outBuffer = ""

    # h o' clock
    if (minutes == 0):
        print ("%s o' clock" % numDict [hours])
    # quarter past h
    elif (minutes == 15):
        print ("quarter past %s" % numDict [hours])
    # m minutes past h
    elif (minutes < 30):
        print ("%s minutes past %s" % (numDict [minutes], numDict [hours]))
    # half past h
    elif (minutes == 30):
        print ("half past %s" % numDict [hours])
    # quarter to h + 1
    elif (minutes == 45):
        print ("quarter to %s" % numDict [hours + 1])
    # 60 - m minutes to h + 1
    elif (minutes > 30):
        print ("%s minutes to %s" % (numDict [60 - m], numDict [hours + 1]))

def populateNumDict ():
    numDict [1] = "one"
    numDict [2] = "two"
    numDict [3] = "three"
    numDict [4] = "four"
    numDict [5] = "five"
    numDict [6] = "six"
    numDict [7] = "seven"
    numDict [8] = "eight"
    numDict [9] = "nine"
    numDict [10] = "ten"
    numDict [11] = "eleven"
    numDict [12] = "twelve"
    numDict [13] = "thirteen"
    numDict [14] = "fourteen"
    numDict [15] = "fithteen"
    numDict [16] = "sixteen"
    numDict [17] = "seventeen"
    numDict [18] = "eighteen"
    numDict [19] = "nineteen"
    numDict [20] = "twenty"
    numDict [21] = "twenty one"
    numDict [22] = "twenty two"
    numDict [23] = "twenty three"
    numDict [24] = "twenty four"
    numDict [25] = "twenty five"
    numDict [26] = "twenty six"
    numDict [27] = "twenty seven"
    numDict [28] = "twenty eight"
    numDict [29] = "twenty nine"

import sys

numDict = dict ()
numKeys = dict ()

h = int (input ())
m = int (input ())

populateNumDict ()
wordify (h, m)
