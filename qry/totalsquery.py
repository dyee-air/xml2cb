import pandas as pd
from .abstract import AbstractQuery


class TotalsQuery(AbstractQuery):

    @property
    def columns(self):
        return ['fieldnum', 'fieldname', 'type', 'block', 'item',
                'fieldlabel', 'nummiss', 'datafreq']

    def _buildData(self):
        df = self._codebook.data.loc[
            (self._codebook.data.format == 'numeric') &
            (self._codebook.data.type == 'discrete')
        ][self.columns]

        totals = df[['fieldnum', 'datafreq']].groupby(
            ['fieldnum'], as_index=False).agg('sum')

        return pd.merge(df[df.columns[:-1]].drop_duplicates(), totals, how='left', on=['fieldnum'])
