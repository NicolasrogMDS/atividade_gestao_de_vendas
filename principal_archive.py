"""
Turma - 93313 - Lógica de Programação
Componentes:
Júlia Vitória
Heloísa Lima
Nicolas Roger
"""

from os import system
from time import sleep
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base 

dados = []
#Criando Banco de dados:
BD = create_engine("sqlite:///sistema_de_gestao_de_vendas.db")

#Conectando ao banco de dados:
Session = sessionmaker(bind=BD)
session = Session()

#Criando Tabela e Classe:
Base = declarative_base()

class Produto(Base):
    __tablename__ = "produto"
    
    #Definindo variaveis da tabela:
    nome = Column(String, primary_key=True)
    preco = Column(Float)

def __init__(self,nome:str, preco:float):
        self.nome = nome
        self.preco = preco

#Criando tabela de dados, no banco de dados:
Base.metadata.create_all(bind=BD)

def limpar_terminal():
    sleep(1)
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
    
def adicionar_produto():
    produto = Produto (
        nome = input("insira o nome do produto: "),
        preco = float(input("Insira o preço do produto: "))     
        )
    session.add(produto)
    session.commit()
    return produto

def alterar_preco_produto(nome_do_produto):
    produto = session.querry(Produto).filter(Produto.nome == nome_do_produto).first
    produto.preco = input("Digite o novo preço do produto: ")
    session.commit()

def renomear_produto(nome_do_produto):
    produto = session.query(Produto).filter(Produto.nome == nome_do_produto).first()
    produto.nome = input("Novo nome do produto: ")    
    session.commit()

def remover_produto():
    print("\nRemovendo produto:")
    nome_produto = input("Infome o nome do produto para que ele excluído: ").lower()
    produto = session.query(Produto).filter_by(nome = nome_produto).first()
    session.delete(produto)
    session.commit()

def verificar_todos_os_produtos():
    lista_produtos = session.query(Produto).all()
    for produto in lista_produtos:
        print(f"\nNome: {produto.nome}")
        print(f"Preço: {produto.preco}")