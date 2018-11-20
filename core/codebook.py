import pandas as pd
from .util import convertRows
from .elem import CodebookElement


def loadTree(xml_element):
    if not list(xml_element):
        return CodebookElement(xml_element)

    xml_comp = CodebookElement(xml_element)
    for child in list(xml_element):
        xml_comp.addChild(loadTree(child))
    return xml_comp


class XmlCodebook(object):

    def __init__(self, xml_root):

        self._root = loadTree(xml_root)

        self._table_keys = {
            'DataField': ['fieldname'],
            'DataCount': ['fieldname', 'datavalue'],
            'DataFormat': ['formatname', 'formatvalue']
        }
        self._tables = {
            'DataFields': self._buildTable(
                self._root.find('DataFields'), include_children=False
            ),
            'DataCounts': self._buildTable(
                self._root.find('DataFields'), element_tag='DataCount'
            ),
            'DataFormats': self._buildTable(
                self._root.find('DataFormats')
            )
        }
        self.DataFields['fieldnum'] = self.DataFields.index + 1
        self._data = self._buildData()

    @property
    def data(self):
        return self._data

    @property
    def tables(self):
        return self._tables

    def _buildTable(self, element_root, element_tag=None, include_children=True):
        name = element_tag or element_root[0].tag
        element_list = element_root.findall(name)

        key_cols = self._table_keys[name]

        data_cols = list(
            {col
             for elem in element_list
             for col in elem.listColumns(include_children=include_children)
             if col not in key_cols}
        )

        row_list = [row for elem in element_root
                    for row in elem.getRows(key_cols + data_cols)
                    if any(row[field] for field in data_cols)]
        return pd.DataFrame(convertRows(row_list))

    def _buildData(self):
        df0 = pd.merge(self.DataFields, self.DataCounts,
                       how='left', on='fieldname')
        return pd.merge(df0, self.DataFormats, how='left', left_on=['formatname', 'datavalue'], right_on=['formatname', 'formatvalue'])

    def getData(self, column_names, distinct=True):
        if distinct:
            return self._data[column_names].drop_duplicates()
        return self._data[column_names]

    def __getattr__(self, attr_name):
        try:
            return self._tables[attr_name]
        except KeyError:
            return getattr(super(), attr_name)
