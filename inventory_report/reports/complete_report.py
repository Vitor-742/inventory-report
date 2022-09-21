from inventory_report.reports.simple_report import SimpleReport
from datetime import date
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(lista):
        oldestDate = date.today()
        closest_date = date.today()
        empresas = []
        for index, item in enumerate(lista):
            empresas.append(item['nome_da_empresa'])
            dateFabricacao = date.fromisoformat(item['data_de_fabricacao'])
            dateValidade = date.fromisoformat(item['data_de_validade'])
            if(oldestDate > dateFabricacao):
                oldestDate = dateFabricacao
            if(closest_date < dateValidade < date.today() or index == 0):
                dateValidade = closest_date
        company_bigger_stock = Counter(empresas).most_common()
        string_lista = (
            f"Data de fabricação mais antiga: {oldestDate}\n"
            f"Data de validade mais próxima: {dateValidade}\n"
            f"Empresa com mais produtos: {company_bigger_stock[0][0]}"
        )
        counter_emp = Counter(empresas)
        company_bigger_stock = counter_emp.most_common()
        produtos_empresa = []
        for empresa in empresas:
            produtos_empresa.append(f'- {empresa}: {counter_emp[empresa]}\n')
        string_lista = [
            f"Data de fabricação mais antiga: {oldestDate}\n",
            f"Data de validade mais próxima: {dateValidade}\n",
            f"Empresa com mais produtos: {company_bigger_stock[0][0]}\n",
            "Produtos estocados por empresa:\n",
        ]
        produtos_empresa.pop(0)
        final_string = ''.join(string_lista + produtos_empresa)
        return final_string
