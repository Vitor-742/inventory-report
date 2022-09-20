from inventory_report.inventory.product import Product
from datetime import datetime


def test_cria_produto():
    produto_test = Product(
        3,
        'produtoTeste',
        'empresaTeste',
        datetime.now().strftime("%x"),
        datetime.now().strftime("%x"),
        '10',
        'em ambiente arejado'
    )
    assert type(produto_test.id) == int
    assert type(produto_test.nome_do_produto) == str
    assert type(produto_test.nome_da_empresa) == str
    assert type(produto_test.data_de_fabricacao) == str
    assert type(produto_test.data_de_validade) == str
    assert type(produto_test.numero_de_serie) == str
    assert type(produto_test.instrucoes_de_armazenamento) == str
