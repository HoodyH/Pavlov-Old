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