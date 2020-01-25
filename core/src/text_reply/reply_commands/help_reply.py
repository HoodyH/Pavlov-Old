from core.src.languages_handler import chose_language


def response(language, prefix):

    def eng():
        intro = 'This is **Pavlov** a multi-purpose bot, maintained by @AbbestiaDC.'

        requirements = '**REQUIREMENTS**\nIt require the admin cause it read the messages to perform actions.\n' \
                       'Il will Log data like number of messages or number of commands used.\n' \
                       '**It will not store any message.**'

        use = '**USE OF THE BOT**\nLets start with an simple introduction.\n' \
              'There is a manual, like in the linux terminal, in this bot. ' \
              'Use command **{}man** to see how to use it.\n' \
              'All the available commands are listed with **{}man all** ' \
              'and to see the details of a specific command use **{}man command_name**. ' \
              'Every command has alternative invocations, those are also good to use with manual command, ' \
              'basically everything that works as command can be used in **{}man command**.\n' \
              'This is all you need to start. For any problem contact the admins'.format(
                    prefix,
                    prefix,
                    prefix,
                    prefix,
                )

        help_develop = '**CONTACT ADMINS**\nHelp improve the bot reporting bugs.\n' \
                       'Use command **{}ticket with some text here** to send an instant message to the support group.' \
                       '\nAnd if you are a programmer and you want to create new commands you are free to help, ' \
                       'every command can be made in a separate file and added later to the bot. ' \
                       'If you want the **default-command-file** contact me right away.'.format(
                            prefix,
                        )

        return '{}\n\n{}\n\n{}\n\n{}'.format(intro, requirements, use, help_develop)

    def ita():
        intro = 'Questo è **Pavlov** un multi-purpose bot, mantenuto da @AbbestiaDC.'

        requirements = '**REQUISITI**\nRichiede l\'admin cause in quanto deve leggere i messaggi' \
                       ' per eseguire i comandi.\n' \
                       'Logga alcuni dati come numero di messaggi mandati e numero di comandi chiamati.\n' \
                       '**Non salva alcun tipo di messaggio.**'

        use = '**UTILIZZO DEL BOT**\nCominciamo con una semplice introduzione.\n' \
              'C\'è un manuale, come nel terminale di linux, in questo bot. ' \
              'Usa il comando **{}man** per vedere come utilizzarlo.\n' \
              'Tutti i comandi utilizzabili vengono mostrati con **{}man all** ' \
              'e per i dettagli di utilizzo di uno specifico comando usa **{}man command_name**. ' \
              'Esistono anche invocazioni alternative del comando, sono tutte utilizzabili con il comando manuale, ' \
              'praticamente tutto quello che funziona come comando può essere usato in **{}man command**.\n' \
              'Questo è tutto quello che serve sapere per cominciare. Per qualsiasi problema contatta gli admin'.format(
                    prefix,
                    prefix,
                    prefix,
                    prefix,
                )

        help_develop = '**CONTATTA GLI ADMINS**\nAiuta a migliorare il bot segnalando i bugs.\n' \
                       'Usa il commando **{}ticket con il problema qui** per mandare un messaggio nel support group.' \
                       '\nE se sei un programmatore e vuoi creare nuovi comandi sei libero di contribuire, ' \
                       'ogni comando può essere fatto in un file a parte per essere poi aggiunto al bot. ' \
                       'Se vuoi avere il **default-command-file** manda un ticket ora.'.format(
                            prefix,
                        )

        return '{}\n\n{}\n\n{}\n\n{}'.format(intro, requirements, use, help_develop)

    return chose_language(
        language,
        eng, ita=ita
    )

