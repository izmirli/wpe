"""Mixins for load & dump object attributes using a variety of formats.

Some formats support only string values.
"""
import csv
import json
import pickle
import xml.etree.ElementTree as ET


class Serializable:
    """Mixin for load & dump using pickle."""

    def dump(self, filename: str):
        """Dump object attributes to file in pickle format."""
        with open(filename, 'wb') as fh:
            pickle.dump(self.__dict__, fh)

    def load(self, filename: str):
        """Load and set object attributes from file in pickle format."""
        with open(filename, 'rb') as fh:
            saved_attributes = pickle.load(fh)
            for attribute_name in self.__dict__:
                setattr(self, attribute_name, saved_attributes[attribute_name])


class JSONMixin:
    """JSON Mixin for load & dump."""

    def dump(self, filename: str):
        """Dump object attributes to file in JSON format."""
        with open(filename, 'w') as fh:
            json.dump(self.__dict__, fh)

    def load(self, filename: str):
        """Load and set object attributes from file in JSON format."""
        with open(filename, 'r') as fh:
            saved_attributes = json.load(fh)
            for attribute_name in self.__dict__:
                setattr(self, attribute_name, saved_attributes[attribute_name])


class XMLMixin:
    """XML Mixin for load & dump.

    Support only string and int values.
    """

    def dump(self, filename: str):
        """Dump object attributes to file in XML format."""
        data = ET.Element('data')
        for attr_name in self.__dict__:
            attr_type = type(self.__dict__[attr_name]).__name__
            elm = ET.SubElement(data, attr_name, attrib={'type': attr_type})
            elm.text = str(self.__dict__[attr_name])

        with open(filename, 'wb') as fh:
            fh.write(ET.tostring(data))

    def load(self, filename: str):
        """Load and set object attributes from file in XML format."""
        tree = ET.parse(filename)
        root = tree.getroot()
        saved_attributes = {}
        for child in root:
            saved_attributes[child.tag] = child.text
            if 'type' in child.attrib:
                if child.attrib['type'] == 'int':
                    saved_attributes[child.tag] = int(child.text)
        for attribute_name in self.__dict__:
            setattr(self, attribute_name, saved_attributes[attribute_name])


class CSVMixin:
    """CSV Mixin for load & dump.

    Support only string values.
    """

    def dump(self, filename: str):
        """Dump object attributes to file in CSV format."""
        fieldnames = list(self.__dict__.keys())
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(self.__dict__)

    def load(self, filename: str):
        """Load and set object attributes from file in CSV format."""
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data_row = reader.__next__()
            for attribute_name in self.__dict__:
                setattr(self, attribute_name, data_row[attribute_name])
