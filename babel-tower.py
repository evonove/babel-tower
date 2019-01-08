import sys
import os

import csv
from lxml import etree


def apply_translations(csv_path, xml_path, from_lang_key, to_lang_key):
    # Reads csv
    csv_file = open(csv_path, "r")
    reader = csv.DictReader(csv_file, delimiter=";")

    # Verifies both languages are present in read csv
    if from_lang_key not in reader.fieldnames:
        print(f"'{from_lang_key}' not found in '{os.path.basename(csv_path)}'")
        return

    if to_lang_key not in reader.fieldnames:
        print(f"'{to_lang_key}' not found in '{os.path.basename(csv_path)}'")
        return

    # Parses xml
    tree = etree.parse(xml_path)
    context_list = tree.findall("context")

    for context in context_list:
        if context.find("name").text == "CardsData":
            # Saves all message elements for faster lookup
            messages = {}
            for message in context.findall("message"):
                text = "\\n".join(message.find("source").text.split("\n"))
                messages[text] = message
            break

    for line in reader:
        # Skips empty lines
        if line[from_lang_key] == "":
            continue

        from_text = line[from_lang_key]
        to_text = line[to_lang_key].strip()

        message = messages.get(from_text)

        if message is not None:
            tr = message.find("translation")
            tr.text = to_text
            # Marks current translation as done
            tr.attrib.pop("type")

    tree.write(xml_path, encoding="utf-8", pretty_print=True)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage:")
        print("babel-tower.py <csv_file> <xml_file> <from> <to>")
        print("<from> and <to> must be the name of columns contained in <csv_file>")
        exit()

    apply_translations(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
