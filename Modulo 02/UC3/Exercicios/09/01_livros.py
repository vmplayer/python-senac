class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrarDados(self):
        print("\n=== DADOS DO LIVRO ===")
        print()
        print(f" Título: {self.titulo}")
        print(f"  Autor: {self.autor}")
        print(f"Páginas: {self.paginas}\n")

    def alterarPaginas(self, novoValor):
        self.paginas = novoValor
        print("Valor alterado com sucesso!")

livro1 = Livro("A Sutil Arte de Ligar o Xablau", "J. K. Xablau", 100)
livro2 = Livro("Xablau Wars", "Xablau Lucas", 455)

livro1.mostrarDados()
livro2.mostrarDados()
livro1.alterarPaginas(200)
livro1.mostrarDados()

# classe = LIVRO
# instancias = livro1 e livro2
# atributos = titulo, autor, paginas

# Não, afetou apenas o que eu editei. Hmph!
