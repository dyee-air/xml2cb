from .nullexporter import NullExporter
from .csvexporter import CsvExporter

EXPORTERS = {
    'csv': CsvExporter,
    'null': NullExporter
}

EXPORTERS.setdefault('null')


def exportData(mode, data, outfile=None, noheader=False, custom_header=None):
    exporter = EXPORTERS[mode](data=data, outfile=outfile, noheader=noheader)
    exporter.header = custom_header or exporter.header
    exporter.export()
