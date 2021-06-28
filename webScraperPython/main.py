import os
import re
import csv
from os import path
from re import search

from application import App 
from webScraper import WebScraper

def control(): #This function checks whether the input that is given to the GUI is information that can be used.
	app.buildGUI()
	url = app.getURL()
	desired_Price = app.getDesiredPrice()
	receiver_email = app.getReceiver_email()
	app.clearText() #Clearing the red input error text
	checkEmail(app, receiver_email)
	if (desired_Price == ""):
		app.printText("The price input is not a valid desired price. Provide any number.")
		control() #Resetting the GUI, because nothing is entered in the desired price input box
	if search("pricerunner.dk", url): 
		webscraper = WebScraper(desired_Price, url, receiver_email)
		try:
			webscraper.extractCurrentPrice()
		except:
			app.printText("Provide a 'pricerunner.dk' URL corresponding to an item.")
			control() #Resetting the GUI, because the provided URL results in an exception
		else:
			saveSettings(desired_Price, url, receiver_email)
			finalCheck(webscraper)
			if (app.itemsConfirmed == True): #When the 'confirm items' button is pressed, the program is terminated after reaching this part of the control loop
				app.destroy() #Close the entire GUI
				os._exit(1) #No exception is raised this way, and the program is terminated.
			else:
				control()
	else:
		app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL.")
		control() #Resetting the GUI because the url is not remotely close to what the webscraper will expect.

def checkEmail(app, receiver_email):
	#Regular expression to validate email
	regex_email = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
	print(receiver_email)
	if (re.search(regex_email, receiver_email)):#(confirmation_mail -> accepted)
		print("The email is valid")
	else:
		app.printText("The email does not seem to be valid")
		control()

def saveSettings(desired_Price, url, receiver_email):
	cwd = os.getcwd() #Current working directory
	savePath = cwd + "\data\settings.csv"
	scraping_info = []
	scraping_info.append(desired_Price)
	scraping_info.append(url)
	scraping_info.append(receiver_email)
	if (path.exists("data\settings.csv")):
		with open(savePath, 'a', newline='\n') as file: #Append the scraping info to an existing file
			writer = csv.writer(file)
			writer.writerow(scraping_info)
	else:
		with open(savePath, 'w', newline='\n') as file: #Create file and write to the new file
			writer = csv.writer(file)
			writer.writerow(scraping_info)

def finalCheck(webscraper):
	if ((webscraper.current_Price) <= int(webscraper.desired_Price)):
		webscraper.sendNotification()
		webscraper.saveToCSV()
	else:
		print("Not sending a notification, current price higher than desired price.")

def usingSettings():
	with open("data\settings.csv") as csvFile:  
		CSVdata = csv.reader(csvFile, delimiter=',') 
		for row in CSVdata:
			desired_Price = row[0]
			url = row[1]
			receiver_email = row[2]
			webscraper = WebScraper(desired_Price, url, receiver_email)
			webscraper.extractCurrentPrice()
			finalCheck(webscraper)
	csvFile.close()

if __name__ == "__main__":
	#if statement: No initial GUI prompt is necessary, because the user already indicated their preferences.
	#These preferences are saved in the '\data\settings.csv' file
	if (path.exists("data\settings.csv")): 
		usingSettings()		
	#No prior settings will be used, the GUI will be prompted
	else: 
		app = App()
		control()