

def destring(val):
    """
    Attempts to convert `val` to a numeric type if it is a string.
    Returns `val` if it cannot be converted (or if it is not a string).

    Parameters
    ----------
    val : object
        The object to be converted.

    Returns
    -------
    int, float, or type(val)

    """

    if isinstance(val, str):
        if val.lstrip('-').isdecimal():
            return int(val)

        if val.lstrip('-').replace('.', '', 1).isdecimal():
            return float(val)

    return val


def convertRows(row_list):
    """
    Converts a dictionary of `column: value` pairs to a dictionary with
    elements of the form `column: [value0, value1, value2,...]` suitable
    for constructing a pandas dataframe.

    Parameters
    ----------
    row_list : list
        A list of dictionaries of the form
            [{col0: val0, col1: val0, col2: val0, ...},
             {col0: val1, col1: val1, col2: val1, ...},
              ...
             {col0: valN, col1: valN, col2: valN, ...}]


    Returns
    -------
    dict
        A single dictionary of the form
            {col0: [val0, val1, ..., valN],
             col1: [val0, val1, ..., valN],
             ...
            }
    """

    col_dict = dict()
    for col_name in row_list[0].keys():
        col_dict[col_name] = [row[col_name] for row in row_list]

    return col_dict
