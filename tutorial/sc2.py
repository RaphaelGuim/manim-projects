from manim import *

class FormasBasicas(Scene):
    def construct(self):
        # Criar formas
        quadrado = Square(side_length=2, color=BLUE)
        circulo = Circle(radius=1, color=RED)
        triangulo = Triangle(color=GREEN).scale(1.5)
        
        # Posicionar as formas
        quadrado.to_edge(LEFT)         
        triangulo.to_edge(RIGHT)
        
        # Mostrar as formas
        self.play(Create(quadrado))
        self.play(Create(circulo))
        self.play(Create(triangulo))
        
        # Transformações
        self.play(
            quadrado.animate.rotate(PI/4),
            circulo.animate.set_fill(RED, opacity=0.5),
            triangulo.animate.shift(DOWN)
        )
        
        
        self.wait(1)