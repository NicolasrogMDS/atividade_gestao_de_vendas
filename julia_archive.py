from os import system

#limpar terminal

def limpar_terminal():
    system("cls||clear")

def menu_principal():
    limpar_terminal()

    print("""
1 - Adicionar um produto ao estoque
2 - Alterar p preço de um produto
3 - Renomear um produto
4 - Remover um produto
5 - Verificar todos os produtos no estoque
6 - Sair do sistema
""")