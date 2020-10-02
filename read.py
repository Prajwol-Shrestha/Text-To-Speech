from tkinter import *
import pyttsx3
from tkinter import filedialog

window = Tk()
window.title("Text to Speech")
window.geometry("440x300")
window.configure(background = "Black")


Heading = Label(window, text = "Text To Speech Converter", font = ('Bold',25), fg = "white", bg = "black")
Heading.grid(column = 1, row = 0, columnspan = 3,pady = 20)

def choosefile():
	global filepath
	#----------Getting Filepath-------
	filepath = filedialog.askopenfilename()

def read():
	#-------Opening File Path------
	file = open(filepath , 'r')
	#-------Initializing function-------
	engine = pyttsx3.init()
	#-------If Given Input = True Try Block--- Otherwise except Block----
	try:
		 engine.setProperty('rate', int(Set_speed.get()))
	except:
		engine.setProperty('rate', 130)

	#-------Speaking contents Inside the file		
	engine.say(file.read())
	engine.runAndWait()

	file.close()

# ---------Recommended Label----------
recommended = Label(window, text = "Recommended Speed : 130 ", font = 20, fg = "white", bg = "black")
recommended.grid(column= 1 , row = 1 ,columnspan = 2,pady = 10)

#----------Setting Speech Speed Label--------
setspeed = Label(window, text = "Set Speech Speed ", font = 20, fg = "white", bg = "black")
setspeed.grid(column= 0 , row = 2 ,columnspan = 2, padx= 10)

#----------Setting Speech Speed --------
Set_speed = Entry(window, width = 25, font = 20,bd = 3, fg = "white", bg = "black")
Set_speed.grid(column = 2, row = 2, pady = 10, columnspan = 2)


#----------Choose File------------
choose_file = Button(window, text  = "Choose File", command = choosefile , padx = 20,pady = 5, bd= 5, font = 20, fg = "white", bg = "black")
choose_file.grid(row = 4,column = 2,pady = 10)

#----------Start Reading Button ----------
Open = Button(window, text = "Start Reading", command = read , padx = 20,pady = 5, bd= 5, font = 20, fg = "white", bg = "black")
Open.grid(row = 5, column = 2 ,pady = 10, padx = 20)

window.mainloop()