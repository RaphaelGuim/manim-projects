from manim import *


def getAbsoluteValue():
    moduloText = Text("Valor Absoluto")
    equacaoText = MathTex(r"|x|", color=BLUE).next_to(
        moduloText, DOWN, buff=0.5)
    equacaoText.scale(2)
    return VGroup(moduloText, equacaoText)


def getDefinition():
    caso_positivo = MathTex("+", r"a", r"\text{ if } a \geq 0")
    caso_positivo[0].set_opacity(0)
    caso_positivo[1].set_color(BLUE)  # Colore apenas o "x" inicial em azul

    caso_negativo = MathTex(r"-a", r"\text{ if } a < 0")
    caso_negativo[0].set_color(RED)  # Colore apenas o "-x" inicial em vermelho
    casos = VGroup(caso_positivo, caso_negativo).arrange(
        DOWN, aligned_edge=LEFT)

    parte_esquerda = MathTex(r"|a|")

    # Criar o sinal = separadamente
    igual = MathTex(r"=")

    # Criar a chave (apontando para a direita)
    chave = Brace(casos, direction=LEFT)

    # Posicionar tudo corretamente
    igual.next_to(parte_esquerda, RIGHT)

    chave.next_to(igual, RIGHT)

    casos.next_to(chave, RIGHT)

    # Agrupar tudo
    return VGroup(parte_esquerda, igual, chave, casos)


def transformEq(eq, mathExp, scene, run_time=1):
    mathExp.move_to(eq)
    scene.play(TransformMatchingTex(eq, mathExp), run_time=run_time)
    return mathExp


def transformEqSteps(eq, steps, scene, run_time=1):
    steps = [MathTex(*step) if type(step) ==
             str else step for step in steps]
    for step in steps:
        eq = transformEq(eq, step, scene, run_time)

    return eq


def nextLine(eq, scene):
    line = eq.copy()
    scene.play(line.animate.next_to(eq, DOWN))
    return line
