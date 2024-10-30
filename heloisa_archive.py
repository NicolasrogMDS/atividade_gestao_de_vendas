def adicionar_produto():
    produto = Produto (
        nome = input("insira o nome do produto: ")
        preco = float(input("Insira o preço do produto: "))     
    )
    session.add(produto)
    session.commit()
    return produto

def alterar_preco_produto():
    produto = session.querry(Produto).filter(Produto.nome == nome_do_produto).first
    produto.preco = input("Digite o novo preço do produto: ")
    session.commit()
