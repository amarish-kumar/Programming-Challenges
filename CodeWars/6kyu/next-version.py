###############################################################################################
## CodeWars - Next Version                                                                   ##
##      Rank: 6-kyu                                                                          ##
##                                                                                           ##
## https://www.codewars.com/kata/next-version/train/python                                   ##
##                                                                                           ##
## You're fed up about changing the version of your software manually. Instead, you will     ##
## create a little script that will make it for you.                                         ##
##                                                                                           ##
## ==== Exercise ====                                                                        ##
## Create a function nextVersion, that will take a string in parameter, and will return a    ##
## string containing the next version number.                                                ##
##                                                                                           ##
## For example:                                                                              ##
##                                                                                           ##
## nextVersion("1.2.3") === "1.2.4";                                                         ##
## nextVersion("0.9.9") === "1.0.0.";                                                        ##
## nextVersion("1") === "2";                                                                 ##
## nextVersion("1.2.3.4.5.6.7.8") === "1.2.3.4.5.6.7.9";                                     ##
## nextVersion("9.9") === "10.0";                                                            ##
##                                                                                           ##
## ==== Rules ====                                                                           ##
## All numbers, except the first one, must be lower than 10: if there are, you have to set   ##
## them to 0 and increment the next number in sequence.                                      ##
##                                                                                           ##
## You can assume all tests inputs to be valid.                                              ##
###############################################################################################

def next_version(version):
    # Split vals into ints
    s = version.split ('.')
    
    length = len (s)
    
    for i in range (0, length):
        s[i] = int (s[i])

    for i in range (length - 1, -1, -1):
        # If the value we are currently on (also entry value) is to be rolled over
        if (s[i] >= 9 and i != 0):
            s[i] = 0 
        # If value is under 9
        else:
            s[i] += 1
            break
         
    st = ""
    for num in s:
       st += str (num) + "."
       
    return st[:-1]