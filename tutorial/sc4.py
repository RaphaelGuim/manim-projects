from manim import *

class Coordenadas(Scene):
    def construct(self):
        # Criando um plano
        plano = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }
        ) 
        
        # Adicionar rótulos aos eixos
        eixos = Axes(
            x_range=[-7, 7, 0.5],
            y_range=[-4, 4, 1],
            axis_config={"include_tip": True}
        )
        
        # Mostrar o plano e eixos        
        self.play(Create(plano), Create(eixos))
        
        # Criar pontos em coordenadas específicas
        ponto1 = Dot(point=eixos.coords_to_point(2, 3), color=RED)
        ponto2 = Dot(point=eixos.coords_to_point(-3, -2), color=GREEN)
        
        # Mostrar os pontos
        self.play(Create(ponto1), Create(ponto2))
        
        # Conectar os pontos
        linha = Line(ponto1.get_center(), ponto2.get_center(), color=YELLOW)
        self.play(Create(linha))
        
        self.wait(1)