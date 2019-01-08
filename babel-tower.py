import sys

import csv
from lxml import etree


def apply_translations(csv_path, xml_path):
    tree = etree.parse(xml_path)
    csv_file = open(csv_path, "r")
    reader = csv.reader(csv_file, delimiter=";")

    context_list = tree.findall("context")

    for context in context_list:
        if context.find("name").text == "CardsData":
            messages = context.findall("message")
            break

    for line in reader:
        # Skips header
        if reader.line_num == 0:
            continue

        # Skips empty lines
        if line[0] == "":
            continue

        english_text = line[5]
        german_text = line[6].strip()

        for message in messages:
            found_text = "\\n".join(message.find("source").text.split("\n"))
            if found_text == english_text:
                tr = message.find("translation")
                tr.text = german_text
                # Marks current translation as done
                tr.attrib.pop("type")

    tree.write(xml_path, encoding="utf-8", pretty_print=True)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("babel-tower.py <csv_file> <xml_file>")
        exit()

    apply_translations(sys.argv[1], sys.argv[2])
