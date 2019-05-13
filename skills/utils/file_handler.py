import json

base_dir_stograge = "data"
shared_file = "skills/skills_data"

def loadJson(file_name):
    global shared_file
    dir =  "{}/{}.json".format(shared_file, file_name)
    try:
        json_obj = json.loads(open(dir).read())
    except:
        file = open(dir, "w")
        json_obj = {}
        data = json.dumps(json_obj, indent=4)
        file.write(data)
        file.close()

    return json_obj



example_mat =   [
        [0, "global", ["hello","ciao","bella"], ["Yooo", "Yeyy", "bruuu"], ["merda"], ["non dire queste cose"], ["Buongiorno", "buongiornissimo"], ["Ma vai via"]],
        [0, "global", ["pt"], ["PT", "PPT", "PTPT"], [""], [""], ["PPPT", "PTPTPT"], ["PPPPPPPPPPTTTTTTTTTT"]]
    ]

def _private_create_respond_file():
    
    global example_mat
    data = {}
    num = 0
    for el in example_mat:
        num += 1
        field = data[num] = {}
        field["output_counter"] = el[0]
        field["scope"] = el[1]
        field["standard_triggers"] = el[2]
        field["standars_output"] = el[3]
        field["avoiders"] = el[4]
        field["avoid_output"] = el[5]
        field["power_triggers"] = el[6]
        field["power_outputs"] = el[7]

    json_obj = json.dumps(data, indent=4)
    file = open("skills/skills_data/situational_respond.json", "w")
    file.write(json_obj)
    file.close()
    return data

_private_create_respond_file()