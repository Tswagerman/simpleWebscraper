import tkinter as tk

#Private methods are preceded by __
class PasswordPrompt:
    def __init__(self, sender_email):
        self.window = tk.Tk()
        self.canvas1 = tk.Canvas(self.window, width = 250, height = 140,  relief = 'raised')
        self.entryPassword = tk.Entry(self.window, show="*", width=15)
        self.password = ""
        self.sender_email = sender_email
        
    def buildGUI(self):
        self.__openWindow()

        self.canvas1.pack()
        self.canvas1.create_text(125,20,fill="darkblue",font=('helvetica', 9, 'bold'), text="Enter password for")
        self.canvas1.create_text(125,30,fill="darkblue",font=('helvetica', 9, 'bold'), text=str(self.sender_email))
        self.canvas1.create_window(125, 60, window=self.entryPassword) #password entrybox

        self.window.focus_set()
        self.entryPassword.focus() #Type immediatly, without moving mouse to entrybox
        self.window.bind('<Return>', self.__confirmEnter) #Pressing enter will confirm the password, no need to press the button 

        self.window.mainloop()

    def __openWindow(self):
        self.window.title('Password prompt')
        self.window.geometry("250x140")
        self.window.resizable("true", "true")
        self.window.attributes("-topmost", True)
        
    def __setPassword(self):
        self.password = self.entryPassword.get()

    def getPassword(self):
        return self.password

    def __confirmEnter(self, event):
        self.__setPassword()
        self.window.quit()

    def printText(self, message):
        self.canvas1.create_text(125,120,fill="red",font=('helvetica', 7, 'bold'),text=message, tag="print_text")

    def clearText(self):
        self.canvas1.delete("print_text")

    def destroy(self):
        self.window.destroy() 