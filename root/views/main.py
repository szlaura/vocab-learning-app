from typing import TypedDict
from .root import Root
from .home import HomeView
from .learn import LearnView
from .end import EndView


class Frames(TypedDict):
    learn: LearnView
    home: HomeView
    end: EndView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._add_frame(EndView, "end")
        self._add_frame(LearnView, "learn")
        self._add_frame(HomeView, "home")

    def _add_frame(self, frame, name: str) -> None:
        self.frames[name] = frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
