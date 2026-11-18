from dao import ClienteDAO, CategoriaDAO, ProdutoDAO


class Servico:
    def __init__(self):
        self.clientes = ClienteDAO()
        self.categorias = CategoriaDAO()
        self.produtos = ProdutoDAO()

    def cadastrar_cliente(self, nome, email):
        return self.clientes.inserir(nome, email)

    def cadastrar_categoria(self, nome):
        return self.categorias.inserir(nome)

    def cadastrar_produto(self, nome, preco, estoque, categoria_id):
        if self.categorias.buscar(categoria_id) is None:
            raise ValueError("Categoria não encontrada.")
        if preco < 0 or estoque < 0:
            raise ValueError("Preço e estoque devem ser positivos.")
        return self.produtos.inserir(nome, preco, estoque, categoria_id)

    def ajustar_estoque(self, produto_id, quantidade):
        produto = self.produtos.buscar(produto_id)
        if produto is None:
            raise ValueError("Produto não encontrado.")
        novo_estoque = produto.estoque + quantidade
        if novo_estoque < 0:
            raise ValueError("Estoque não pode ficar negativo.")
        self.produtos.atualizar(produto.id, produto.nome, produto.preco,
                                novo_estoque, produto.categoria_id)

    def excluir_categoria(self, id):
        if any(p.categoria_id == id for p in self.produtos.listar()):
            raise ValueError("A categoria possui produtos cadastrados.")
        return self.categorias.excluir(id)
