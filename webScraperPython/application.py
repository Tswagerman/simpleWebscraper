import tkinter as tk

#Private methods are preceded by __
class App:
	def __init__(self): 
		self.window = tk.Tk()
		self.canvas1 = tk.Canvas(self.window, width = 600, height = 300,  relief = 'raised')
		self.entryURL = tk.Entry (self.window)
		self.entryDesiredPrice = tk.Entry (self.window)
		self.buttonConfirmEntry = tk.Button(text='Confirm entered values', command=self.__confirm2, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
		self.buttonConfirmItems = tk.Button(text='Confirm final item', command=self.confirmAllItems, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

		reg = self.window.register(self.__callback)
		self.entryDesiredPrice.config(validate="key", validatecommand=(reg, '%P'))

		self.url = ""
		self.desiredPrice = 0
		self.receiver_email = ""
		self.number_of_items = 0
		self.itemsConfirmed = False

	def buildGUI(self):
		self.__openWindow()

		self.canvas1.pack()
		self.canvas1.create_text(150,60,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter a pricerunner item URL.")
		self.canvas1.create_window(150, 100, window=self.entryURL) #URL entrybox

		self.canvas1.create_text(400,60,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter a desired price.")
		self.canvas1.create_window(400, 100, window=self.entryDesiredPrice) #Desired price entrybox

		#self.canvas1.create_text(275,140,fill="darkblue",font=('helvetica', 9, 'bold'), text="Press confirm after filling in the URL and desired price")
		self.canvas1.create_window(275, 160, window=self.buttonConfirmEntry) #Button to confirm entered values

		#self.canvas1.create_text(275,180,fill="darkblue",font=('helvetica', 9, 'bold'), text="Press this button only when adding the final item.")
		self.canvas1.create_window(275, 210, window=self.buttonConfirmItems) #Button to stop the restarting of the GUI,
																			 #making this the last item added to the settings
		self.canvas1.create_text(275,250,fill="darkblue",font=('helvetica', 12, 'bold'), text="Press the upper button to coninue to add more items.")
		self.canvas1.create_text(275,270,fill="darkblue",font=('helvetica', 12, 'bold'), text="Press the lower button to finalize the list.")
		self.entryURL.focus() #Type immediatly, without moving mouse to entrybox
		self.window.bind('<Return>', self.__confirm1) #Pressing enter will confirm the entered values, no need to press the button 

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

	def __confirm1(self, event):
		self.__setURL()
		self.__setDesiredPrice()
		self.window.quit()

	def __confirm2(self): #overloeaded method
		self.__setURL()
		self.__setDesiredPrice()
		self.window.quit()

	def confirmAllItems(self):
		self.__confirm2()
		print("CONFIRM BUTTON PRESSED")
		self.itemsConfirmed = True

	def printText(self, message):
		self.canvas1.create_text(275,20,fill="red",font=('helvetica', 12, 'bold'), text=message, tag="print_text")

	def clearText(self):
		self.canvas1.delete("print_text")

	def destroy(self):
		self.window.destroy() 