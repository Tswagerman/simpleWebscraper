import os
import re
from re import search

from application import App 
from webScraperPython import WebScraper

def control():
	app.buildGUI()
	url = app.getURL()
	desired_Price = app.getDesiredPrice()
	if (desired_Price == ""):
		app.printText("The price input is not a valid desired price. Provide any number")
		control() #Resetting the GUI because nothing is entered
	app.clearText() #Clearing the red input error text
	if search("pricerunner.dk", url): 
		webscraper = WebScraper(desired_Price, url)
		try:
			print("try")
			webscraper.extractCurrentPrice()
		except:
			print("except")
			app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL with the item you want to track")
			control() #Resetting the GUI because the URL provided results in an exception
		else:
			app.destroy() #Close the window of the GUI
			if ((int(desired_Price) >= webscraper.current_Price)):
				webscraper.sendNotification()
			else:
				print("Not sending a notification, current price higher than desired price")
				return
			webscraper.saveToCSV()
			os._exit(1) #No exception is raised this way, and the program is terminated.
	else:
		app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL")
		control() #Resetting the GUI because the url is not remotely close to what the webscraper will expect.

if __name__ == "__main__":
	app = App()
	control()