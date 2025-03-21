from manim import *
from utils import *
class Modulo(Scene):
    def construct(self):     
        
         
        titulo = getAbsoluteValue()
        self.play(Write(titulo))
        
        self.play(titulo.animate.to_edge(UP))
        
        self.wait(1)
        
        apenas_eixo_x = NumberLine(
            x_range=[-5, 5, 1],
            include_tip=True,
            include_numbers=True,
            label_direction=DOWN,
        ).scale(0.9) 
        
       
        for number in apenas_eixo_x.numbers:
            if number.get_value() == 0:  # Verifica se o número é 0
                number.set_color(RED)
        
        ponto_a = Dot(color=RED,point=apenas_eixo_x.n2p(-3))
        
         # Ponto na curva
        x = ValueTracker(-3)  # Começar em x=2
        
        
        # Função para atualizar a posição do ponto
        def update_ponto(p):
            new_point = apenas_eixo_x.n2p(x.get_value())
            p.move_to(new_point)
            return p
        
        ponto_a.add_updater(update_ponto)
        
        chave = always_redraw(
            lambda:BraceBetweenPoints(ponto_a, apenas_eixo_x.n2p(0),color=BLUE, direction=DOWN,buff=1))
        
        modulo_texto = always_redraw(
            lambda: Text("{}".format(round(abs(x.get_value()),1)), font="Arial",font_size=24,color=BLUE).next_to(chave,DOWN)
        )
           
        
        self.play(*[Create(obj) for obj in [apenas_eixo_x,ponto_a,chave,modulo_texto]])
        self.wait()                
        self.play(x.animate.set_value(-1), run_time=2)
        self.play(x.animate.set_value(-4), run_time=3)
        self.play(x.animate.set_value(1), run_time=2)
        self.play(x.animate.set_value(2), run_time=2)
        self.wait(1)
        
        self.play(*[Uncreate(obj,run_time=0.2) for obj in [apenas_eixo_x,ponto_a,chave,modulo_texto]],titulo.animate.scale(0.7).to_corner(UL, buff=0.5))
        self.wait()
        
        