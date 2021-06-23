import tkinter as tk

#I chose for a class representation, because this allows me to visually encapsulate methods.
#To make clear which methods are meant to be used outside of this class. Private methods are preceded by __
class App:
	def __init__(self): 
		self.window = tk.Tk()
		self.canvas1 = tk.Canvas(self.window, width = 600, height = 300,  relief = 'raised')
		self.entryURL = tk.Entry (self.window)
		self.entryDesiredPrice = tk.Entry (self.window)
		self.buttonConfirmEntry = tk.Button(text='Confirm Entered values', command=self.__confirm, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

		reg = self.window.register(self.__callback)
		self.entryDesiredPrice.config(validate="key", validatecommand=(reg, '%P'))

		self.url = ""
		self.desiredPrice = 0
		self.receiver_email = ""
		self.number_of_items = 0

	def buildGUI(self):
		self.__openWindow()

		self.canvas1.pack()
		self.canvas1.create_text(150,100,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter a pricerunner item URL.")
		self.canvas1.create_window(150, 140, window=self.entryURL) #URL entrybox

		self.canvas1.create_text(400,100,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter a desired price.")
		self.canvas1.create_window(400, 140, window=self.entryDesiredPrice) #Desired price entrybox

		self.canvas1.create_text(275,200,fill="darkblue",font=('helvetica', 9, 'bold'), text="Press confirm after filling in the URL and desired price")
		self.canvas1.create_window(275, 240, window=self.buttonConfirmEntry) #Button to confirm entered values

		self.entryURL.focus() #Type immediatly, without moving mouse to entrybox
		self.window.bind('<Return>', self.__confirm) #Pressing enter will confirm the entered values, no need to press the button 

		self.window.mainloop()

	def __openWindow(self):
		self.window.title('Pricerunner webscraper')
		self.window.geometry("600x300")
		self.window.resizable("true", "true")

	def __setURL(self):
		self.url = self.entryURL.get()
		
	def getURL(self):
		return self.url

	def __setDesiredPrice(self):
		self.desiredPrice = self.entryDesiredPrice.get()
		
	def getDesiredPrice(self):
		return self.desiredPrice
	
	def __callback(self, input):
		if input.isdigit():
			return True
		elif input is "": #This is necessary in order to delete the complete input from the desired price entrybox
			return True
		else:
			return False

	def __confirm(self, event):
		self.__setURL()
		self.__setDesiredPrice()
		self.window.quit()

	def __confirm(self): #overloeaded method
		self.__setURL()
		self.__setDesiredPrice()
		self.window.quit()

	def printText(self, message):
		self.canvas1.create_text(275,275,fill="red",font=('helvetica', 12, 'bold'), text=message, tag="print_text")

	def clearText(self):
		self.canvas1.delete("print_text")

	def destroy(self):
		self.window.destroy() 