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