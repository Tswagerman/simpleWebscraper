import tkinter as tk
from tkinter import messagebox
import os

#Private methods are preceded by __
class App:
	def __init__(self): 
		self.window = tk.Tk()
		self.canvas1 = tk.Canvas(self.window, width = 600, height = 300,  relief = 'raised')
		self.entryURL = tk.Entry (self.window)
		self.entryDesiredPrice = tk.Entry (self.window)
		self.entryReceiverEmail = tk.Entry (self.window)
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
		#Text & URL entrybox
		self.canvas1.create_text(150,60,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter a pricerunner item URL.")
		self.canvas1.create_window(150, 100, window=self.entryURL) 
		#Text & Desired price entrybox
		self.canvas1.create_text(400,60,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter a desired price.")
		self.canvas1.create_window(400, 100, window=self.entryDesiredPrice) 
		#Text & Receiver email entrybox
		self.canvas1.create_text(275,20,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter the email you want to be notified at.")
		self.canvas1.create_window(275, 40, window=self.entryReceiverEmail)
		#Button to confirm entered values and to continue to the next item.
		self.canvas1.create_window(275, 200, window=self.buttonConfirmEntry) 
		#Button to stop the restarting of the GUI, making this the last item added to the settings.
		self.canvas1.create_window(275, 230, window=self.buttonConfirmItems)
		self.canvas1.create_text(275,260,fill="darkblue",font=('helvetica', 12, 'bold'), text="Press the upper button to coninue to add more items.")
		self.canvas1.create_text(275,280,fill="darkblue",font=('helvetica', 12, 'bold'), text="Press the lower button to finalize the list.")

		self.entryURL.focus() #Type immediatly, without moving mouse to entrybox
		self.window.bind('<Return>', self.__confirm1) #Pressing enter will confirm the entered values, no need to press the button 
		
		self.window.protocol("WM_DELETE_WINDOW", self.__on_closing)
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

	def __setReceiverEmail(self):
		self.receiver_email = self.entryReceiverEmail.get()
		
	def getReceiver_email(self):
		return self.receiver_email
	
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
		self.__setReceiverEmail()
		self.window.quit()

	def __confirm2(self): #Python does not support overloading, hence this method name convention
		self.__setURL()
		self.__setDesiredPrice()
		self.__setReceiverEmail()
		self.window.quit()

	def confirmAllItems(self):
		self.__confirm2()
		print("CONFIRM BUTTON PRESSED")
		self.itemsConfirmed = True

	def printText(self, message):
		self.canvas1.create_text(275,150,fill="red",font=('helvetica', 12, 'bold'), text=message, tag="print_text")

	def clearText(self):
		self.canvas1.delete("print_text")

	def __on_closing(self):
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			self.destroy()
			os._exit(1)

	def destroy(self):
		self.window.destroy() 