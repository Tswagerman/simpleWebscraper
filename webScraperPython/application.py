import tkinter as tk

class App:
	def __init__(self):
		self.window = tk.Tk()
		self.canvas1 = tk.Canvas(self.window, width = 1000, height = 300,  relief = 'raised')
		self.entryURL = tk.Entry (self.window)
		self.entryDesiredPrice = tk.Entry (self.window)
		reg=self.window.register(self.callback)
		self.entryDesiredPrice.config(validate="key", validatecommand=(reg, '%P'))
		self.buttonConfirmEntry = tk.Button(text='Confirm Entered values', command=self.confirm, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
		self.url = ""
		self.desiredPrice = 0

	def buildGUI(self):
		print("Building GUI")
		self.window.title('Pricerunner webscraper')
		self.window.geometry("600x600")
		self.window.resizable("true", "true")
		self.canvas1.pack()
		self.canvas1.create_text(150,100,fill="darkblue",font=('helvetica', 9, 'bold'),
                        text="Enter a pricerunner item URL below.")
		self.canvas1.create_window(150, 140, window=self.entryURL) #URL entrybox
		self.canvas1.create_text(400,100,fill="darkblue",font=('helvetica', 9, 'bold'),
                        text="Enter a desired price for the item below.")
		self.canvas1.create_window(400, 140, window=self.entryDesiredPrice) #Desired price entrybox
		self.canvas1.create_text(275,200,fill="darkblue",font=('helvetica', 10, 'bold'),
                        text="Press confirm after filling in the URL and desired price")
		self.canvas1.create_window(275, 240, window=self.buttonConfirmEntry) #Button to confirm entered values
		self.window.mainloop()

	def setURL(self):
		print("Setting URL")
		self.url = self.entryURL.get()
		print(self.url)
		
	def getURL(self):
		print("Getting URL")
		return self.url

	def setDesiredPrice(self):
		print("Setting desired price")
		self.desiredPrice = self.entryDesiredPrice.get()
		print(self.desiredPrice)
		
	def getDesiredPrice(self):
		print("Getting desired price")
		return self.desiredPrice
	
	def callback(self, input):
		print("Calling callback")
		if input.isdigit():
			print(input)
			return True
		elif input is "":
			print("Enter a value for the desired price")
			return True
		else:
			print(input)
			return False

	def confirm(self):
		self.setURL()
		self.setDesiredPrice()
		self.window.quit()

	def printText(self, message):
		self.canvas1.create_text(275,275,fill="red",font=('helvetica', 12, 'bold'),
                        text=message, tag="print_text")

	def clearText(self):
		self.canvas1.delete("print_text")

	def destroy(self):
		self.window.destroy() 
		