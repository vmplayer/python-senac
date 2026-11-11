class Retangulo:
    def __init__(self, largura, altura):
        if largura or altura < 0:
            print("A largura é menor do que zero.")