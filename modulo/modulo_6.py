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

        eq_original = MathTex(r"f(x) = |x|")
        eq_original.shift(UP * 2)

        self.play(Create(eq_original))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": WHITE}
        )

        # Label axes
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Create the graph of y = |x|
        graph = axes.plot(
            lambda x: abs(x),
            color=BLUE,
            stroke_width=1
        )

        # Label the graph

        # Add elements to the scene
        graph_group = VGroup(axes, labels, graph)

        # Scale down the whole group to half the size
        graph_group.scale(0.5)

        # Position the group at the center of the screen
        graph_group.move_to(ORIGIN)

        graph_group.shift(DOWN)

        # Add elements to the scene
        self.play(Create(graph_group), run_time=1)

        xA = ValueTracker(-3)

        pointA = always_redraw(lambda: Dot(
            axes.c2p(xA.get_value(), abs(xA.get_value())),
            color=RED
        ))

        labelA = always_redraw(lambda: MathTex(
            f"({xA.get_value():.1f}, {abs(xA.get_value()):.1f})"
        ).next_to(
            axes.c2p(xA.get_value(), abs(xA.get_value())),
            UP
        ).scale(0.8).set_color(WHITE))

        self.play(Create(pointA))

        self.wait(2)

        dashed_lines = always_redraw(lambda: VGroup(
            DashedLine(
                start=axes.c2p(xA.get_value(), 0),
                end=axes.c2p(xA.get_value(), abs(xA.get_value())),
                color=YELLOW
            ),
            DashedLine(
                start=axes.c2p(0, abs(xA.get_value())),
                end=axes.c2p(xA.get_value(), abs(xA.get_value())),
                color=YELLOW
            )
        ))

        self.play(Write(labelA), Create(dashed_lines))

        self.wait(2)

        self.play(xA.animate.set_value(-2), run_time=3, rate_func=smooth)
        self.wait(2)
        self.play(xA.animate.set_value(-4), run_time=3, rate_func=smooth)
        self.wait(2)
        self.play(xA.animate.set_value(2), run_time=3, rate_func=smooth)
        self.wait(2)

        eqA = MathTex(r"x = 0\\", r"\text{ Ponto Mínimo}")
        eqA.to_edge(LEFT).shift(UP).scale(0.8)

        self.play(Write(eqA))

        dashed_lines.clear_updaters()
        pointA.clear_updaters()
        labelA.clear_updaters()

        self.play(FadeOut(dashed_lines, pointA, labelA))
        self.remove(dashed_lines, pointA, labelA)

        eq_original = transformEq(
            eq_original, MathTex(r"f(x) = |x +2 |"), self)

        graph2 = axes.plot(
            lambda x: abs(x + 2),
            color=BLUE,
            stroke_width=1
        )

        pointA = always_redraw(lambda: Dot(
            axes.c2p(xA.get_value(), abs(xA.get_value()+2)),
            color=RED
        ))

        labelA = always_redraw(lambda: MathTex(
            f"({xA.get_value():.1f}, {abs(xA.get_value()+2):.1f})"
        ).next_to(
            axes.c2p(xA.get_value(), abs(xA.get_value()+2)),
            UP
        ).scale(0.8).set_color(WHITE))
        dashed_lines = always_redraw(lambda: VGroup(
            DashedLine(
                start=axes.c2p(xA.get_value(), 0),
                end=axes.c2p(xA.get_value(), abs(xA.get_value()+2)),
                color=YELLOW
            ),
            DashedLine(
                start=axes.c2p(0, abs(xA.get_value()+2)),
                end=axes.c2p(xA.get_value(), abs(xA.get_value()+2)),
                color=YELLOW
            )
        ))

        self.play(Transform(graph, graph2), Create(
            pointA), Create(dashed_lines), Write(labelA))

        temp = MathTex(r"x = -2\\", r"\text{ Ponto Mínimo}")
        eqA = transformEq(eqA, temp, self)

        self.wait(3)

        self.play(FadeOut(dashed_lines, pointA, labelA, eqA))

        self.wait(1)
