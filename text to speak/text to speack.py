from tkinter import *
from tkinter import ttk
from pyttsx3.drivers import sapi5

root = Tk()
mainframe = ttk.Frame(root, padding="30 30 32 32")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

variable1 = StringVar()  # Value saved here


def submit():
    import pyttsx3
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # convert this text to speech
    text = variable1.get()
    print(text)
    engine.say(text)
    # play the speech
    engine.runAndWait()



ttk.Entry(mainframe, width=50, textvariable=variable1).grid(column=2, row=1)



ttk.Label(mainframe, text="Text to voice").grid(column=1, row=1)

ttk.Button(mainframe, text="speak", command=submit).grid(column=2, row=13)



root.mainloop()