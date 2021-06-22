import tkinter as tk

class PasswordPrompt:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas1 = tk.Canvas(self.window, width = 180, height = 100,  relief = 'raised')
        self.entryPassword = tk.Entry(self.window, show="*", width=15)
        self.buttonConfirmEntry = tk.Button(text='Confirm password', command=self.confirm, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        self.password = ""
        
    def buildGUI(self):
        self.window.title('Password prompt')
        self.window.geometry("200x200")
        self.window.resizable("true", "true")
        self.canvas1.pack()
        self.canvas1.create_text(90,20,fill="darkblue",font=('helvetica', 9, 'bold'),
                        text="Enter password")
        self.canvas1.create_window(90, 50, window=self.entryPassword) #password entrybox
        self.entryPassword.focus() #Type immediatly, withou moving mouse
        self.window.bind('<Return>', self.confirm) #Pressing enter will confirm the password 
        self.window.mainloop()

    def setPassword(self):
        self.password = self.entryPassword.get()

    def getPassword(self):
        return self.password

    def confirm(self, event):
        self.setPassword()
        self.window.quit()

    def printText(self, message):
        self.canvas1.create_text(90,70,fill="red",font=('helvetica', 7, 'bold'),text=message, tag="print_text")

    def clearText(self):
        self.canvas1.delete("print_text")

    def destroy(self):
        print("Destroying GUI")
        self.window.destroy() 