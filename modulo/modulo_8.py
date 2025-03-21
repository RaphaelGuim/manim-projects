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

        eq_original = MathTex(r"|x + 2 | + |x-1| = 3")
        eq_original.shift(UP * 2)

        self.play(Create(eq_original))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.play(eq_original.animate.to_corner(UL))

        LA1 = Text("Passo 1: Descobrir as raizes das Equações Modulares",
                   font="Arial", font_size=24, color=RED)
        LA2 = MathTex("f1(x) = |x+2|", r"\Rightarrow",
                      "x+2", "=", r"0 \Rightarrow", "x=", r"-2")
        LA3 = MathTex("f2(x) = |x-1|", r"\Rightarrow",
                      "x-1", "=", r"0 \Rightarrow", "x=", r"1")

        textos = VGroup(LA1, LA2, LA3)
        textos.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        textos.to_edge(LEFT).shift(UP)

        self.play(Create(LA1))
        self.wait(2)
        self.play(Create(LA2))
        self.wait(2)
        self.play(Create(LA3))

        self.wait(2)

        self.play(LA2[6].animate.set_color(BLUE),
                  LA3[6].animate.set_color(GREEN))

        textA = LA2[6].copy()
        textB = LA3[6].copy()
        self.wait(2)
        self.add(textA, textB)
        self.play(FadeOut(LA1, LA2, LA3), run_time=1)

        self.wait(1)
        self.play(textA.animate.center().shift(LEFT+UP*3),
                  textB.animate.center().shift(RIGHT+UP*3))

        self.wait(2)
