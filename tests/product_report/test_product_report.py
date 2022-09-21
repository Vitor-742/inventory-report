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
    dateToday = str(datetime.now().strftime("%x"))
    assert str(produto_test) == f"O produto produtoTeste fabricado em {dateToday} \
por empresaTeste com validade até {dateToday} precisa ser armazenado em \
ambiente arejado."
