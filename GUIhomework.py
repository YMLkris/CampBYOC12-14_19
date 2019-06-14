from random import randint
from guizero import App, Text

who = ["my dog", "my cat", "my hamster", "my grandma","Yoshi", "Shrek", "The Principal"]
action = ["ate", "burned", "destroyed", "washed", "erased"]
assignment = ["my homework", "my PowerPoint", "my essay", "my math problems"]

whoChoice = who[randint(0,len(who)-1)]
actionChoice = action[randint(0,len(action)-1)]
assignmentChoice = assignment[randint(0,len(assignment)-1)]

#print excuse
#print(whoChoice + " " + actionChoice + " " + assignmentChoice)

app = App(title="Homework Excuse Generator")

excuse = Text(app, text=whoChoice + " " + actionChoice + " " + assignmentChoice,size =20, color = 'blue' )

app.display()