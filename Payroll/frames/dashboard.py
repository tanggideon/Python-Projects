import tkinter as tk
from tkinter import *
from tkinter import ttk


def dashboard(master):
    dashboard_frame = Frame(master, background="white")
    dashboard_frame.pack(fill=tk.BOTH, expand=TRUE, side=RIGHT)
    display_information = Frame(dashboard_frame, height=200, background="white")
    display_information.pack(fill=tk.X)
    payment_information = Frame(display_information, width=320, height=190)
    payment_information.pack(side=LEFT, padx=25, pady=5, fill=tk.Y, expand=TRUE)
    staff_information = Frame(display_information, width=320, height=190)
    staff_information.pack(side=LEFT, padx=25, pady=5, fill=tk.Y, expand=TRUE)
    other_information = Frame(display_information, width=320, height=190)
    other_information.pack(side=LEFT, padx=25, pady=5, fill=tk.Y, expand=TRUE)
    tables = Frame(dashboard_frame, background="white")
    tables.pack(fill=tk.BOTH, expand=TRUE)
    summary_header = Frame(tables, background="white")
    summary_header.pack(fill=tk.X)
    Label(summary_header, text="Payment Summary",
          background="white",
          foreground="grey",
          font=("Helvatica", 12)).pack(side=LEFT, padx=25, pady=10)
    summary_table = Frame(tables, width=690)
    summary_table.pack(fill=tk.Y, side=LEFT, padx=25)
    summary_piechart = Frame(tables, width=350)
    summary_piechart.pack(fill=tk.Y, side=LEFT)