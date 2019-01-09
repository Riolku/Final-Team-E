import xml.etree.ElementTree as ET


def load_xml(filename):
    return ET.parse(filename)


def write_xml(filename, data):
    data.write(filename)


