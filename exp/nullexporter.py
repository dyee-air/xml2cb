from .abstract import AbstractExporter


class NullExporter(AbstractExporter):

    def export(self):
        print(self.data)

    def write(self, outfile):
        pass
