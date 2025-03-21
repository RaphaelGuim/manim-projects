from manim import *

from utils import getAbsoluteValue

class Modulo(Scene):
    def construct(self):     
        
         
        titulo = getAbsoluteValue()
        
        titulo.scale(0.7).to_corner(UL)
        self.add(titulo)
        
        
        
         # Criar as equações
        eq1 = MathTex(r"|", r"-3", r"| = 3")
        eq1[1].set_color(RED)  # Colore o "-3" em vermelho
        
        eq2 = MathTex(r"|", r"-1", r"| = 1")
        eq2[1].set_color(RED)
        
        eq3 = MathTex(r"|", r"-3.14", r"| = 3.14")
        eq3[1].set_color(RED)
        
        eq4 = MathTex(r"|", r"-\pi", r"| = \pi")
        eq4[1].set_color(RED)
        
        # Agrupar equações em uma VGroup
        equacoes = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, buff=0.5)
        
        # Posicionar as equações no lado esquerdo
        equacoes_esquerda = equacoes.copy().to_edge(LEFT, buff=1.5).shift(DOWN)
        
        # Criar equivalentes no lado direito com valores positivos
        eq1_dir = MathTex(r"|", r"7", r"| = 7")
        eq1_dir[1].set_color(BLUE)  # Colore o "7" em azul

        eq2_dir = MathTex(r"|", r"2", r"| = 2")
        eq2_dir[1].set_color(BLUE)

        eq3_dir = MathTex(r"|", r"1.9", r"| = 1.9")
        eq3_dir[1].set_color(BLUE)

        eq4_dir = MathTex(r"|", r"\phi", r"| = \phi")
        eq4_dir[1].set_color(BLUE)

        # Agrupar equações do lado direito
        equacoes_direita = VGroup(eq1_dir, eq2_dir, eq3_dir, eq4_dir).arrange(DOWN, buff=0.5)
        
        # Posicionar as equações no lado direito
        equacoes_direita.to_edge(RIGHT, buff=1.5).shift(DOWN)
        
        # Adicionar as equações à cena
        self.play(Write(equacoes_esquerda), run_time=3)
        self.play(Write(equacoes_direita), run_time=3)
        
        self.wait(2)
        self.play(Uncreate(equacoes_esquerda,run_time=0.5),Uncreate(equacoes_direita,run_time=0.5))