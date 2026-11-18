from servico import Servico


def ler_id(texto="ID: "):
    return int(input(texto))


def mostrar_lista(titulo, itens):
    print(f"\n{titulo}")
    if not itens:
        print("Nenhum registro cadastrado.")
    for item in itens:
        print(item)


def executar():
    sistema = Servico()
    while True:
        print("\n=== Sistema de Comércio ===")
        print("1. Cadastrar cliente   2. Listar clientes")
        print("3. Cadastrar categoria 4. Listar categorias")
        print("5. Cadastrar produto   6. Listar produtos")
        print("7. Ajustar estoque     8. Excluir cadastro")
        print("9. Atualizar cadastro")
        print("0. Sair")
        opcao = input("Escolha: ").strip()

        try:
            if opcao == "1":
                sistema.cadastrar_cliente(input("Nome: "), input("E-mail: "))
                print("Cliente cadastrado.")
            elif opcao == "2":
                mostrar_lista("Clientes", sistema.clientes.listar())
            elif opcao == "3":
                sistema.cadastrar_categoria(input("Nome da categoria: "))
                print("Categoria cadastrada.")
            elif opcao == "4":
                mostrar_lista("Categorias", sistema.categorias.listar())
            elif opcao == "5":
                nome = input("Nome do produto: ")
                preco = float(input("Preço: R$ ").replace(",", "."))
                estoque = int(input("Estoque inicial: "))
                categoria_id = ler_id("ID da categoria: ")
                sistema.cadastrar_produto(nome, preco, estoque, categoria_id)
                print("Produto cadastrado.")
            elif opcao == "6":
                mostrar_lista("Produtos", sistema.produtos.listar())
            elif opcao == "7":
                produto_id = ler_id("ID do produto: ")
                quantidade = int(input("Quantidade (use negativo para retirar): "))
                sistema.ajustar_estoque(produto_id, quantidade)
                print("Estoque atualizado.")
            elif opcao == "8":
                tipo = input("Excluir (cliente/categoria/produto): ").lower()
                id = ler_id()
                daos = {"cliente": sistema.clientes,
                        "categoria": sistema.categorias,
                        "produto": sistema.produtos}
                if tipo == "categoria":
                    removido = sistema.excluir_categoria(id)
                elif tipo in daos:
                    removido = daos[tipo].excluir(id)
                else:
                    print("Tipo inválido.")
                    continue
                print("Cadastro excluído." if removido else "ID não encontrado.")
            elif opcao == "9":
                tipo = input("Atualizar (cliente/categoria/produto): ").lower()
                id = ler_id()
                if tipo == "cliente":
                    dao = sistema.clientes
                    valores = (input("Novo nome: "), input("Novo e-mail: "))
                elif tipo == "categoria":
                    dao = sistema.categorias
                    valores = (input("Novo nome: "),)
                elif tipo == "produto":
                    dao = sistema.produtos
                    nome = input("Novo nome: ")
                    preco = float(input("Novo preço: R$ ").replace(",", "."))
                    estoque = int(input("Novo estoque: "))
                    categoria_id = ler_id("ID da categoria: ")
                    if sistema.categorias.buscar(categoria_id) is None:
                        raise ValueError("Categoria não encontrada.")
                    valores = (nome, preco, estoque, categoria_id)
                else:
                    print("Tipo inválido.")
                    continue
                if dao.atualizar(id, *valores):
                    print("Cadastro atualizado.")
                else:
                    print("ID não encontrado.")
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")
