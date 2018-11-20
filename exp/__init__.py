import warnings
from .nullexporter import NullExporter
from .csvexporter import CsvExporter

EXPORTERS = {
    'csv': CsvExporter
}


def exportData(format_name, data, outfile=None, header=True):
    export_cls = NullExporter

    if format_name:
        try:
            export_cls = EXPORTERS[format_name.lower()]
        except KeyError:
            warnings.warn(
                "Format '{}' not found.  Printing output to stdout.".format(format_name))

    exporter = export_cls(data=data, outfile=outfile, header=header)
    exporter.export()
