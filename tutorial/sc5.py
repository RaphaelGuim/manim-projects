from manim import *

class Derivada(Scene):
    def construct(self):
        # Criar eixos
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 9],
            axis_config={"include_tip": True}
        ).add_coordinates()
        
        # Função f(x) = x²
        funcao = axes.plot(lambda x: x**2,x_range=[-1,4], color=BLUE)
        
        rotulo_funcao = MathTex("f(x) = x^2").next_to(axes.coords_to_point(3, 7),buff=0.5)        
        # Mostrar eixos e função
        
        self.play(Create(axes), Create(funcao), Write(rotulo_funcao))               
        
        # Ponto na curva
        x = ValueTracker(0)  # Começar em x=2
        ponto = Dot(color=RED)
        
        # Função para atualizar a posição do ponto
        def update_ponto(p):
            new_point = axes.coords_to_point(x.get_value(), x.get_value()**2)
            p.move_to(new_point)
            return p
        
        ponto.add_updater(update_ponto)

        
        # Tangente à curva
        tangente = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=funcao,
                dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=3
            )
        )
        
        self.play(Create(ponto), Create(tangente))
        
        # Mover o ponto ao longo da curva
        self.play(x.animate.set_value(3), run_time=3)
        self.wait()
        
        # Mostrar derivada
        derivada = axes.plot(lambda x: 2*x, color=RED)
        rotulo_derivada = MathTex("f'(x) = 2x").next_to(derivada.get_center(), buff=0.5) 
        
        
        ponto_a = Dot(point=[-2, 0,0], color=RED)
         
        self.play(Create(derivada),Write(rotulo_derivada),Create(ponto_a))
        
        
        # ponto = have = BraceBetweenPoints(ponto_a.get_center(), ponto_b.get_center(), direction=DOWN)
        self.wait(2)