from bs4 import BeautifulSoup, SoupStrainer
import requests
import csv
import re
import datetime 
import getpass #secrets (hint: ******)!
import smtplib, ssl #sendNotification
import os

from application import App 
from re import search

class WebScraper:
	def __init__(self, desired_price, url):
		self.current_Price = 0
		self.desired_Price = desired_price
		self.url = url
		#WebScraper.main(self) 

	#def main(self):
		#url = "https://www.pricerunner.dk/pl/126-5049980/Analoge-kameraer/Fujifilm-Instax-Mini-Film-20-pack-Sammenlign-Priser"
		
	def extractCurrentPrice(self):
		page = requests.get(self.url) 
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		data = soup.findAll('span', attrs={'currency':'DKK'})
		#The lowest price is the first item found on the website with the corresponding attributes
		self.current_Price = data[0].text.strip() 
		self.current_Price = re.sub(r'[aA-zZ]+', '', self.current_Price, re.I) 
		self.current_Price = int(self.current_Price.replace(".", ""))	
	
	def sendNotification(self):
		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = "devthomasswagerman@gmail.com"  # Enter your address
		receiver_email = "devthomasswagerman@gmail.com"  # Enter receiver address
		print('Sending from ', sender_email)
		password = getpass.getpass("Type your password and press enter: ")
		message = f"ALERT ALERT, BUY YOUR SHINY STUFF. IT IS CHEAP!! \nCurrent Price: {self.current_Price} \nDesired Price: {self.desired_Price}"
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message)
			print("Email has been sent to ", receiver_email)

	def saveToCSV(self):
		print("Saving for history purposes")
		mydate = datetime.datetime.now().strftime('%d %b %Y - %H:%M')	#add date, so history is build up.
		csvdata = 'Price = ' + str(self.current_Price) + ', Date = ' + str(mydate)
		cwd = os.getcwd() #current working directory
		savePath = cwd + "\data.csv"
		with open(savePath, 'a', newline='\n') as file:
			mywriter = csv.writer(file, delimiter=',')
			mywriter.writerow([csvdata]) #the [] are there to make sure the entire string is saved as one.

def control():
	app.buildGUI()
	url = app.getURL()
	desired_Price = app.getDesiredPrice()
	if (desired_Price == ""):
		app.printText("The price input is not a valid desired price. Provide any number")
		control() #Resetting the GUI
	app.clearText() #Clearing the red input error text
	if search("pricerunner.dk", url): 
		webscraper = WebScraper(desired_Price, url)
		try:
			print("try")
			webscraper.extractCurrentPrice()
		except:
			print("except")
			app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL with the item you want to track")
			control() #Resetting the GUI
		else:
			app.destroy() #Close the window of the GUI
			if ((int(desired_Price) >= webscraper.current_Price)):
				webscraper.sendNotification()
			else:
				print("Not sending a notification, current price higher than desired price")
				#return
			webscraper.saveToCSV()
			os._exit(1) #No exception is raised this way, and the program is terminated.
	else:
		app.printText("The input is not a valid URL. Provide a 'pricerunner.dk' URL")
		control() #Resetting the GUI

if __name__ == "__main__":
	app = App()
	control()


