# 🐍 This is the Python code linked to your Dash

# 🔄 Code here is executed at each restart of the app

# 📍 This is the place where you set the initial state of your app...

name = ""
counter = 0

# ...and define functions that return data to be displayed...
def get_greeting():
    text = "# Welcome to your first Dash 🎉\n"

    if name: 
        text += f"## Nice meeting you, {name}!\n"

    return text

def get_button_label():
    if counter == 0:
        return "Click me!"

    return f"You've clicked the button {counter} times!"

# ...or that handle user input
def increment():
    global counter
    counter += 1


# 🔗 Everything defined here is available to use on the Layout Editor
