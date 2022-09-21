import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory:
    def import_data(file, report_type):
        with open(file) as csv_file:
            CSVreader = csv.reader(csv_file, delimiter=",", quotechar='"')
            header, *data = CSVreader
        
        listData = []
        for item in data:
            product = {}
            for i in range(len(item)):
                product.update({header[i]: item[i]})
            listData.append(product)

        if(report_type == "simples"):
            relatorio_simples = SimpleReport()
            return relatorio_simples.generate(listData)
        else:
            relatorio_completo = CompleteReport()
            return relatorio_completo.generate(listData)