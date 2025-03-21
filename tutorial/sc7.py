from manim import *

class Fibonacci(Scene):
    def construct(self):
        # Título
        titulo = Text("Sequência de Fibonacci").to_edge(UP)
        self.play(Write(titulo))
        
        # Definição
        definicao = MathTex(
            r"F_0 &= 0\\",
            r"F_1 &= 1\\",
            r"F_n &= F_{n-1} + F_{n-2} \quad \text{para } n > 1"
        ).next_to(titulo, DOWN, buff=0.5)
        
        self.play(Write(definicao))
        self.wait()
        
        # Calcular a sequência
        fib = [0, 1]
        for i in range(2, 10):
            fib.append(fib[i-1] + fib[i-2])
        
        # Criar gráfico de barras
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, fib[-1] + 10, 50],
            axis_config={"include_tip": True}
        ).to_edge(DOWN, buff=1)
        
        barras = VGroup()
        
        for i, val in enumerate(fib):
            barra = Rectangle(
                height=val/10,
                width=0.5,
                fill_color=BLUE,
                fill_opacity=0.8,
                stroke_color=WHITE
            ).move_to(axes.coords_to_point(i, val/2), aligned_edge=DOWN)
            valor = Text(str(val), font_size=20).next_to(barra, UP, buff=0.1)
            indice = Text(f"F{i}", font_size=16).next_to(barra, DOWN, buff=0.1)
            grupo = VGroup(barra, valor, indice)
            barras.add(grupo)
        
        self.play(Create(axes))
        
        # Mostrar cada barra sequencialmente
        for barra in barras:
            self.play(Create(barra))
        
        self.wait(2)
        
        # Razão de Ouro
        razao = Text("À medida que n cresce, Fₙ₊₁/Fₙ se aproxima da razão áurea")
        razao_formula = MathTex(r"\frac{F_{n+1}}{F_n} \approx \frac{1 + \sqrt{5}}{2} \approx 1.618")
        
        grupo_razao = VGroup(razao, razao_formula).arrange(DOWN).to_edge(DOWN)
        
        self.play(FadeOut(barras), FadeOut(axes))
        self.play(Write(grupo_razao))
        
        self.wait(2)