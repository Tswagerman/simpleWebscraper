import tkinter as tk

class PasswordPrompt:
    def __init__(self, sender_email):
        self.window = tk.Tk()
        self.canvas1 = tk.Canvas(self.window, width = 250, height = 100,  relief = 'raised')
        self.entryPassword = tk.Entry(self.window, show="*", width=15)
        self.buttonConfirmEntry = tk.Button(text='Confirm password', command=self.__confirm, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        
        self.password = ""
        self.sender_email = sender_email
        
    def buildGUI(self):
        self.__openWindow()

        self.canvas1.pack()
        self.canvas1.create_text(125,20,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter password for")
        self.canvas1.create_text(125,50,fill="darkblue",font=('helvetica', 9, 'bold'), text=str(self.sender_email))
        self.canvas1.create_window(125, 80, window=self.entryPassword) #password entrybox

        self.entryPassword.focus() #Type immediatly, without moving mouse to entrybox
        self.window.bind('<Return>', self.__confirm) #Pressing enter will confirm the password, no need to press the button 

        self.window.mainloop()

    def __openWindow(self):
        self.window.title('Password prompt')
        self.window.geometry("250x100")
        self.window.resizable("true", "true")
        self.window.attributes("-topmost", True)
        
    def __setPassword(self):
        self.password = self.entryPassword.get()

    def getPassword(self):
        return self.password

    def __confirm(self, event):
        self.__setPassword()
        self.window.quit()

    def printText(self, message):
        self.canvas1.create_text(90,70,fill="red",font=('helvetica', 7, 'bold'),text=message, tag="print_text")

    def clearText(self):
        self.canvas1.delete("print_text")

    def destroy(self):
        print("Destroying GUI")
        self.window.destroy() 