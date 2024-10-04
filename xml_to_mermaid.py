import xml.etree.ElementTree as ET
import sys

def xml_to_mermaid(xml_file, mermaid_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def process_element(element, parent=None):
        node_id = element.tag
        nodes.add(node_id)

        if parent:
            edges.append((parent, node_id))

        for child in element:
            process_element(child, node_id)
        
    nodes = set()
    edges = []

    process_element(root)

    with open(mermaid_file, 'w') as f:
        f.write('graph TD\n')
        for node in nodes:
            f.write(f'    {node}[{node}]\n')
        
        for parent, child in edges:
            f.write(f'    {parent} --> {child}\n')

if len(sys.argv) != 3:
    print("Usage: python xml_to_mermaid.py input.xml output.mmd")
    sys.exit(1)

xml_to_mermaid(sys.argv[1], sys.argv[2])
