from manim import *
from utils import *
class Modulo(Scene):
    def construct(self):     
        
        titulo = getAbsoluteValue()        
        titulo.scale(0.7).to_corner(UL)
        self.add(titulo)     
                
        definicao = getDefinition()
        definicao.center().shift(UP * 0.5)        
        
        self.play(Create(definicao),run_time=1)
        self.wait(3)
        
        self.play(definicao.animate.scale(0.7).to_corner(UR, buff=0.5))
        
        self.wait(3)