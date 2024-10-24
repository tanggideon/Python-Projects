import tkinter as tk
from tkinter import *
from tkinter import ttk


def navigation_frame(master):
    navigation_frame = Frame(master=master)
    navigation_frame.pack(fill=tk.BOTH, expand=TRUE)
    dashboard_button = ttk.Button(navigation_frame, text="Dashboard")
    dashboard_button.pack(fill=tk.X, ipady=10)
    analytics_button = ttk.Button(navigation_frame, text="Analytics")
    analytics_button.pack(fill=tk.X, ipady=10)
    staff_button = ttk.Button(navigation_frame, text="Staff")
    staff_button.pack(fill=tk.X, ipady=10)
    salary_button = ttk.Button(navigation_frame, text="Salaries and Advances")
    salary_button.pack(fill=tk.X, ipady=10)
    summary_button = ttk.Button(navigation_frame, text="Summaries")
    summary_button.pack(fill=tk.X, ipady=10)
    settings_button = ttk.Button(navigation_frame, text="Settings")
    settings_button.pack(fill=tk.X, ipady=10)

    logout_frame = Frame(master)
    logout_frame.pack(fill=tk.X)
    logout_button = ttk.Button(logout_frame, text="Logout")
    logout_button.pack(fill=tk.X, ipady=5)
