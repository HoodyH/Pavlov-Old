
from skills.modules.message_reply import Respond

message_max_lenght = 70

def find_match(text, scope, guild):
         
        string = str(text)
        
        if len(string) > message_max_lenght:
                return

        array = string.split()
        respond = Respond(array, scope, guild)

        for word in array:
                respond.find_keywords(word)
                
        return respond.get_message()

        