import os
import re
import csv
from os import path
from re import search

from application import App 
from webScraper import WebScraper

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
			saveSettings(desired_Price, url)
			finalCheck(desired_Price, webscraper)
	else:
		app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL")
		control() #Resetting the GUI because the url is not remotely close to what the webscraper will expect.

def saveSettings(desired_Price, url):
	cwd = os.getcwd() #current working directory
	savePath = cwd + "\settings.csv"
	scraping_info = []
	scraping_info.append(desired_Price)
	scraping_info.append(url)
	with open(savePath, 'w', newline='\n') as file:
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
	if (path.exists("settings.csv")):
		with open("settings.csv") as csvFile:   #open the file
			CSVdata = csv.reader(csvFile, delimiter=',') 
			#for iteration, row in CSVdata:
			for row in CSVdata:
				desired_Price = row[0]
				url = row[1]
		csvFile.close()
		webscraper = WebScraper(desired_Price, url)
		webscraper.extractCurrentPrice()
		finalCheck(desired_Price, webscraper)
	else: #No prior settings will be used, the GUI will be prompted
		app = App()
		control()