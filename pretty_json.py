#!/usr/bin/python3
import sys
import json
from json import JSONDecodeError
import os
import errno


folder = "reformated"

if len(sys.argv) >= 1:
    try:
        if len(sys.argv) == 1:
            with open(sys.argv[1], 'r') as json_file:
                json_object = json.load(json_file)
            filename = "new_{}".format(sys.argv[1])
            with open(filename, 'w', encoding="utf-8") as a_files:
                a_files.write(js.dumps(json_object, indent=2))
        for i in range(1, len(sys.argv)):
            with open(sys.argv[i], 'r') as json_file:
                json_object = json.load(json_file)

            filename = "{}/{}".format(folder, sys.argv[i])
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            with open(filename, 'w', encoding="utf-8") as a_files:
                a_files.write(json.dumps(json_object, indent=2))
    except JSONDecodeError:
        print("Some files might not be reformated.")
        print("Please check {}/{}/ for more.".format(os.getcwd(), folder))
