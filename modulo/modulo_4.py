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

        eq_original = MathTex(r"|x - 3| = 2")
        eq_original.shift(UP * 2)

        self.play(Write(eq_original))
        self.wait(1)

        lA = MathTex(r"(x-3)",  r"\text{ if } (x-3) \geq 0")
        lA.to_edge(LEFT).shift(UP)
        lA[0].set_color(BLUE)

        self.play(Write(lA))
        self.wait(1)

        lA1 = MathTex(r"(x", r"-3", r")", r"=", r"2")
        lA1.to_edge(LEFT)
        self.play(Write(lA1))

        lA2 = nextLine(lA1, self)

        self.play(lA2[1].animate.set_color(RED))
        lA2 = transformEq(lA2, MathTex(r"x", r"=", r"2", r"+3"), self)

        lA3 = nextLine(lA2, self)
        lA3 = transformEq(lA3, MathTex(r"x", r"=", r"5"), self)

        LB = MathTex(r"-(x-3)",  r"\text{ if } (x-3) < 0")
        LB.to_edge(RIGHT).shift(UP)
        LB[0].set_color(RED)
        self.play(Write(LB))
        self.wait(1)

        LB1 = MathTex(r"-(x-3)", r"=", r"2")
        LB1.to_edge(RIGHT)
        self.play(Write(LB1))
        self.wait(1)

        LB2 = nextLine(LB1, self)

        self.play(LB2[0][0].animate.set_color(RED))

        LB2 = transformEq(LB2, MathTex(r"(-x+3)", r"=", r"2"), self)

        LB3 = nextLine(LB2, self)

        self.play(LB3[0][3].animate.set_color(RED),
                  LB3[0][4].animate.set_color(RED))

        LB3 = transformEq(LB3, MathTex(r"(-x)", r"=", r"2", r"-3"), self)

        LB4 = nextLine(LB3, self)
        LB4 = transformEqSteps(
            LB4, [MathTex(r"(-x)", r"=", r"-1"), MathTex(r"x", r"=", r"1")], self)

        self.wait(3)

        resultA = lA3
        resultB = LB4

        self.play(*[Uncreate(obj)
                  for obj in [lA, lA1, lA2, LB, LB1, LB2, LB3]],
                  resultA.animate.move_to(ORIGIN).to_edge(
                      LEFT).shift(UP).set_color(BLUE),
                  resultB.animate.move_to(ORIGIN).to_edge(
                      RIGHT).shift(UP).shift(LEFT * 3).set_color(RED),


                  run_time=0.5)

        self.wait(2)
