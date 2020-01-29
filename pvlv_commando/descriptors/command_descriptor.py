import json
from pvlv_commando.descriptors.modules.base_command_reader import BaseCommandReader


class CommandDescriptor(BaseCommandReader):

    def __init__(self):
        super(CommandDescriptor, self).__init__()
        self.management_command = None
        self.beta_command = None
        self.pro_command = None
        self.dm_enabled = None
        self.enabled_by_default = None
        self.permissions = None

        self.handled_args = None
        self.handled_params = None

    def _read_args_and_params(self, language, dictionary):
        result = {}
        for key in dictionary.keys():
            result[key] = self.__read_language(language, dictionary.get(key))
        return result

    def read_command(self, command_descriptor_dir):

        with open(command_descriptor_dir) as f:
            file = json.load(f)

        self.management_command = file.get('management_command')
        self.beta_command = file.get('beta_command')
        self.pro_command = file.get('pro_command')
        self.dm_enabled = file.get('dm_enabled')
        self.enabled_by_default = file.get('enabled_by_default')
        self.permissions = file.get('permissions')
        self.invocation_words = file.get('invocation_words')

        # self.description = self._read_language(language, module.get('description'))
        # self.handled_args = self._read_args_and_params(language, module.get('handled_args'))
        # self.handled_params = self._read_args_and_params(language, module.get('handled_params'))
        # self.examples = module.get(language, module.get('examples'))

