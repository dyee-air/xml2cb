from .abstract import AbstractQuery


class CountsQuery(AbstractQuery):

    @property
    def columns(self):
        return ['fieldnum', 'fieldname', 'type', 'block', 'item',
                'fieldlabel', 'formatlabel', 'datavalue', 'datafreq']

    def _buildData(self):
        df = self._codebook.data.loc[
            (self._codebook.data.format == 'numeric') &
            (self._codebook.data.type == 'discrete')
        ]

        return df
