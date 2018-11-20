from abc import ABC, abstractmethod


class AbstractExporter(ABC):

    def __init__(self, data, outfile=None, header=True):
        self.data = data
        self.outfile = outfile
        self.header = header

    def export(self):
        with open(self.outfile, 'w', newline='') as outfile:
            self.write(outfile)

    @abstractmethod
    def write(self, outfile):
        pass
