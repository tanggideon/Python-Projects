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
        self.title('Point of Service')

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
        navigation_frame = tk.Frame(self, background='blue')
        navigation_frame.pack(ipady=10, fill=tk.X)
        pos_header = tk.Frame(self, background="white")
        pos_header.pack(fill=tk.X, ipady=10)
        Label(pos_header, text="Point of Service",
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

        self.transactions()
        pos_container.pack(fill=tk.BOTH, expand=True, pady=5, ipady=50)
        self.pos_table()
        price_frame = Frame(self.container1, background="#DDDDDD")
        price_frame.pack(fill=tk.X, ipady=10, padx=30)
        Label(price_frame, text="Total:",
              foreground="#35374B",
              background="#DDDDDD",
              font=("Helvatica", 14)).pack(side=LEFT, padx=10)
        controls = Frame(self.container1, background="white")
        controls.pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(controls, text="Checkout").pack(side=RIGHT)
        ttk.Button(controls, text="Save Cart").pack(side=RIGHT, padx=20)
        ttk.Button(controls, text="Clear").pack(side=RIGHT)

    def pos_table(self):
        headers = ("serial_no", "item_name", "quantity", "price")
        tree = Treeview(self.container1, columns=headers, show='headings')
        tree.heading('serial_no', text='S/N')
        tree.column('serial_no', width=50)
        tree.heading('item_name', text='Item Name')
        tree.column('item_name', width=300)
        tree.heading('quantity', text='Quantity')
        tree.column('quantity', width=150)
        tree.heading('price', text='Price')
        tree.column('price', width=150)
        s = ttk.Style()
        s.configure('Treeview', rowheight=40)

        return tree.pack(padx=30)

    def transactions(self):
        for item in range(10, 0, -1):
            self.transaction_item(item)
    
    def transaction_item(self, serial):
        item_frame = Frame(self.transaction_container, background="white")
        item_frame.pack(fill=tk.X, pady=5)
        Label(item_frame, text=str(serial),
              width=2,
              background="white",
              foreground="#35374B",
              font=("Helvatica", 10)).pack(fill=tk.Y, ipady=10, ipadx=20, side=LEFT)
        description_frame = Frame(item_frame, background="white", width=350)
        description_frame.pack(fill=tk.Y, ipadx=20, side=LEFT)
        controls = Frame(item_frame, background="white")
        controls.pack(fill=BOTH, padx=20, expand=True)
        ttk.Button(controls, text="View").pack(side=RIGHT)
        ttk.Button(controls, text="Edit").pack(side=RIGHT, padx=5)
        id_frame = Frame(description_frame, background="white")
        id_frame.pack(fill=tk.X)
        Label(id_frame, text="pos-12345678-200324",
              font=("Helvatica", 10),
              background="white",
              foreground="grey").pack(side=LEFT)
        others_frame = Frame(description_frame, background="white")
        others_frame.pack(fill=tk.X)
        price_frame = Frame(others_frame, background="white")
        price_frame.pack(side=LEFT, fill=tk.Y)
        Label(price_frame, text="Price: ",
              background="white",
              foreground="#35374B").pack(side=LEFT, padx=20)
        Label(price_frame, text="200.00",
              font=("Helvatica", 12),
              background="white",
              foreground="#35374B").pack(side=LEFT)
        status_frame = Frame(others_frame, background="white")
        status_frame.pack(side=RIGHT)
        Label(status_frame, text="Status: ", background="white", foreground="#35374B").pack(side=LEFT)
        Label(status_frame, text="Completed",
              background="white",
              font=("Helvatica", 12),
              foreground="#35374B").pack(side=RIGHT)


if __name__ == "__main__":
    app = App()
    app.mainloop()
