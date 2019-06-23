from core.src.settings import *
import json
import os

base_dir_storage = "data"


def load_json(directory, file_name):
    """
    _scope: "discord" or "commands"
    _guild: "guild id (discord), or channel id (commands)"
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    full_path = "{}/{}.json".format(directory, file_name)

    try:
        json_obj = json.loads(open(full_path).read())
    except Exception as e:
        print(e)
        read_path = "data_global/{}_global.json".format(file_name)
        json_obj = json.loads(open(read_path).read())

        file = open(full_path, "w")
        data = json.dumps(json_obj, indent=4)
        file.write(data)
        file.close()

    return json_obj


# global files that must be always loaded
situational_reply_global = load_json("data_global", "situational_reply_global")


def load(scope, guild, file_name):

    if guild is not None and USE_GLOBAL_FILE_ONLY is False:
        path = "data/{}/{}".format(scope, guild)
        return load_json(path, file_name)
    elif file_name == "situational_reply":
        return situational_reply_global


commands = load_json("core/commands/commands_declaration", "commands")
commands_shortcut = load_json("core/commands/commands_declaration", "commands_shortcut")


def load_commands():
    return commands


def load_commands_shortcut():
    return commands_shortcut


def save(scope, guild, file_name, json_obj):

    if guild is not None and USE_GLOBAL_FILE_ONLY is False:
        path = "data/{}/{}/{}.json".format(scope, guild, file_name)
    else:
        path = "data_global/{}_global.json".format(file_name)

    data = json.dumps(json_obj, indent=4)
    file = open(path, "w")
    file.write(data)
    file.close()


# log data to a text file locally
def log_data(data):
    log = open("data.log", "a")
    log.write(str(data)+"\r\n")
    log.close()


example_mat = [
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
        field["_scope"] = el[1]
        field["standard_triggers"] = el[2]
        field["standars_outputs"] = el[3]
        field["avoiders"] = el[4]
        field["avoid_outputs"] = el[5]
        field["power_triggers"] = el[6]
        field["power_outputs"] = el[7]
        field["author"] = el[8]

    data = json.dumps(json_obj, indent=4)
    file = open("core/skills_data/situational_respond.json", "w")
    file.write(data)
    file.close()
    return json_obj


