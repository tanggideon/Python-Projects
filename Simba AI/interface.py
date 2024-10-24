import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from tkinter.ttk import Treeview


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simba AI")

        window_width = 1024
        window_height = 600

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # Zoom the window on startup and set window icon
        self.state("zoomed")
        self.iconbitmap(r"images/icon.ico")
        image = Image.open("images/simba.jpg")
        self.image = ImageTk.PhotoImage(image.resize((120, 120)))

        # Icons
        simba_ai = Image.open("images/simba.png")
        sentiment_analyzer = Image.open("images/sentiment_analyzer.png")
        text_categorizer = Image.open("images/text_categorization.png")

        self.simba_ai = ImageTk.PhotoImage(simba_ai.resize((50, 50)))
        self.sentiment_analyzer = ImageTk.PhotoImage(sentiment_analyzer.resize((50, 50)))
        self.text_categorization = ImageTk.PhotoImage(text_categorizer.resize((50, 50)))

        container = Frame(self, background="white")
        container.pack(fill=BOTH)
        Label(container, text="Welcome to Simba AI",
              background="white",
              foreground="grey",
              font=("Helvatica", 12)
              ).pack(side=LEFT, padx=50, pady=20)
        user_avatar = Frame(container, background="White")
        user_avatar.pack(side=RIGHT, padx=50)
        spaced_font = font.Font(family="Helvatica", size=11, weight="bold")
        Label(user_avatar, text="Gideon Tang", background="white", font=spaced_font, foreground="grey").pack()

        menu_frame = Frame(self, background="white")
        menu_frame.pack(pady=20)

        logo_frame = Frame(menu_frame, width=600, background="White")
        logo_frame.pack(ipady=20, fill=tk.X, pady=10)
        logo = Label(logo_frame, image=self.image)
        logo.pack(padx=50, pady=20)
        Label(logo_frame, text="Simba AI", background="white", font=("Helvatica", 14, "bold"), foreground="grey").pack()
        Label(logo_frame, text="Powered by OpenAi", background="white", font=("Helvatica", 12, "bold"), foreground="grey").pack()

        button_frame = Frame(menu_frame, background="white")
        button_frame.pack(fill=tk.X)
        sentiment_analyzer = Button(button_frame, text="Sentiment Analyzer", image=self.sentiment_analyzer, compound="top", background="white", font=("Helvatica", 12, "bold"), foreground="grey")
        text_categorization = Button(button_frame, text="Text Categorization", image=self.text_categorization, compound="top", background="white", font=("Helvatica", 12, "bold"), foreground="grey")
        simba_gpt = Button(button_frame, text="Simba AI", background="white", image=self.simba_ai, compound="top", font=("Helvatica", 12, "bold"), foreground="grey")
        sentiment_analyzer.pack(side=LEFT, ipady=30, ipadx=50, pady=10, padx=10)
        text_categorization.pack(side=LEFT, ipady=30, ipadx=50, pady=10, padx=10)
        simba_gpt.pack(side=LEFT, ipady=30, ipadx=50, pady=10, padx=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()