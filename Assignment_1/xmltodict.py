"""
Minimal xmltodict replacement for the FSMD simulator.
Converts XML to nested OrderedDict, matching the xmltodict.parse() API.
"""
from collections import OrderedDict
import xml.etree.ElementTree as ET


def parse(xml_string):
    """Parse an XML string and return an OrderedDict."""
    root = ET.fromstring(xml_string)
    return OrderedDict([(root.tag, _element_to_dict(root))])


def _element_to_dict(element):
    """Recursively convert an XML element to an OrderedDict."""
    result = OrderedDict()

    # Process child elements
    children = list(element)
    if not children:
        # Leaf node: return text content (or None if empty)
        text = element.text
        if text is not None:
            text = text.strip()
            if text == '':
                return None
            return text
        return None

    # Group children by tag
    child_tags = OrderedDict()
    for child in children:
        tag = child.tag
        if tag not in child_tags:
            child_tags[tag] = []
        child_tags[tag].append(child)

    for tag, elements in child_tags.items():
        if len(elements) == 1:
            result[tag] = _element_to_dict(elements[0])
        else:
            result[tag] = [_element_to_dict(e) for e in elements]

    return result
