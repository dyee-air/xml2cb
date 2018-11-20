from .abstract import AbstractQuery


class ContinuousQuery(AbstractQuery):

    @property
    def columns(self):
        return ['fieldnum', 'fieldname', 'type', 'fieldlabel',
                'validn', 'minvalue', 'maxvalue', 'mean', 'stddev']

    def _buildData(self):
        df = self._codebook.data.loc[
            (self._codebook.data.format == 'numeric') &
            (self._codebook.data.type == 'continuous')
        ]

        return df
