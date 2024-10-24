import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.ttk import Treeview

from Payroll.components.navigation_frame import navigation_frame
from Payroll.frames.dashboard import dashboard
from Payroll.frames.salaries import salaries


class App(Tk):
    def __init__(self):
        super().__init__()
        self.transaction_container = None
        self.container2 = None
        self.container1 = None
        self.title("Payroll Management System")
        self.head_label = "Dashboard"

        window_width = 1024
        window_height = 600

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.state("zoomed")
        image = Image.open("images/avatar.jpg")
        resize_image = image.resize((100,100))
        self.image = ImageTk.PhotoImage(resize_image)
        menubar = Menu(self)
        self.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Add menu items to the File menu
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Settings")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Add menu items to Help menu
        help_menu.add_command(label="Contact Developer")
        help_menu.add_command(label="Need Help Navigating")

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        header = tk.Frame(self, background="white")
        header.pack(fill=tk.X, ipady=10)
        Label(header, text=self.head_label,
              background="white",
              foreground="grey",
              font=("Helvatica", 12)
              ).pack(side=LEFT, padx=50)
        container = Frame(self)
        container.pack(fill=tk.BOTH, pady=5, expand=TRUE)
        navigation = Frame(container, width=250)
        navigation.pack(fill=tk.Y, side=LEFT)
        avatar = Label(navigation, image=self.image)
        avatar.pack(padx=50, pady=20)
        navigation_frame(navigation)
        # dashboard(container)
        salaries(container)


if __name__ == "__main__":
    app = App()
    app.mainloop()