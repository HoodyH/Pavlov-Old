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

        def control(trigger, vet_outputs, key, scope):
            
            trigger_array = trigger.upper().split()

            for i in range (0, len(trigger_array)):
                
                if(word_index+i > len(self.text_array)-1):
                    #if i'm at the end of the sentence then abort
                    return
                if trigger_array[i] != self.text_array[word_index+i].upper():
                    #if in the array a word dont match then abort
                    return

            sentence = []
            sentence.append(key)
            if self.find_avoiders():
                sentence.append(0)
                sentence.append(self.avoid_outputs[random_between(0, len(self.avoid_outputs))])
            else:
                if scope == "power":
                    sentence.append(2)
                else:
                    sentence.append(1)
                sentence.append(vet_outputs[random_between(0, len(vet_outputs))])        

            self.output.append(sentence)
            return

        #look if there are the custom words
        for key in self.s_resp_json.keys():
            self._update_category(key)

            for trigger in self.standard_triggers: 
                control(trigger, self.standard_outputs, key, "standard")

            for trigger in self.power_triggers:  
                control(trigger, self.power_outputs, key, "power")

        return


    def find_avoiders(self):
        
        for word in self.text_array:
            for avoider in self.avoid_triggers:
                if avoider.upper() == word.upper():
                    return True
        return False


    def get_reply(self):
        
        print(self.output)
        key = None
        index = 0

        for el in self.output:
            if key is None:
                key = el[0]

        out_0 = ""
        out_1 = ""
        out_2 = ""
        for el in self.output:
            if el[1] == 0:
                out_0 += str(el[2]) + "\n"
            if el[1] == 1:
                out_1 += str(el[2]) + "\n"
            if el[1] == 2:
                out_2 += str(el[2]) + "\n"

        if len(out_0) != 0:
            return out_0
        if len(out_2) != 0:
            return out_2
        if len(out_1) != 0:
            return out_1
        return ""


