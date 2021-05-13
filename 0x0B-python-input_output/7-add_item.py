#!/usr/bin/python3
"""module for functions"""


import json
import sys


saveJason = __import__('5-save_to_json_file').save_to_json_file
loadJason = __import__('6-load_from_json_file').load_from_json_file
argitems = []
for i in range(1, len(sys.argv)):
    argitems.append(str(sys.argv[i]))
try:
    with open("add_item.json", mode="x") as BourneLegacy:
        saveJason(argitems, "add_item.json")
except:
    saveJason(loadJason("add_item.json") + argitems, "add_item.json")
