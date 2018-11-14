import csv
from .abstract import AbstractExporter


class CsvExporter(AbstractExporter):

    def write(self, outfile):
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)

        if not self.noheader:
            writer.writerow(self.header)

        outdf = self.data.where(self.data.notnull(), None)

        writer.writerows(outdf.values.tolist())
