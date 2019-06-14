from random import randint

#Create lists of choices for the excuse
who = ["my dog", "my cat", "my hamster", "my grandma","Yoshi", "Shrek", "The Principal"]

action = ["ate", "burned", "destroyed", "washed", "erased"]

assignment = ["my homework", "my PowerPoint", "my essay", "my math problems"]

#Random selection from each list
whoChoice = who[randint(0,len(who)-1)]
actionChoice = action[randint(0,len(action)-1)]
assignmentChoice = assignment[randint(0,len(assignment)-1)]

#print excuse
print(whoChoice + " " + actionChoice + " " + assignmentChoice)