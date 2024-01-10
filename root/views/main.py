from typing import TypedDict
from .root import Root
from .home import HomeView
from .learn import LearnView
from .result import ResultView


class Frames(TypedDict):
    learn: LearnView
    result: ResultView
    home: HomeView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(LearnView, "learn")
        self._add_frame(ResultView, "result")
        self._add_frame(HomeView, "home")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
