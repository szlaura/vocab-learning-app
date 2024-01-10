from root.models.main import Model


class LearnModel(Model):
    def __init__(self, random_foreign_word="", random_base_word="", hinter="", hint_count=0):
        super().__init__()
        self.random_foreign_word = random_foreign_word
        self.random_base_word = random_base_word
        self.hinter = hinter
        self.hint_count = hint_count

        @property
        def random_foreign_word(self):
            return self._random_foreign_word

        @random_foreign_word.setter
        def random_foreign_word(self, value):
            self._random_foreign_word = value

        @property
        def random_base_word(self):
            return self._random_base_word

        @random_base_word.setter
        def random_base_word(self, value):
            self._random_base_word = value

        @property
        def hinter(self):
            return self._hinter

        @hinter.setter
        def hinter(self, value):
            self._hinter = value

        @property
        def hint_count(self):
            return self._hint_count

        @hint_count.setter
        def hint_count(self, value):
            self._hint_count = value
