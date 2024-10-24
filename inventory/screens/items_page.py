import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview


class App(Tk):
    def __init__(self):
        super().__init__()
        self.transaction_container = None
        self.container2 = None
        self.container1 = None
        self.title('Inventory')

        window_width = 1024
        window_height = 600

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.state("zoomed")

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        pos_header = tk.Frame(self, background="white")
        pos_header.pack(fill=tk.X, ipady=20)
        Label(pos_header, text="Item Inventory",
              background="white",
              foreground="grey",
              font=("Helvatica", 12)
              ).pack(side=LEFT, padx=50)
        self.pos_frame()

    def pos_frame(self):
        pos_container = Frame(self, background="white")
        self.container1 = Frame(pos_container, background="white")
        self.container2 = Frame(pos_container, background="#DDDDDD")
        search_entry = ttk.Combobox(self.container1)
        search_entry.pack(fill=tk.X, padx=30, pady=20)
        self.container1.pack(side=LEFT, fill=tk.Y)
        self.container2.pack(side=LEFT, fill=BOTH, expand=True, padx=30, pady=20)
        Label(self.container2,
              text="Transactions",
              font=("Helvatica", 14),
              foreground="#35374B",
              background="#dddddd").pack(fill=tk.X)
        self.transaction_container = Frame(self.container2, background="#DDDDDD")
        self.transaction_container.pack(expand=True, fill=BOTH, padx=10)




if __name__ == "__main__":
    app = App()
    app.mainloop()
