from abc import ABC, abstractmethod, abstractproperty


class AbstractQuery(ABC):

    def __init__(self, codebook):
        self._codebook = codebook
        self._data = self._buildData()

    @abstractproperty
    def columns(self):
        pass

    @abstractmethod
    def _buildData(self):
        pass

    def getData(self):
        return self._data[self.columns]
