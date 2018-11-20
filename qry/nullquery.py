from .abstract import AbstractQuery


class NullQuery(AbstractQuery):

    @property
    def columns(self):
        return list(self._codebook.data.columns)

    def _buildData(self):
        return self._codebook.data
