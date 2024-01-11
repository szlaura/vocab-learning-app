class ResultModel(object):
    def __init__(self, total=0, score=0):
        self.total = total
        self.score = score
        if total > 0:
            self.percent = round((score / total) * 100, 2)
        else:
            self.percent = 0
