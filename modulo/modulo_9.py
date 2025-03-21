from manim import *
from utils import *


def getGroupA():
    axesA = Axes(
        x_range=[-5, 5, 1],
        y_range=[-1, 5, 1],
        axis_config={"color": WHITE}
    )
    labelsA = axesA.get_axis_labels(x_label="x", y_label="y")

    graphA = axesA.plot(
        lambda x: abs(x + 2),
        x_range=[-5, 3],
        color=BLUE,
    )
    legendaA = MathTex("f(x) = |x + 2|", color=BLUE)
    legendaA.next_to(axesA, UP).shift(UP)

    aCoords = (-2, 0)
    pointA = Dot(axesA.coords_to_point(*aCoords), color=BLUE)
    labelA = MathTex(f"({aCoords[0]}, {aCoords[1]})")
    labelA.next_to(pointA, DOWN, buff=0.1)

    return VGroup(axesA, labelsA, graphA, legendaA, pointA, labelA)


def getGroupB():
    axesB = Axes(
        x_range=[-5, 5, 1],
        y_range=[-1, 5, 1],
        axis_config={"color": WHITE}
    )
    labelsB = axesB.get_axis_labels(x_label="x", y_label="y")

    graphB = axesB.plot(
        lambda x: abs(x - 1),
        x_range=[-5, 3],
        color=GREEN,

    )

    legendaB = MathTex("f(x) = |x -1|", color=GREEN)
    legendaB.next_to(axesB, UP).shift(UP)
    bCoords = (1, 0)
    pointB = Dot(axesB.coords_to_point(*bCoords), color=BLUE)
    labelB = MathTex(f"({bCoords[0]}, {bCoords[1]})")
    labelB.next_to(pointB, DOWN, buff=0.1)

    return VGroup(axesB, labelsB, graphB, legendaB, pointB, labelB)


class Modulo(Scene):
    def construct(self):

        definicao = getDefinition()
        definicao.scale(0.8).to_corner(UR)
        self.add(definicao)

        eq_original = MathTex(r"|x + 2 | + |x-1| = 3")
        eq_original.shift(UP * 2)
        eq_original.to_corner(UL)
        self.add(eq_original)

        textA = MathTex(r"-2")
        textB = MathTex(r"1")

        textA.set_color(BLUE).center().shift(LEFT+UP*3)
        textB.set_color(GREEN).center().shift(RIGHT+UP*3)
        self.add(textA, textB)

        tempA = MathTex(r"k_0 =-2")
        tempA.set_color(BLUE)
        tempB = MathTex(r"k_0 =1")
        tempB.set_color(GREEN)

        textA = transformEq(textA, tempA, self)
        textB = transformEq(textB, tempB, self)

        self.play(textA.animate.shift(DOWN*0.2), textB.animate.shift(DOWN*0.2))
        self.wait(2)

        LA1 = Text("Passo 2: Analizar a equação nos Intervalos entre as Raizes",
                   font="Arial", font_size=24, color=RED)
        LA2 = MathTex(r"x \geq 1")
        LA3 = MathTex(r"|x-1| e |x+2| \geq 0")

        textos = VGroup(LA1, LA2, LA3)
        textos.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        textos.to_edge(LEFT).shift(UP)

        self.play(Create(LA1))

        graph_groupA = getGroupA()
        graph_groupB = getGroupB()

        graph_groupB.scale(0.5).to_corner(DR)
        graph_groupA.scale(0.5).next_to(graph_groupB, LEFT)

        self.play(Create(graph_groupA), Create(graph_groupB))
        self.wait(3)
        return

        LA1 = Text("Passo 2: Analizar a equação nos Intervalos entre as Raizes",
                   font="Arial", font_size=24, color=RED)
        LA2 = MathTex(r"x \geq 1", r"\Rightarrow", r"|x-1| e |x+2| \geq 0")

        LA3 = MathTex(*[r"{}".format(char)
                      for char in "|x + 2 | + |x - 1| = 3"])

        textos = VGroup(LA1, LA2)
        textos.arrange(DOWN, aligned_edge=LEFT, buff=0.01)

        textos.to_edge(LEFT).shift(UP)
        self.wait(2)

        self.play(Create(LA2))
        self.wait(2)
        self.play(FadeOut(graph_groupA), FadeOut(graph_groupB))
        self.wait(3)

        self.play(Create(LA3))
        self.wait(4)

        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "(x + 2) + (x - 1) = 3"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "x + 2 + x - 1 = 3"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "2x + 1 = 3"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "2x=2"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(r"x_1=1"), self)
        self.wait(1)

        resultA = LA3.copy()
        self.add(resultA)
        self.play(FadeOut(LA2, LA3), resultA.animate.to_corner(UR))
        self.wait(3)
        self.play(FadeIn(graph_groupA), FadeIn(graph_groupB))
        self.wait(3)

        LA2 = MathTex(r"-2 \geq x \geq 1", r"\Rightarrow",
                      r"|x-1| \leq 0 e |x+2| \geq 0")

        LA3 = MathTex(*[r"{}".format(char)
                        for char in "|x + 2 | + |x - 1| = 3"])

        textos = VGroup(LA1, LA2)
        textos.arrange(DOWN, aligned_edge=LEFT, buff=0.01)

        textos.to_edge(LEFT).shift(UP)
        self.wait(2)

        self.play(Create(LA2))
        self.wait(2)
        self.play(FadeOut(graph_groupA), FadeOut(graph_groupB))
        self.wait(3)

        self.play(Create(LA3))
        self.wait(4)

        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "(x + 2) + -(x - 1) = 3"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "x + 2 + x - 1 = 3"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "2x + 1 = 3"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(
            *[r"{}".format(char) for char in "2x=2"]), self)
        self.wait(1)
        LA3 = transformEq(LA3, MathTex(r"x_1=1"), self)
        self.wait(1)

        resultA = LA3.copy()
        self.add(resultA)
        self.play(FadeOut(LA2, LA3), resultA.animate.to_corner(UR))
        self.wait(3)
