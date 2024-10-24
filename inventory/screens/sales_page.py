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
        self.title('Sales Page')

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
        sales_header = Frame(self, background="white")
        sales_header.pack(fill=tk.X, ipady=20)
        Label(sales_header, text="Sales Analysis",
              background="white",
              foreground="grey",
              font=("Helvatica", 12)
              ).pack(side=LEFT, padx=50)
        self.sales_analysis_frame = Frame(self, background="white")
        self.sales_analysis_frame.pack(expand=True, fill=BOTH, pady=5)
        self.sales_analysis()

    def sales_analysis(self):
        container = Frame(self.sales_analysis_frame, background="white")
        container.pack(fill=BOTH, expand=True, padx=30)
        sales_frame = Frame(container, background="blue", width=300)
        sales_frame.pack(fill=BOTH, expand=True, side=LEFT)
        sales_summary_frame = Frame(container, background="#dddddd")
        sales_summary_frame.pack(fill=BOTH, expand=True, side=LEFT)


if __name__ == "__main__":
    app = App()
    app.mainloop()