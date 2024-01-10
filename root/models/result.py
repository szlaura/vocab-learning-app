class Result(object):
    def __init__(self, total=None, score=None):
        self.total = total
        self.score = score
        self.percent = round((score / total) * 100, 2)
