import tkinter as tk
from tkinter import *
from tkinter import ttk


def salaries(master):
    file_export_type = tk.StringVar()
    salary_frame = Frame(master, background="white")
    salary_frame.pack(fill=tk.BOTH, expand=TRUE, side=RIGHT)
    header = Frame(salary_frame, background="white")
    header.pack(fill=tk.X, ipady=5)
    Label(header, text="Salary and Advances",
          background="white",
          foreground="grey",
          font=("Helvatica", 12)).pack(side=LEFT, padx=25, pady=10)
    export_frame = Frame(header, background="white")
    export_frame.pack(side=RIGHT, padx=25, pady=10)
    file_type_combo = ttk.Combobox(export_frame, textvariable=file_export_type)
    file_type_combo["values"] = ["PDF", "Excel", "CSV"]
    file_type_combo["state"] = "readonly"
    file_type_combo.pack(side=LEFT)
    export_button = ttk.Button(export_frame, text="Export")
    export_button.pack(side=RIGHT, ipady=2, ipadx=4, padx=5)