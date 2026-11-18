class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.id} - {self.nome} ({self.email})"


class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"{self.id} - {self.nome}"


class Produto:
    def __init__(self, id, nome, preco, estoque, categoria_id):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria_id = categoria_id

    def __str__(self):
        return (f"{self.id} - {self.nome} | R$ {self.preco:.2f} | "
                f"Estoque: {self.estoque} | Categoria: {self.categoria_id}")
