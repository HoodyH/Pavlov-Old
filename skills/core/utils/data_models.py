
CONFIG_MODEL = {
    "guild_id": "",
    "guild_name": "",
    "prefix": ".",
    "quiet_prefix": ",",
    "sudo_prefix": "#",
    "languages": [
        "eng",
        "ita"
    ],
    "modules_status": {}
}

NEW_MODULE_STATUS = {
    "permissions": 0,
    "enabled": 1,
    "dm_enabled": 1,
    "status": 2
}

NEW_MODULE_MODEL = {

        "name": "module.deactivate",
        "main_module": 1,
        "module_type": 1,
        "status": {},
        "eng": {
            "invocation": [],
            "description": "Description",
            "usage": "Usage",
            "man": "Man"
        },
        "ita": {
            "invocation": [],
            "description": "Descrizione",
            "usage": "Uso",
            "man": "Manuale"
        }
}

NEW_REPLY = {
        "name": "",
        "enabled": 1,
        "mode": 1,
        "cit_author": "",
        "private": 1,
        "users_allowed": {
            "telegram": [

            ],
            "discord": [

            ]
        },
        "eng": {
            "standard_triggers": [
                ""
            ],
            "standard_counter": 0,
            "standard_outputs": [
                ""
            ],
            "power_triggers": [
                ""
            ],
            "power_counter": 0,
            "power_outputs": [
                ""
            ],
            "avoid_triggers": [
                ""
            ],
            "avoid_counter": 0,
            "avoid_outputs": [
                ""
            ]
        },
        "ita": {
            "standard_triggers": [
                ""
            ],
            "standard_counter": 0,
            "standard_outputs": [
                ""
            ],
            "power_triggers": [
                ""
            ],
            "power_counter": 0,
            "power_outputs": [
                ""
            ],
            "avoid_triggers": [
                ""
            ],
            "avoid_counter": 0,
            "avoid_outputs": [
                ""
            ]
        }
    }
