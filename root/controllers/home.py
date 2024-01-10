from root.models.main import Model
from root.views.main import View


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        self.frame.learn_btn.config(command=self.start_learn)

    def start_learn(self):
        self.view.switch("learn")
