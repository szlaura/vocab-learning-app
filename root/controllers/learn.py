from tkinter import messagebox
from root.models.learn import LearnModel
from root.models.result import ResultModel
from root.views.main import View
from root.services.file_handler import get_vocabulary
from root.services.calculate import get_random_vocab_number


class LearnController:
    def __init__(self, model: LearnModel, view: View) -> None:
        self.model = model
        self.model.vocabulary = get_vocabulary()
        self.model.result = ResultModel()
        self.view = view
        self.frame = self.view.frames["learn"]
        self._bind()
        self.go_next()

    def _bind(self) -> None:
        self.frame.answer_button.config(command=lambda: [self.manage_iterations(), self.check_answer(),
                                                         self.show_next_btn()])
        self.frame.next_button.config(command=self.go_next)
        self.frame.hint_button.config(command=self.add_hint)

    def manage_iterations(self):
        vocab_iterations = 5
        if self.model.result.total >= vocab_iterations:
            messagebox.showinfo("Result", f"Your score is {self.model.result.score} "
                                          f"out of {self.model.result.total}, "
                                          f"which is {self.model.result.percent}%.")
            self.view.switch("end")

    def check_answer(self):
        answer_input = self.frame.input_answer.get()
        base_word = self.model.random_base_word
        foreign_word = self.model.random_foreign_word

        if answer_input.lower() == self.model.random_base_word.lower():
            self.frame.answer_label.config(text=f"Correct! The word {foreign_word} means {answer_input}.", fg="green")
            self.set_result(self.model.result.total + 1, self.model.result.score + 1)

        else:
            self.frame.answer_label.config(text=f"Incorrect! The word {base_word} is not {answer_input}.", fg="red")
            self.set_result(self.model.result.total + 1, self.model.result.score + 0)

    def add_hint(self):
        hinter = self.model.hinter
        hint_count = self.model.hint_count

        if hint_count < len(self.model.random_base_word):
            hinter = hinter + self.model.random_base_word[hint_count]
            self.set_hinter(hinter)
            self.frame.hint_label.config(text=hinter)
            self.set_hint_count(hint_count + 1)

    def go_next(self):
        actual_vocabulary = self.model.vocabulary

        self.clear_frame()

        random_num = get_random_vocab_number(actual_vocabulary)
        actual_foreign_word = actual_vocabulary[random_num][0]
        self.set_random_foreign_word(actual_foreign_word)
        self.frame.foreign_word.config(text=actual_foreign_word)

        actual_base_word = actual_vocabulary[random_num][1]
        self.set_random_base_word(actual_base_word)

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

    def set_result(self, total, score):
        self.model.result = ResultModel(total, score)

    def show_next_btn(self):
        self.frame.next_button.grid(row=6, column=0, padx=10, pady=10)

    def clear_frame(self):
        self.frame.foreign_word.config(text="")
        self.frame.answer_label.config(text="")
        self.frame.hint_label.config(text="")
        self.frame.input_answer.delete(0, 'end')
        self.frame.next_button.grid_forget()

        self.set_hinter("")
        self.set_hint_count(0)
