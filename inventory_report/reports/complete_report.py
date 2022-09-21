from inventory_report.reports.simple_report import SimpleReport
from datetime import date
from collections import Counter


def aux(lista):
    oldestDate = date.today()
    closest_date = date.min
    empresas = []
    for item in lista:
        empresas.append(item['nome_da_empresa'])
        dateFabricacao = date.fromisoformat(item['data_de_fabricacao'])
        dateValidade = date.fromisoformat(item['data_de_validade'])
        if(oldestDate > dateFabricacao):
            oldestDate = dateFabricacao
        if(closest_date < date.today() < dateValidade):
            closest_date = dateValidade
    return [empresas, oldestDate, closest_date]


class CompleteReport(SimpleReport):
    def generate(self, lista):
        # oldestDate = date.today()
        # closest_date = date.min
        # empresas = []
        # for item in lista:
        #     empresas.append(item['nome_da_empresa'])
        #     dateFabricacao = date.fromisoformat(item['data_de_fabricacao'])
        #     dateValidade = date.fromisoformat(item['data_de_validade'])
        #     if(oldestDate > dateFabricacao):
        #         oldestDate = dateFabricacao
        #     if(closest_date < date.today() < dateValidade):
        #         closest_date = dateValidade
        empresas, oldestDate, closest_date = aux(lista)
        print(empresas)
        counter_emp = Counter(empresas)
        company_bigger_stock = counter_emp.most_common()
        produtos_empresa = []
        list_empresas = []
        for empresa in empresas:
            if empresa not in list_empresas:
                list_empresas.append(empresa)
        for empresa in list_empresas:
            produtos_empresa.append(f'- {empresa}: {counter_emp[empresa]}\n')
        string_lista = [
            f"Data de fabricação mais antiga: {oldestDate}\n",
            f"Data de validade mais próxima: {closest_date}\n",
            f"Empresa com mais produtos: {company_bigger_stock[0][0]}\n",
            "Produtos estocados por empresa:\n",
        ]
        final_string = ''.join(string_lista + produtos_empresa)
        return final_string
