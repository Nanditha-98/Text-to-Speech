from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from ttkthemes import ThemedStyle
from gtts import *
from playsound import playsound
# Tk()       : to initialize tkinter which will be used for GUI
# geometry( ): to set the width and height of the windowPP
# configure(): to access window attributes
# bg         :set the color of the background
# title()    : set the title of the window

# Window is initialised
# root is the name which we refer to our window

root = tk.ThemedTk()
root.geometry('400x300')
root.configure(bg='ghost white')
root.title('TEXT TO SPEECH')

style = ThemedStyle(root)
style.theme_use("kroc")

# Label() widget is used to display one or more than one line of text that users can’t able to modify.


# text which we display on the label
# font in which the text is written
# pack organized widget in block
# Msg is a string type variable
# Entry() used to create an input text field
# textvariable used to retrieve the current text to entry widget
# place() organizes widgets by placing them in a specific position in the parent widget

# heading
Label(root, text = 'Convert your Texts to Speech' , font='Times 20 bold' , bg ='white smoke').pack()
Label(root, text ='Enter Text', font ='Helvetica 15 bold', bg ='white smoke').place(x=20,y=60)

# text variable
Msg = StringVar()

# Input
# Entry(): accept single-line text strings from a user
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Speech.mp3')
    playsound('Speech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Buttons
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech,width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)

# infinite loop to run program
root.mainloop()

