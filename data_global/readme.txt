Per i plebei del cazzo, come aggiungere un modulo

Questo è il format:

"Void": {
        "scope": "global",
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
        ],
        "cit_author": ""
    },

 -- Al posto del "Void" mettete un nome UNICO che identifica cosa serve quel blocco, possibilmente corto.
 -- I triggers possono essere anche frasi, più lunga è la frase minore è la probabilità che venga scritta.
 -- Se ci sono trigger uguali in più blocchi verrà preso quello più in alto nel file.
 -- Il cit_author viene aggiunto solo nei power_outputs
 -- I counters non serve modificarli, servono per stampare in sequenza gli output

 -- Per le risposte statiche nei trigger aggiungere il comando in questo format:
     "trigger &&& risposta"

     se si vuole avere anche il cit:
     "trigger &&& risposta &&& cit"

     Spazzi nei pressi dello spaziatore (&&&) verranno ignorati,
     stessa cosa se per caso aggiungete più di 2 spaziatori nella stringa.