from old_core.src.languages_handler import chose_language


def time_to_string(language, time, short=False, time_input='s'):

    t = int(time)
    if time_input == 'h':
        m = 0
        h = t
    elif time_input == 'm':
        s = 0
        h, m = divmod(t, 60)
    else:
        m, s = divmod(t, 60)
        h, m = divmod(m, 60)

    d, h = divmod(h, 24)

    def eng():
        if d is not 0:
            out = '{} {}, {} {} and {} {}'.format(
                d, "days" if d != 1 else "day",
                h, "hours" if h != 1 else "hour",
                m, "minutes" if m != 1 else "minute",
            )
            short_out = '{}d, {}h'.format(d, h)

        elif h is not 0:

            out = '{} {} and {} {}'.format(
                h, "hours" if h != 1 else "hour",
                m, "minutes" if m != 1 else "minute",
            )
            short_out = '{}h, {}min'.format(h, m)

        elif m is not 0:

            out = '{} {} and {} {}'.format(
                m, "minutes" if m != 1 else "minute",
                s, "seconds" if s != 1 else "second",
            )
            short_out = '{}min'.format(m)

        else:

            out = '{} {}'.format(
                s, "seconds" if s != 1 else "second",
            )
            short_out = '{}sec'.format(s)

        if short:
            return short_out
        else:
            return out

    def ita():
        if d is not 0:
            out = '{} {}, {} {} e {} {}'.format(
                d, "giorni" if d != 1 else "giorno",
                h, "ore" if h != 1 else "ora",
                m, "minuti" if m != 1 else "minuto",
            )
            short_out = '{}d, {}h'.format(d, h)

        elif h is not 0:

            out = '{} {} e {} {}'.format(
                h, "ore" if h != 1 else "ora",
                m, "minuti" if m != 1 else "minuto",
            )
            short_out = '{}h, {}min'.format(h, m)

        elif m is not 0:

            out = '{} {} e {} {}'.format(
                m, "minuti" if m != 1 else "minuto",
                s, "secondi" if s != 1 else "secondo",
            )
            short_out = '{}min'.format(m)

        else:
            out = '{} {}'.format(
                s, "secondi" if s != 1 else "secondo",
            )
            short_out = '{}sec'.format(s)

        if short:
            return short_out
        else:
            return out

    return chose_language(
        language,
        eng, ita=ita
    )


def weekdays_string(week_number, offset, language, short=False):

    def eng():

        def monday():
            return "Monday"

        def tuesday():
            return "Tuesday"

        def wednesday():
            return "Wednesday"

        def thursday():
            return "Thursday"

        def friday():
            return "Friday"

        def saturday():
            return "Saturday"

        def sunday():
            return "Sunday"

        weekdays = {
            0: monday,
            1: tuesday,
            2: wednesday,
            3: thursday,
            4: friday,
            5: saturday,
            6: sunday,
        }

        try:
            out = weekdays[week_number + offset]()
        except Exception as e:
            print('wrong offset in weekdays_string function\n{}'.format(e))
            return "wrong offset"

        if short:
            return out[:2]
        else:
            return out

    def ita():

        def monday():
            return "Lunedì"

        def tuesday():
            return "Martedì"

        def wednesday():
            return "Mercoledì"

        def thursday():
            return "Giovegì"

        def friday():
            return "Venerdì"

        def saturday():
            return "Sabato"

        def sunday():
            return "Domenica"

        weekdays = {
            0: monday,
            1: tuesday,
            2: wednesday,
            3: thursday,
            4: friday,
            5: saturday,
            6: sunday,
        }

        try:
            out = weekdays[week_number + offset]()
        except Exception as e:
            print('wrong offset in weekdays_string function\n{}'.format(e))
            return "wrong offset"

        if short:
            return out[:2]
        else:
            return out

    return chose_language(
        language,
        eng, ita=ita
    )


def my_data_subtitle(language, time_scope):

    def eng():
        if time_scope == "hourly":
            return "Messages and Time spent here shown by hour"

        elif time_scope == "daily":
            return "Messages and Time spent here shown by day"

        elif time_scope == "monthly":
            return "Messages and Time spent here shown by month"
        else:
            return ""

    def ita():
        if time_scope == "hourly":
            return "Messaggi e tempo sprecato mostrati per ora"

        elif time_scope == "daily":
            return "Messaggi e tempo sprecato mostrati per giorno"

        elif time_scope == "monthly":
            return "Messaggi e tempo sprecato mostrati per mese"

    return chose_language(
        language,
        eng, ita=ita
    )


def my_data_description(language, time_scope, n_messages, n_sec):

    def eng():

        if time_scope == "hourly":
            out = 'This graph show the {} msg that\'s you\'ve sent in these hours\n' \
                  'For a total of {} of time wasted.'

        elif time_scope == "daily":
            out = 'Here you can see the {} msg that\'s you\'ve sent in these days\n' \
                  'For a total of {} of time wasted.'

        elif time_scope == "monthly":
            out = 'At the end we can see the {} msg sent in these months\n' \
                  'Congrats, {} of wasted in total.'
        else:
            out = ""

        return out.format(n_messages, time_to_string(language, n_sec))

    def ita():
        if time_scope == "hourly":
            out = 'Questo grafico rappresenta i {} che hai inviato in queste ore\n' \
                  'Per un totali {} di tempo sprecato.'

        elif time_scope == "daily":
            out = 'Qui invece, puoi vedere i {} che hai inviato in questi giorni\n' \
                  'Per un totali {} di tempo sprecato.'

        elif time_scope == "monthly":
            out = 'In fine abbiamo i {} che hai inviato in questi mesi\n' \
                  'Complimenti, hai sprecato {} in tutto.'
        else:
            out = ""

        return out.format(n_messages, time_to_string(language, n_sec))

    return chose_language(
        language,
        eng, ita=ita
    )

