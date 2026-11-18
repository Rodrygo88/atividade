from modelo import Cliente, Categoria, Produto


class DAO:
    classe = None

    def __init__(self):
        self.dados = {}
        self.proximo_id = 1

    def inserir(self, *valores):
        objeto = self.classe(self.proximo_id, *valores)
        self.dados[self.proximo_id] = objeto
        self.proximo_id += 1
        return objeto

    def listar(self):
        return list(self.dados.values())

    def buscar(self, id):
        return self.dados.get(id)

    def atualizar(self, id, *valores):
        if id not in self.dados:
            return False
        self.dados[id] = self.classe(id, *valores)
        return True

    def excluir(self, id):
        return self.dados.pop(id, None) is not None


class ClienteDAO(DAO):
    classe = Cliente


class CategoriaDAO(DAO):
    classe = Categoria


class ProdutoDAO(DAO):
    classe = Produto
