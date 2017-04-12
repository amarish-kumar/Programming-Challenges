###############################################################################################
## CodeWars - What's wrong with these identifiers?                                           ##
##      Rank: 8-kyu                                                                          ##
##                                                                                           ##
## https://www.codewars.com/kata/whats-wrong-with-these-identifiers/train/python             ##
##                                                                                           ##
## An identifier is simply a name...                                                         ##
##                                                                                           ##
## Can you amend this object so that it's properties comprise of valid identifiers?          ##
###############################################################################################

##### Provided Code ####

# Person = {
#  1stname: "John",
#  second-name: "Doe",
#  email@ddress: "john.doe@email.com",
#  male.female: "M"
#}

# Person is a simple dictionary; make the keys into strings makes them valid
Person = {
    "1stname": "John",
    "second-name": "Doe",
    "email@address": "john.doe@email.com",
    "male.female": "M"
}