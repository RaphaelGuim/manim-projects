from manim import *

class GradientColor(Scene):
    def construct(self):
        square = Square().set_fill(color=[BLUE, GREEN, YELLOW, RED],opacity=0.8)
         
        self.play(Create(square))
        self.wait(3)
       