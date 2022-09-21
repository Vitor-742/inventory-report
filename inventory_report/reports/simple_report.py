from datetime import date
from collections import Counter


class SimpleReport:
    def generate(self, lista):
        oldestDate = date.today()
        closest_date = date.min
        empresas = []
        for item in lista:
            empresas.append(item['nome_da_empresa'])
            dateFabricacao = date.fromisoformat(item['data_de_fabricacao'])
            dateValidade = date.fromisoformat(item['data_de_validade'])
            if(oldestDate > dateFabricacao):
                oldestDate = dateFabricacao
            if(closest_date <  date.today() < dateValidade):
                closest_date = dateValidade
        company_bigger_stock = Counter(empresas).most_common()
        string_lista = (
            f"Data de fabricação mais antiga: {oldestDate}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock[0][0]}"
        )
        return string_lista
