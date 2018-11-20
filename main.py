import sys
from argparse import ArgumentParser
from xml.etree import ElementTree
from core import XmlCodebook
from exp import exportData
from qry import queryCodebook

PARSER = ArgumentParser()
PARSER.add_argument('infile')
PARSER.add_argument('-o', '--outfile',
                    help="Output file path", default=".\\output.txt")
PARSER.add_argument('-f', '--format', dest='outformat',
                    help="Export format", default=None)
PARSER.add_argument('-d', '--data', dest="outdata",
                    help="Dataset to output (continuous | discrete | count)", default='discrete')

FILE_PATH = "R:\\project\\DSY\\XML Codebook\\M48NT2AT.xml"
OUTFILE_PATH = "G:\\Projects\\testout.csv"


def main():

    xml_tree = ElementTree.parse(FILE_PATH)
    codebook = XmlCodebook(xml_tree.getroot())

    exportData(
        'csv', queryCodebook(codebook, 'continuous'), outfile=OUTFILE_PATH)


main()
