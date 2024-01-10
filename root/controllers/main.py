from root.controllers.home import HomeController
from root.controllers.learn import LearnController
from root.controllers.result import ResultController
from root.models.main import Model
from root.views.main import View


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.learn_controller = LearnController(model, view)
        self.result_controller = ResultController(model, view)
        self.home_controller = HomeController(model, view)

    def start(self):
        self.view.start_mainloop()
