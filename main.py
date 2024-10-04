import xml.etree.ElementTree as ET
import sys

def parse_menu(menu_element):
    menu_name = menu_element.find("Name").text
    call_handling = menu_element.find("CallHandling")
    edges = []

    if call_handling is not None:
        for digit_key_input in call_handling.findall("DigitKeyInput"):
            key = digit_key_input.find("Key").text
            action = digit_key_input.find("Action").text
            destination = digit_key_input.find("Destination").text if digit_key_input.find("Destination") is not None else ""
            edges.append(f'{menu_name} --> {key}: {action} to {destination}')

        for special_key_input in call_handling.findall("SpecialKeyInput"):
            key = special_key_input.find("Key").text
            action = special_key_input.find("Action").text
            edges.append(f'{menu_name} --> {key}: {action}')

        no_input = call_handling.find("NoInput")
        if no_input is not None:
            action = no_input.find("Action").text
            destination = no_input.find("Destination").text if no_input.find("Destination") is not None else ""
            edges.append(f'{menu_name} --> No Input: {action} to {destination}')

    return edges

def xml_to_mermaid(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    edges = []

    for menu in root.findall("Menu"):
        edges.extend(parse_menu(menu))

    mermaid_script = "graph TD;\n"
    mermaid_script += ";\n".join(edges)
    return mermaid_script

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: xml_to_mermaid.py <xml_file_path>")
        sys.exit(1)

    xml_file_path = sys.argv[1]
    mermaid_script = xml_to_mermaid(xml_file_path)
    print(mermaid_script)
