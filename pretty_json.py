#!/usr/bin/python3
""" Formats the view of senseless json file """
import json
import sys
import json as js

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv) - 1):
        with open(sys.argv[i], 'r') as json_file:
            json_object = json.load(json_file)
        filename = sys.argv[i]
        with open(filename, 'w', encoding="utf-8") as a_files:
            a_files.write(js.dumps(json_object, indent=2))
