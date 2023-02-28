#!/usr/bin/python3
import sys, json, os, errno
from from_web import to_json, is_url

folder = "reformated"

if len(sys.argv) >= 1:
    print("\nPlease wait...\n", end="")
    try:
        for i in range(1, len(sys.argv)):
            if is_url(sys.argv[i]) is True:
                to_json(sys.argv[i])

        for i in range(1, len(sys.argv)):
            with open(sys.argv[i], 'r') as json_file:
                json_object = json.load(json_file)

            filename = "{}/{}".format(folder, sys.argv[i])
            print("Will be created at \"{}\"".format(filename))
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            with open(filename, 'w', encoding="utf-8") as a_files:
                a_files.write(json.dumps(json_object, indent=2))
                print("Done.\n--")
    except Exception:
        print("\nSome files might not be reformated.")
        print("Please refer {}/{}/ or".format(os.getcwd(), folder))
        print("{}/{}/ for more.".format(os.getcwd(), "url_to_json"))
