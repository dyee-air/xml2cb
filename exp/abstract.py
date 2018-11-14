from abc import ABC, abstractmethod


class AbstractExporter(ABC):

    def __init__(self, data, outfile=None, noheader=False):
        self.data = data
        self.outfile = outfile
        self.header = list(data.columns)
        self.noheader = noheader

    def export(self):
        with open(self.outfile, 'w', newline='') as outfile:
            self.write(outfile)

    @abstractmethod
    def write(self, outfile):
        pass
