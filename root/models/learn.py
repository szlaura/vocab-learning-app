from root.models.main import Model


class LearnModel(Model):
    def __init__(self, vocabulary=None, random_foreign_word="", random_base_word="", hinter="", hint_count=0,
                 result=None):
        super().__init__()
        if vocabulary is None:
            vocabulary = []
        self.vocabulary = vocabulary
        self.random_foreign_word = random_foreign_word
        self.random_base_word = random_base_word
        self.hinter = hinter
        self.hint_count = hint_count
        self.result = result
