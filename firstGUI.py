from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size=slider_value



app = App("Hello World!", width=300, height=500)

welcome_message = Text(app, text="Welcome to my GUI!", size=40, color='red', font='Piboto')

my_name = TextBox(app)

update_text = PushButton(app, command=say_my_name, text="Press to Display Text")

text_size = Slider(app, command=change_text_size, start=10, end=80)

my_image = Picture(app, image="hamster.gif",)

app.display()


