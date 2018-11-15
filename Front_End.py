from tkinter import *
from PIL import Image, ImageTk
#import os
import BG
import p1
import p
#import tkFont

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("DRDO Multi Surveillance Drone")
		self.pack(fill = BOTH, expand = YES)
		
		runButton = Button(self, text="Background substraction", command = self.run_file, bg = "#ff3300", activebackground = "#00ff99")
		runButton.place(height = 50, width = 200, x = 50, y = 540)

		runButton1 = Button(self, text="Identify Objects", command = self.pooja, bg = "#ff3300", activebackground = "#00ff99")
		runButton1.place(height = 50, width = 200, x = 50, y = 600)

		quitButton1 = Button(self, text="Count People", command = self.count, bg = "#ff3300")
		quitButton1.place(height = 50, width = 200,x = 350, y = 540)
		
		quitButton = Button(self, text="Exit", command = self.client_exit, bg = "#ff3300")
		quitButton.place(height = 50, width = 200,x = 350, y = 600)
		
		self.showImg()
		
		menu = Menu(self.master)
		self.master.config(menu = menu)

		file = Menu(menu)
		file.add_command(label = 'Background substraction', command = self.run_file)
		file.add_command(label = 'Identify Objects', command = self.pooja)
		file.add_command(label = 'Exit', command = self.client_exit)
		menu.add_cascade(label = 'File', menu = file)

		edit = Menu(menu)
		edit.add_command(label = 'About', command = self.about_app)
		edit.add_command(label = 'Team', command = self.showTxt)
		menu.add_cascade(label = 'Edit', menu = edit)

	def client_exit(self):
		print("Exit")
		exit()

	def run_file(self):
		BG.main()

	def pooja(self):
		p.main()

	def count(self):
		p1.main()

	def showImg(self):
		load = Image.open('pic1.png')
		render = ImageTk.PhotoImage(load)

		img = Label(self, image = render)
		img.image = render
		img.place(x = 50, y=20, height = 500, width = 500)

	def showTxt(self):
		text = Label(self, text = 'Apurv | Aakash | Aishwary | Pooja | Shrikant')	
		text.pack()

	def about_app(self):
		text = Label(self, text = 'This application is developed by IIIT NR Students as a part of Project of DRDO DRUSE')	
		text.pack()


root = Tk()
root.geometry("600x700")
app = Window(root)
root.mainloop()
