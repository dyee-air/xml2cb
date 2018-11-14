from .util import destring


class CodebookElement(object):
    def __init__(self, xml_element):

        self._xml_element = xml_element
        self._children = list()

    #------- Properties --------#

    @property
    def xml_element(self):
        return self._xml_element

    @property
    def children(self):
        return self._children

    #------- Hierarchy methods --------#

    def addChild(self, new_child):
        self._children.append(new_child)

    def removeChild(self, child):
        if child in self._children:
            self._children.remove(child)

    def listChildren(self):
        return self.children

    def listAllChildren(self):
        return self.children + [elem
                                for child in self.children
                                for elem in child.listAllChildren()]

    def find(self, tag):
        try:
            return self.findall(tag)[0]
        except IndexError:
            return None

    def findall(self, tag):
        return [child for child in self.listAllChildren() if child.tag == tag]

    #------- Utilities --------#

    def get(self, attr_name, default=None):
        try:
            val = getattr(self, attr_name)
        except AttributeError:
            return default

        return destring(val)

    def listColumns(self, include_children=True):
        if include_children and self.children:
            return list(self.xml_element.attrib.keys()) + self.listChildColumns()

        return list(self.xml_element.attrib.keys())

    def listChildColumns(self):
        if self.children:
            return list(dict.fromkeys(
                [col for child in self.children
                 for col in child.listColumns()]
            ))

        return list()

    #------- Data retrieval  --------#

    def _getData(self, col_names):
        return {col: self.get(col)
                for col in col_names
                if col in self.listColumns(include_children=False)}

    def getRows(self, col_names=None):
        """
        Returns a list of dictionaries with {column name: value} as elements.

        Parameters
        ----------
        col_names : list
            List of strings corresponding to column names.  If not
            supplied, returns all available columns.

        Returns
        -------
        dict
            See above
        """

        cols = col_names or self.listColumns()

        # Return empty list if columns don't exist in self or children
        if not any([col in self.listColumns() for col in cols]):
            return list()

        # Identify columns specific to this element
        my_cols = [col
                   for col in cols
                   if col in self.listColumns(include_children=False)]

        # Set up full column dictionary and update with values from
        # this element
        my_data = dict.fromkeys(cols)
        my_data = my_data.update(self._getData(my_cols)) or my_data

        # Remove columns that were found in this element
        new_cols = [col
                    for col in cols
                    if col not in my_cols]

        # Pass remaining columns to children (may return empty)
        child_rows = [my_data.update(child_dict) or my_data.copy()
                      for child in self.children
                      for child_dict in child.getRows(col_names=new_cols)]

        return child_rows or [my_data]

    #------- Internal overrides  --------#

    def __getattr__(self, attr_name):
        try:
            return self.xml_element.attrib[attr_name]
        except KeyError:
            try:
                return getattr(self.xml_element, attr_name)
            except AttributeError:
                raise AttributeError(
                    "'{0}' has no attribute '{1}' (on self or self.xml_element)".format(
                        self.__repr__(), attr_name)
                )

    def __getitem__(self, index):
        return self._children[index]

    def __repr__(self):
        return "<{0} '{1}' at {2}>".format(
            self.__class__.__name__, self.xml_element.tag, id(self)
        )
