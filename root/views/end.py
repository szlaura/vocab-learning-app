from tkinter import Frame, Label


class EndView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="You have improved your vocabulary today!", font=("Arial", 20))
        self.header.grid(row=1, column=0, padx=10, pady=10)
