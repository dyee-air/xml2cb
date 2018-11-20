from .abstract import AbstractExporter


class NullExporter(AbstractExporter):

    def export(self):
        print(self.data.to_string(header=self.header))

    def write(self, outfile):
        pass
