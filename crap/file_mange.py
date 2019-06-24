import json
import sys

def _private_format_json(full_path):
        
    json_obj = json.loads(open(full_path).read())
    file = open(full_path, "w")
    data = json.dumps(json_obj, indent=4)
    file.write(data)
    file.close()

def add_reply():

    file_name = "crap/data_to_appens.json"

    try:
        json_obj = json.loads(open(file_name).read())
    except:
        file = open(file_name, "w")
        json_obj = {}
        data = json.dumps(json_obj, indent=4)
        file.write(data)
        file.close()

    print("Enter the category of this reply asset")
    category_name = sys.stdin.read()
    field = json_obj[category_name] = {}
    print()

    field["output_counter"] = 0

    print("Scope, defult: global")
    scope = sys.stdin.read()
    if scope == "":
        scope = "global"
    field["_scope"] = scope
    print()
    
    print("Standard triggers [comma separated, no spaces between commas]")
    standard_triggers = sys.stdin.read()
    field["standard_triggers"] = standard_triggers.split(",")
    print()

    print("Standard outputs [comma separated, no spaces between commas]")
    standars_outputs = sys.stdin.read()
    field["standars_outputs"] = standars_outputs.split(",")
    print()
    
    print("Avoiders [comma separated, no spaces between commas]")
    avoiders = sys.stdin.read()
    field["avoiders"] = avoiders.split(",")
    print()

    print("Avoid outputs [comma separated, no spaces between commas]")
    avoid_outputs = sys.stdin.read()
    field["avoid_outputs"] = avoid_outputs.split(",")
    print()

    print("Power triggers [comma separated, no spaces between commas]")
    power_triggers = sys.stdin.read()
    field["power_triggers"] = power_triggers.split(",")
    print()

    print("Power outputs [comma separated, no spaces between commas]")
    power_triggers = sys.stdin.read()
    field["power_triggers"] = power_triggers.split(",")
    print()

    print("Author, it will be shown as cit. Default: None")
    author = sys.stdin.read()
    if author == "":
        author = "None"
    field["author"] = author
    print()
    print("You can run this program many time you want and it will continue append to the file")

    data = json.dumps(json_obj, indent=4)
    file = open(file_name, "w")
    file.write(data)
    file.close()

add_reply()