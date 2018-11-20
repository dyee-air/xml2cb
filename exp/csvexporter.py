from .abstract import AbstractExporter


class CsvExporter(AbstractExporter):

    def write(self, outfile):
        self.data.to_csv(outfile, header=self.header, index=False)
