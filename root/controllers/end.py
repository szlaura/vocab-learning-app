from root.models.main import Model
from root.views.main import View


class EndController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["end"]
