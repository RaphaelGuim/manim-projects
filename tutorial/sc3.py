from manim import *

class TextoEFormulas(Scene):
    def construct(self):
        # Texto simples
        texto = Text("Isso é um texto normal", font="Arial")
        
        # Fórmula matemática
        formula = MathTex(r"e^{i\pi} + 1 = 0")
        
        # Organizando verticalmente
        # buff The gap between grid cells
        grupo = VGroup(texto, formula).arrange(DOWN, buff=1)
        
        # Animação
        self.play(Write(texto))
        self.wait(1)
        self.play(Write(formula))
        self.wait(1)