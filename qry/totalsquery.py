from .abstract import AbstractQuery


class TotalsQuery(AbstractQuery):

    @property
    def columns(self):
        return ['fieldnum', 'fieldname', 'type', 'block', 'item',
                'fieldlabel', 'datafreq']

    def _buildData(self):
        df = self._codebook.data.loc[
            (self._codebook.data.format == 'numeric') &
            (self._codebook.data.type == 'discrete')
        ]
        df = df[self.columns]

        return df.groupby(list(df.columns[:-1]), as_index=False).agg('sum')
