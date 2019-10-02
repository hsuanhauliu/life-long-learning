# Disclaimer: the examples below were taken directly from thenewboston's
# tutorial series on Youtube. I merely followed his videos and re-formatted
# the code so that it is easier to skim through.
#
# This file only contains content from his first 8 videos in the series.
#
# This file aims to showcase some of the capabilities Tkinter has to offer.
# The program contains several examples instead of just one for convenience.
# 
# Thanks to thenewboston for his wonderful tutorial series on this subject.
# See the link below to find his video.
# https://www.youtube.com/watch?v=RJB1Ek2Ko_Y

from tkinter import *

print('Creating the first example window...')
# First we create a Tk object. This is the GUI window. Initially empty
root = Tk()

# Add texts
label_1 = Label(root, text='Wow this is so...')  # create a string of text
label_1.pack()  # put it somewhere in the window where it can fit
label_2 = Label(root, text='COOL!', bg='red', fg='black')
label_2.pack(fill=X)
label_3 = Label(root, text='options:', bg='blue', fg='white')
label_3.pack(side=LEFT, fill=Y)

# Frame create a container for other objects
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Here we can create some buttons and place them in the frames
button1 = Button(topFrame, text='Button 1', fg='red')  # create custom buttons
button2 = Button(topFrame, text='Button 2', fg='blue')
button3 = Button(topFrame, text='Button 3', fg='green')
button4 = Button(bottomFrame, text='Button 4', fg='purple')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

# Open the window and keep it open until the user exists
root.mainloop()


# The second example shows how we can create texts fields using Tkinter
print('Creating the second example window...')
root_2 = Tk()

label_1 = Label(root_2, text='Name')
label_2 = Label(root_2, text='Password')

# Create two text fields
entry_1 = Entry(root_2)
entry_2 = Entry(root_2)

# Use grid to organize the objects
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

# We can also create a widget like so
c = Checkbutton(root_2, text='Keep me logged in')
c.grid(columnspan=2)

root_2.mainloop()


# Third example: tie functions to buttons
print('Creating the third example window...')
root_3 = Tk()

# First method
def printSomething():
    print('Hello!')

button_1 = Button(root_3, text='Print something', command=printSomething)
button_1.pack()

# Second method
def printMoreThings(event):
    print('Heyoooo!')

button_2 = Button(root_3, text='Print more things')
button_2.bind('<Button-1>', printMoreThings)
button_2.pack()

root_3.mainloop()


# Fourth example: detect different events
print('Creating the fourth example window...')
root_4 = Tk()

def leftClick(event):
    print('Left')

def middleClick(event):
    print('Middle')

def rightClick(event):
    print('Right')

window = Frame(root_4, width=300, height=250)
window.bind('<Button-1>', leftClick)
window.bind('<Button-2>', middleClick)
window.bind('<Button-3>', rightClick)
window.pack()

root_4.mainloop()


# Final example: create a class to organize functionalities of an object
print('Creating the fifth example window...')
class ButtonClass:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Print Message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('Hello from the other side~')

root_5 = Tk()
button = ButtonClass(root_5)
root_5.mainloop()
