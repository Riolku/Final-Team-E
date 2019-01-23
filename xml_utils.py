# File for XML utilities

# import xml library
import xml.etree.ElementTree


# Load xml utility function
def load_xml(filename):
    return xml.etree.ElementTree.parse(filename).getroot()