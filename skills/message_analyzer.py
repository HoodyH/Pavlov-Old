
from skills.modules.message_reply import Respond
from skills.utils.file_handler import loadJson

message_max_lenght = 70

config_global = loadJson("data_global","config_global")
commands_global = loadJson("data_global", "commands_global")

class Analyze(object): 

        global config_global
        global commands_global

        def __init__(self, scope, guild, user_id, **kwargs):

                self.scope = scope
                self.guild = guild
                self.user_id = user_id

                if guild is not None:
                        path = "data/{}/{}".format(scope, guild)
                        self.config = loadJson(path, "config")
                        self.commands = loadJson(path, "commands")
                else:
                        self.config = config_global
                        self.commands = commands_global

        def _update_config(self):
                
                self.prefix = self.config["prefix"]
                self.quiet_prefix = self.config["quiet_prefix"]
                self.sudo_prefix = self.config["sudo_prefix"]
                self.languages = self.config["languages"]
                self.modules_status = self.config["modules_status"]
                return

        def _update_command(self, key, language):
                
                self.dm_enabled = self.commands[key]["dm_enabled"]
                self.permissions = self.commands[key]["dm_enabled"]
                self.invocation = self.commands[key][language]["invocation"]
                self.manual = self.commands[key][language]["invocation"]
                return


        def _module_status(self, module_name, prefix_mode):
                """
                read in the appropriate json if the module is active
                """
                enabled = self.modules_status[module_name]["enabled"]
                status = self.modules_status[module_name]["status"]

                if prefix_mode == "SUDO":
                        return True
                if enabled == 0:
                        return False
                if status == 1 and prefix_mode == "QUIET":
                        return True
                if status == 2:
                        return True
                return False
        

        def _command_executer(self):
                """
                read language/languages of the guild.
                find if there's a command of send an error.
                execute the command in the module.
                """
                
                return        


        def analyze(self, text):

                self._update_config()

                #ceck if this text is a command
                if str.startswith(text, self.prefix):
                        self._command_executer()


                #ceck the prefix executer type SUDO OR QUIET
                prefix_mode = None
                if str.startswith(text, self.quiet_prefix):
                        text = text[1:]
                        prefix_mode = "QUIET"
                if str.startswith(text, self.sudo_prefix):
                        text = text[1:]
                        prefix_mode = "SUDO"


                if len(text) > message_max_lenght:
                        return

                text_array = text.split()
                respond = Respond(text_array, self.scope, self.guild)

                index = 0
                for word in text_array:
                        
                        if self._module_status("message_reply", prefix_mode):
                                respond.message_reply(word, index)

                        index += 1
                        
                return respond.get_reply()

        