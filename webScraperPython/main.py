import os
import re
import csv
from os import path
from re import search

from application import App 
from webScraper import WebScraper

def control(): #This method checks whether the input that is given to the GUI is information that can be used.
	app.buildGUI()
	url = app.getURL()
	desired_Price = app.getDesiredPrice()
	app.clearText() #Clearing the red input error text

	if (desired_Price == ""):
		app.printText("The price input is not a valid desired price. Provide any number")
		control() #Resetting the GUI because nothing is entered in the desired price input box
	
	if search("pricerunner.dk", url): 
		webscraper = WebScraper(desired_Price, url)
		try:
			webscraper.extractCurrentPrice()
		except:
			app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL with the item you want to track")
			control() #Resetting the GUI because the URL provided results in an exception
		else:
			#saveSettings(desired_Price, url)
			finalCheck(desired_Price, webscraper)
			app.destroy() #Close the window of the GUI
	else:
		app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL")
		control() #Resetting the GUI because the url is not remotely close to what the webscraper will expect.

def saveSettings(desired_Price, url):
	cwd = os.getcwd() #current working directory
	savePath = cwd + "\data\settings.csv"
	scraping_info = []
	scraping_info.append(desired_Price)
	scraping_info.append(url)
	if (path.exists("settings.csv")):
		with open(savePath, 'a', newline='\n') as file: #append the scraping info to an existing file
			writer = csv.writer(file)
			writer.writerow(scraping_info)
	else:
		with open(savePath, 'w', newline='\n') as file: #Create file and write to the new file
			writer = csv.writer(file)
			writer.writerow(scraping_info)

def finalCheck(desired_Price, webscraper):
	if ((int(desired_Price) >= webscraper.current_Price)):
		webscraper.sendNotification()
		webscraper.saveToCSV()
	else:
		print("Not sending a notification, current price higher than desired price")
	os._exit(1) #No exception is raised this way, and the program is terminated.

if __name__ == "__main__":
	#if statement: No initial GUI prompt is necessary, because the user already indicated their preferences.
	#These preferences are saved in the seetings file
	if (path.exists("settings.csv")): 
		with open("settings.csv") as csvFile:  
			CSVdata = csv.reader(csvFile, delimiter=',') 
			#for iteration, row in CSVdata:
			for row in CSVdata:
				desired_Price = row[0]
				url = row[1]
		csvFile.close()
		webscraper = WebScraper(desired_Price, url)
		webscraper.extractCurrentPrice()
		finalCheck(desired_Price, webscraper)
	#No prior settings will be used, the GUI will be prompted
	else: 
		app = App()
		control()