from tkinter import Frame, Label, Button, Entry


class LearnView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Learn")
        self.header.grid(row=0, column=0, padx=10, pady=10)

        # ------------

        self.foreign_word = Label(self, text="", font=("Arial", 28))
        self.foreign_word.grid(row=0, column=1, padx=10, pady=10)

        self.answer_label = Label(self, text="")
        self.answer_label.grid(row=1, column=1, padx=10, pady=20)

        self.my_entry = Entry(self, font=("Arial", 18))
        self.my_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create Buttons

        self.answer_button = Button(self, text="Answer")
        self.answer_button.grid(row=3, column=0, padx=20)

        self.next_button = Button(self, text="Next")
        self.next_button.grid_forget()

        self.hint_button = Button(self, text="Hint")
        self.hint_button.grid(row=3, column=1, padx=20)

        # # Create Hint Label
        self.hint_label = Label(self, text="")
        self.hint_label.grid(row=4, column=1, padx=20)
