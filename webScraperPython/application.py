import tkinter as tk

class App:
	def __init__(self):
		self.window = tk.Tk()
		self.canvas1 = tk.Canvas(self.window, width = 400, height = 300,  relief = 'raised')
		self.entryURL = tk.Entry (self.window)
		self.buttonURL = tk.Button(text='Confirm URL', command=self.setURL, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
		self.url = ""

	def buildGUI(self):
		self.window.title('Pricerunner webscraper')
		self.window.geometry("600x600")
		self.window.resizable("true", "true")
		self.canvas1.pack()
		self.canvas1.create_window(200, 140, window=self.entryURL)
		self.canvas1.create_window(200, 180, window=self.buttonURL)
		self.window.mainloop()

	def setURL(self):
		self.url = self.entryURL.get()
		print(self.url)
		self.window.quit()
		
	def getURL(self):
		return self.url

	def destroy(self):
		self.window.destroy() 
		