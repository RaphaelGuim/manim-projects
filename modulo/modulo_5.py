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

        eq_original = MathTex(r"|", r"x", r"-3" + r"|", r"=", r"2")
        eq_original.shift(UP * 2)

        self.add(eq_original)

        resultA = MathTex(r"x", r"=", r"5")
        resultA.to_edge(LEFT).shift(UP).set_color(BLUE)
        resultB = MathTex(r"x", r"=", r"1")
        resultB.to_edge(RIGHT).shift(UP+LEFT * 3).set_color(RED)

        self.add(resultA)
        self.add(resultB)

        self.wait(1)

        todoA = MathTex(r"\Rightarrow", r"|", r"x", r"-3", r"|", r"=", r"2")
        todoA.next_to(resultA, RIGHT)
        self.play(Create(todoA))

        self.wait(1)

        LA = eq_original.copy()
        LA.next_to(resultA, DOWN).shift(RIGHT * 0.5)
        self.play(Create(LA))

        temp = MathTex(
            r"|", r"5", r"-3" + r"|", r"=", r"2")
        temp[1].set_color(BLUE)

        LA = transformEq(LA, temp, self)

        LA1 = nextLine(LA, self)
        LA1 = transformEq(LA1, MathTex(r"|", r"2" + r"|", r"=", r"2"), self)

        self.wait(1)

        LB = eq_original.copy()

        todoB = MathTex(r"\Rightarrow", r"|", r"x", r"-3", r"|", r"=", r"2")

        todoB.next_to(resultB, RIGHT)

        self.play(Create(todoB))
        self.wait(1)

        LB.next_to(resultB, DOWN).shift(RIGHT * 0.5)
        self.play(Create(LB))

        temp = MathTex(
            r"|", r"1", r"-3" + r"|", r"=", r"2")
        temp[1].set_color(RED)

        LB = transformEq(LB, temp, self)

        LB1 = nextLine(LB, self)
        LB1 = transformEq(LB1, MathTex(r"|", r"-2" + r"|", r"=", r"2"), self)

        self.wait(3)

        self.play(*[Uncreate(obj)
                  for obj in [resultA, resultB, todoA, todoB, LA, LA1, LB, LB1, eq_original]],


                  run_time=0.5)

        self.wait(2)
