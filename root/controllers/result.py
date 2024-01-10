class ResultController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["result"]
