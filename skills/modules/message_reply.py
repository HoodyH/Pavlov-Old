from skills.utils.file_handler import loadJson
from skills.utils.select_handler import random_between

class Respond(object):

    def __init__(self,
                array,
                scope,
                guild,
                **kwargs):
        self.array = array

        self.output = []

        if guild is not None:
            path = "data/{}/{}".format(scope, guild)
            self.s_resp_json = loadJson("situational_reply", path)
        else:
            self.s_resp_json = loadJson("situational_reply_global", "data_global")

    def find_keywords(self, word):
        
        def control(trigger, key, output_type):
            if trigger.upper() == word.upper():

                avoid = self.find_avoiders(self.s_resp_json[key]["avoiders"])
                if avoid:
                    vet_out = self.s_resp_json[key]["avoid_output"]
                    self.output = vet_out[random_between(0, len(vet_out))]
                else:
                    vet_out = self.s_resp_json[key][output_type]
                    self.output.append(vet_out[random_between(0, len(vet_out))])

            return

        #look if there are the custom words
        for key in self.s_resp_json.keys():

            for trigger in  self.s_resp_json[key]["standard_triggers"]:  
                control(trigger, key, "standars_outputs")

            for trigger in  self.s_resp_json[key]["power_triggers"]:  
                control(trigger, key, "power_outputs")

        return


    def find_avoiders(self, avoiders):
        
        for word in self.array:
            for avoider in avoiders:
                if avoider.upper() == word.upper():
                    return True
        return False


    def get_message(self):
        
        out = ""
        for el in self.output:
            out += el + ".\n"
        return out


