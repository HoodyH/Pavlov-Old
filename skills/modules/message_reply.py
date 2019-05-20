from skills.utils.file_handler import loadJson
from skills.utils.select_handler import random_between

#is global cause i dont wanna read the file every private message
s_resp_global = loadJson("data_global", "situational_reply_global") 

class Respond(object):
    
    global s_resp_global

    """
    it expects an array of words as input.
    """
    def __init__(self,
                text_array,
                scope,
                guild,
                **kwargs):
        self.text_array = text_array

        if guild is not None:
            path = "data/{}/{}".format(scope, guild)
            self.s_resp_json = loadJson(path, "situational_reply")
        else:
            self.s_resp_json = s_resp_global

        self.output_counter = None
        self.scope = None
        self.standard_triggers = None
        self.standard_outputs = None
        self.avoid_triggers = None
        self.avoid_outputs = None
        self.power_triggers = None
        self.power_outputs = None
        self.author = None

        self.output = []


    def _update_category(self, key):

        _vars = [
            "output_counter", 
            "scope", 
            "standard_triggers", 
            "standard_outputs", 
            "avoid_triggers", 
            "avoid_outputs", 
            "power_triggers",
            "power_outputs",
            "author",
        ]

        for var_name in _vars:
            try:
                setattr(self, var_name, self.s_resp_json[key][var_name])
            except:
                setattr(self, var_name, None)


    def message_reply(self, word, word_index):

        def control(trigger, vet_outputs):
            
            trigger_array = trigger.upper().split()

            for i in range (0, len(trigger_array)):
                
                if(word_index+i > len(self.text_array)-1):
                    #if i'm at the end of the sentence then abort
                    return
                if trigger_array[i] != self.text_array[word_index+i].upper():
                    #if in the array a word dont match then abort
                    return

            if self.find_avoiders():
                self.output = vet_outputs[random_between(0, len(vet_outputs))]
            else:
                self.output.append(vet_outputs[random_between(0, len(vet_outputs))])
            return

        #look if there are the custom words
        for key in self.s_resp_json.keys():
            self._update_category(key)

            for trigger in self.standard_triggers: 
                control(trigger, self.standard_outputs)

            for trigger in self.power_triggers:  
                control(trigger, self.power_outputs)

        return


    def find_avoiders(self):
        
        for word in self.text_array:
            for avoider in self.avoid_triggers:
                if avoider.upper() == word.upper():
                    return True
        return False


    def get_reply(self):
        
        out = ""
        for el in set(self.output):
            out += el + "\n"
        return out


