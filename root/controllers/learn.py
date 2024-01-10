import pandas as pd
from random import randint

from root.decorators.countcalls import count_calls
from root.models.learn import LearnModel
from root.views.main import View


def get_random_vocab_number(input_vocab):
    count = len(input_vocab)
    random_num = randint(0, count - 1)
    return random_num


def get_vocabulary():
    data = pd.read_excel(r"D:\LAURA\SZTE_MSC\Applications\Oslo\vocab-learning-app\spanish.xlsx")
    df = pd.DataFrame(data, columns=["foreign", "base"])
    vocabulary = df.values.tolist()
    return vocabulary


class LearnController:
    def __init__(self, model: LearnModel, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["learn"]
        self._bind()
        get_vocabulary()
        self.go_next()

    def _bind(self) -> None:
        self.frame.answer_button.config(command=lambda: [self.show_answer(), self.show_next_btn()])
        self.frame.next_button.config(command=self.go_next)
        self.frame.hint_button.config(command=self.add_hint)

    def show_answer(self):
        if self.frame.my_entry.get().lower() == self.model.random_base_word.lower():
            self.frame.answer_label.config(
                text=f"Correct! The word {self.model.random_foreign_word} means {self.frame.my_entry.get()}.",
                fg="green")
        else:
            self.frame.answer_label.config(
                text=f"Incorrect! The word {self.model.random_foreign_word} is not {self.frame.my_entry.get()}.",
                fg="red")

    def add_hint(self):
        hinter = self.model.hinter
        hint_count = self.model.hint_count

        if hint_count < len(self.model.random_base_word):
            hinter = hinter + self.model.random_base_word[hint_count]
            self.set_hinter(hinter)
            self.frame.hint_label.config(text=hinter)
            self.set_hint_count(hint_count + 1)

    @count_calls
    def go_next(self):

        actual_vocabulary = get_vocabulary()
        # Clear the screen
        self.frame.answer_label.config(text="")
        self.frame.my_entry.delete(0, 'end')
        self.frame.hint_label.config(text="")
        self.frame.next_button.grid_forget()
        # Reset Hint stuff
        self.set_hinter("")
        self.set_hint_count(0)
        random_num = get_random_vocab_number(actual_vocabulary)
        actual_foreign_word = actual_vocabulary[random_num][0]
        self.set_random_foreign_word(actual_foreign_word)
        self.frame.foreign_word.config(text=actual_foreign_word)

        actual_base_word = actual_vocabulary[random_num][1]
        self.set_random_base_word(actual_base_word)

    def show_next_btn(self):
        self.frame.next_button.grid(row=3, column=2, padx=10, pady=10)

    def set_random_foreign_word(self, actual_random_word):
        self.model.random_foreign_word = actual_random_word
        return self.model.random_foreign_word

    def set_random_base_word(self, actual_random_word):
        self.model.random_base_word = actual_random_word
        return self.model.random_base_word

    def set_hinter(self, actual_hinter_string):
        self.model.hinter = actual_hinter_string
        return self.model.hinter

    def set_hint_count(self, actual_hint_count):
        self.model.hint_count = actual_hint_count
        return self.model.hint_count
