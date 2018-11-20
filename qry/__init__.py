from .continuousquery import ContinuousQuery
from .countsquery import CountsQuery
from .totalsquery import TotalsQuery
from .nullquery import NullQuery

QUERIES = {
    'counts': CountsQuery,
    'freqs': CountsQuery,
    'totals': TotalsQuery,
    'continuous': ContinuousQuery
}


def queryCodebook(codebook, query_name):
    qry = QUERIES.get(query_name, NullQuery)(codebook)
    return qry.getData()
