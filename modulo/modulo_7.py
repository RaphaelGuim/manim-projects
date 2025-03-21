from manim import *
from utils import *


class Modulo(Scene):
    def construct(self):

        titulo = getAbsoluteValue()
        titulo.scale(0.7).to_corner(UL)
        self.add(titulo)

        definicao = getDefinition()
        definicao.scale(0.8).to_corner(UR)
        self.add(definicao)

        eq_original = MathTex(r"f(x) = |x + 2 |")
        eq_original.shift(UP * 2)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": WHITE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        graph_positive = axes.plot(
            lambda x: abs(x + 2) if x > -2 else 0,
            x_range=[-2, 3],
            color=BLUE,
            stroke_width=1
        )

        x_values = list(range(-4, 2))  # de -3 até 2
        table_data = [["x", "x+2", "|x+2|"]]
        for x in x_values:
            x_plus_2 = x + 2
            abs_x_plus_2 = abs(x_plus_2)
            table_data.append([str(x), str(x_plus_2), str(abs_x_plus_2)])

        # Criando a tabela
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 1}

        )

        # Posicionando a tabela no lado direito
        table.scale(0.3)
        table.to_edge(LEFT)

        # Adicionando a tabela à cena

        # Texto para x > -2
        texto_positive = MathTex(
            r"\text{se } x \geq -2 \Rightarrow f(x) = x + 2")
        texto_positive.shift(UP).set_color(BLUE)
        # Agrupando elementos
        graph_group = VGroup(
            axes, labels, graph_positive)
        graph_group.scale(0.5).move_to(ORIGIN).shift(DOWN)

        # Adicionando e animando a primeira parte
        self.add(eq_original, axes, labels)
        self.play(Create(table))
        self.wait(2)
        self.play(Create(graph_positive))
        self.wait(2)
        self.play(Write(texto_positive))
        self.wait(2)
        self.play(FadeOut(texto_positive))

        # Gráfico para x < -2
        graph_negative = axes.plot(
            lambda x: abs(x + 2) if x < -2 else 0,
            x_range=[-5, -2],
            color=RED,
            stroke_width=1
        )

        # Texto para x < -2
        texto_negative = MathTex(
            r"\text{se } x < -2 \Rightarrow f(x) = -(x + 2)")
        texto_negative.shift(UP).set_color(RED)
        # Agrupando elementos

        # Adicionando e animando a segunda parte
        self.play(Create(graph_negative))
        self.wait(2)
        self.play(Write(texto_negative))
        self.wait(2)

        graph_group.add(graph_negative)

        self.play(graph_group.animate.to_corner(DR).scale(0.8))
        self.play(FadeOut(texto_negative), definicao.animate.center())
        self.wait(3)
        self.play(definicao.animate.center())
        self.wait(3)
        self.play(FadeOut(table, eq_original, graph_group),
                  definicao.animate.to_corner(UR))
