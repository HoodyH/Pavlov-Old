import json
import os


base_dir_stograge = "data"

def loadJson(file_name, dir):
    """
    _scope: "discord" or "telegram"
    _guild: "guild id (discord), or channel id (telegram)"
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    full_path = "{}/{}.json".format(dir, file_name)
    try:
        json_obj = json.loads(open(full_path).read())
    except:
        read_path = "data_global/{}_global.json".format(file_name)
        json_obj = json.loads(open(read_path).read())

        file = open(full_path, "w")
        data = json.dumps(json_obj, indent=4)
        file.write(data)
        file.close()

    return json_obj


example_mat =   [
        [0, "global", ["hello","ciao","bella"], ["Yooo", "Yeyy", "bruuu"], ["merda"], ["non dire queste cose"], ["Buongiorno", "buongiornissimo"], ["Ma vai via"], "None"],
        [0, "global", ["pt"], ["PT", "PPT", "PTPT"], [""], [""], ["PPPT", "PTPTPT"], ["PPPPPPPPPPTTTTTTTTTT"], "None"]
    ]

def _private_create_reply_file():
    
    global example_mat
    json_obj = {}
    num = 0
    for el in example_mat:
        num += 1
        field = json_obj[num] = {}
        field["output_counter"] = el[0]
        field["scope"] = el[1]
        field["standard_triggers"] = el[2]
        field["standars_outputs"] = el[3]
        field["avoiders"] = el[4]
        field["avoid_outputs"] = el[5]
        field["power_triggers"] = el[6]
        field["power_outputs"] = el[7]
        field["author"] = el[8]

    data = json.dumps(json_obj, indent=4)
    file = open("skills/skills_data/situational_respond.json", "w")
    file.write(data)
    file.close()
    return json_obj


