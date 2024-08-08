'''

This is a note for Module 2 of Python Basics. 
This is a Multi-line String comment. 

LESSON 6: Python Strings


'''
#Making a String and copying/trying to change it

orig = "Python"

newst = orig[0] + "i" + orig[2: ]

print(orig) #Python

print(newst) #Pithon
print()

#Strings are immumtable. You can't make changes. You must make a new string variable
#--------> orig[1] = "i" #This would raise a Type Error

#-----------------------------------------------------------------------------------------------------
#Indexing to access characters in a String
t = "coders"
first_letter = t[1:4]
print(first_letter)

#Use negative to access last character
second_last = t[-2]
print(second_last)

lastcharcter = t[-1]
print(lastcharcter)
print()

#-----------------------------------------------------------------------------------------------------
#Iterating -- Repetitive execution of the same block of code over and over is referred to as iteration. 
#Definite iteration, in which the number of repetitions is specified explicitly in advance. (for Python -- For Loops)
#Indefinite iteration, in which the code block executes until some condition is met. (for Python -- While loops)

track = "Marathon"

for char in track:
    print(char, end= ' ') #the (,end = ' ') -- makes it print with a space
print()
print()

#-----------------------------------------------------------------------------------------------------
#Iterating -- Slicing -- “Slicing” means getting a subset of elements from an iterable based on their indices
field = "Touchdown"
playone = field[0:5]
playtwo = field[5: ]
playthree = field[2::2] #Start from third character and get every second character


print(playone)
print(playtwo)
print(playthree) #Start from third character and get every second character (u h o n)
print()

game_plan = "Execute play number 9"
#to focus on 'play number 9'
for word in game_plan[8:]:
    print(word, end=' ')
    
print()
print()

#-----------------------------------------------------------------------------------------------------
#String Concatenation -- String concatenation means add strings together or joining two or more strings together and forming one single string
quarterback = "Tom"
receiver = "Jerry"
play = " runs a route to catch the pass from "

complete_play = quarterback + play + receiver
print(complete_play)

#---------------- -- # can only concatenate strings (str) not with integer (int)

players = ["Python", "is", "great", "for", "string", "manipulation"]
team_statement = ""
for word in players:
    print(team_statement)
    team_statement += word + " "

print(team_statement.strip())
print()

#-----------------------------------------------------------------------------------------------------
#String Formatting -- It is the process of inserting a custom string or variable in predefined text.
celebration = "{} scores a touchdown and does the {} dance!"

touchdwncelb = celebration.format("Tom", "moonwalk")
print(touchdwncelb)

#F-string
player = "Tom"
action = "touchdown"
celebration_move = "moonwalk"

playcall = f"{player} scores a {action} and does the {celebration_move}!"
print(playcall)
print()

#-----------------------------------------------------------------------------------------------------
#Built-in Functions

#len() function -- returns the number of items in an object.
field_length = "Football field"
field_side = len(field_length)
print(f"The length of the string is: {field_side}")

#upper() function -- returns a string where all characters are in upper case.
#lower() function --  returns a string where all characters are lower case.
chant = "Go team!"
loudchant = chant.upper()
quietchant = chant.lower()
print(loudchant)
print(quietchant)

#replace() function -- method replaces a specified phrase with another specified phrase.
gp = "Attack from the left flank"
print(gp)
newgp = gp.replace("left", "right")
print(newgp)

#strip() function --  method removes any leading, and trailing whitespaces.
playername = "  Ronaldo  "
clean_name = playername.strip()
print(f"'{clean_name}' is ready to play!")

#join() function -- method takes all items in an iterable and joins them into one string.
#split() function -- method splits a string into a list.
chant = "Here we go, team, here we go!"
words = chant.split(",")
newchant = " ".join(words)
print(words)
print(newchant)




