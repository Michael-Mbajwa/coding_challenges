import xml.etree.ElementTree as ET

def timestamps_by_description(xml, description):
    """
    From my coding Test with NextGate Tech
    Given an xml string and description, return the timestamp of the accompanying description in a list.
    """
    result = []
    root = ET.fromstring(xml)
    for event in root.findall('event'):
        description2 = str(event.find('description').text)
        if description2 == description:
            result.append(int(event.attrib['timestamp']))
    
    return result

xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <event timestamp="1614285589">
        <description>Intrusion detected</description>
    </event>
    <event timestamp="1614286432">
        <description>Intrusion ended</description>
    </event>
</log>"""
print(timestamps_by_description(xml, 'Intrusion ended'))