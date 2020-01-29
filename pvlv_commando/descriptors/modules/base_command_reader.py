class BaseCommandReader(object):
    def __init__(self):
        self.module = None  # the module where is member of
        self.name = None  # the name of the command

        self.max_invocations = None  # max uses for a single user

        self.key = None
        self.invocation_words = None
        self.description = None
        self.examples = None

    @staticmethod
    def __read_language(language, module):
        module_language = module.get(language)
        if module_language is None:
            module_language = module.get('eng')
            if module_language is None:
                raise Exception('There is not language descriptions in this command')
        return module_language
