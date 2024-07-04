class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Titulo: {self._titulo}| Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao} | Disponivel: {self._disponivel}'

    def emprestar(self):
        self._disponivel = False

    @property
    def disponivel(self):
        return 'Sim' if self._disponivel else 'Não'

    @staticmethod
    def verificar_disponibilidade(ano):
        for livro in Livro.livros:
            if livro._ano_publicacao == ano:
                print(f'Livro: {livro._titulo}')


livro1 = Livro('Harry Potter', 'Maria', 2009)
livro2 = Livro('Dom Casmurro', 'Machado de Assis', 1889)

print(livro1)
print(livro2)

livro2.emprestar()
print(livro2)

Livro.verificar_disponibilidade(2009)