from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

fornecedores = [
    Fornecedor(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
    Fornecedor(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
    Fornecedor(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
    Fornecedor(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
    Fornecedor(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
]

session.add_all(fornecedores)
session.commit()

produtos = [
    Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
    Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
    Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
    Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
    Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
]

session.add_all(produtos)
session.commit()


for produto in session.query(Produto).all():
    print(f"Produto: {produto.nome}, Fornecedor: {produto.fornecedor.nome}")