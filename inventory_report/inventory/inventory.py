import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def reader_csv(file):
    with open(file) as csv_file:
        CSVreader = csv.reader(csv_file, delimiter=",", quotechar='"')
        header, *data = CSVreader

    listDataCSV = []

    for item in data:
        product = {}
        for i in range(len(item)):
            product.update({header[i]: item[i]})
        listDataCSV.append(product)
    return listDataCSV


def reader_json(file):
    with open(file) as json_file:
        content = json_file.read()
        return json.loads(content)


class Inventory:
    def import_data(file, report_type):
        type_file = file.split('.')[-1]
        listData = []
        if(type_file == 'csv'):
            listData = reader_csv(file)
        if(type_file == 'json'):
            listData = reader_json(file)
        if(type_file == 'xml'):
            with open(file) as xml_file:
                doc = xmltodict.parse(xml_file.read())
                listData = doc['dataset']['record']
        if(report_type == "simples"):
            relatorio_simples = SimpleReport()
            return relatorio_simples.generate(listData)
        else:
            relatorio_completo = CompleteReport()
            return relatorio_completo.generate(listData)
