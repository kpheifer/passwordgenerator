# This is a password generator written in Python3

import tkinter as tk
import random

# GUI Stuff
window = tk.Tk()
window.title("Password Generator")
window.geometry('1000x800')

# Top text
label = tk.Label(window, text="This is a password generator. Enter in a length for your password and then press the button below to generate a completely random password.")
label.pack()

# Text box 
text_box = tk.Entry(window)
text_box.pack()

# Password Label
pass_display = tk.Label(window, text = '')

# Strings containing all of the characters
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
special = '`~!@#$%^&*()-_=+\|]}[{;:,<>./?'

# Reset the list to contain all characters
def reset_list(): 
    # Create lists containing the individual characters from the strings
    lowercase_list = list(lowercase)
    uppercase_list = list(uppercase)
    nums_list = list(nums)
    special_list = list(special)
    
    # Create a new set containing the sets
    global charlist
    charlist = [lowercase_list, uppercase_list, nums_list, special_list]

    # Shuffle the elements of each list in the charlist variable
    for li in charlist: 
        random.shuffle(li)

# Get random list
def generate_list():
    random.shuffle(charlist)
    return random.choice(charlist)

# Get random char from a list
def generate_char(): 

    # Shuffle the charlist variable
    random.shuffle(charlist)

    # Get a random character set from the charlist variable
    characterset = random.choice(charlist)

    # Return a random character from the character set
    return random.choice(characterset)

# Generates the random password
def generate_password(passleng):
    
    # Shuffle for increased variance
    reset_list() 
    random.shuffle(charlist)

    # Generate password
    password = None
    if passleng == 0: 
        password = "Invalid length input"
        pass_display.configure(foreground='red')
    else: 
        pass_display.configure(foreground='green')
        for i in range(1,passleng+1):
            if password is None: 
                password = generate_char()
            else: 
                password += generate_char()     

    return(password)

# Function that calls on the random password function when the button is pressed
def button_clicked():

    # Check if input is an int
    try:
        passleng = int(text_box.get())
    except ValueError:
        passleng = 0

    # Generate pass
    password = generate_password(passleng)

    # Display pass
    pass_display.configure(text = password)
    pass_display.pack()

# Making the generate button
button = tk.Button(window, text="Enter", command=button_clicked)
button.pack()

# Main Function
if __name__ == "__main__":
    window.mainloop()