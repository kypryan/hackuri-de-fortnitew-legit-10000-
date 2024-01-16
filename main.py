import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Fortnite Hacks Store", font=("Arial", 25))
        self.label.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.label = tk.Label(self.root, text="Insert your account username, password and credit card details", font=("Arial", 10))
        self.label.pack(padx=10, pady=10)

        self.textBox = tk.Text(self.root, height=5, font=("Arial", 25))
        self.textBox.bind("<KeyPress>", self.shortcut)
        self.textBox.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text="Sell Your Soul? *", font=("Arial", 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.label = tk.Label(self.root, text="* Selling your soul is not optional and required to continue, also this allows us to posses you, making you our puppet thet we can use to take over the world. Your money left in your bank accont will also be used to fund our conquest", font=("Arial", 7))
        self.label.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, text="BUY",font=("Arial", 15), command=self.showMessage)
        self.button1.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()



    def showMessage(self):
        if self.check_state.get() == 0:
            print(self.textBox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Purchase complete", message=self.textBox.get("1.0", tk.END))

    def on_closing(self):
        if messagebox.askyesno(title="Quit", message="Are you sure? If you quit we will kidnap your family"):
            messagebox.showinfo(title="really?", message="Nice try. We will still kidnap you family for even thinking to quit")

    def shortcut(self, event):
        print (event)

MyGUI()