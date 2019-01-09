import xml.etree.ElementTree


def load_xml(filename):
    return xml.etree.ElementTree.parse(filename).getroot()


def write_xml(filename, data):
    data.write(filename)


