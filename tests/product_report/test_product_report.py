from inventory_report.inventory.product import Product
from datetime import datetime


def test_relatorio_produto():
    produto_test = Product(
        3,
        'produtoTeste',
        'empresaTeste',
        datetime.now().strftime("%x"),
        datetime.now().strftime("%x"),
        '10',
        'em ambiente arejado'
    )
    assert str(produto_test) == "O produto produtoTeste fabricado em 09/20/22 \
por empresaTeste com validade até 09/20/22 precisa ser armazenado em \
ambiente arejado."
