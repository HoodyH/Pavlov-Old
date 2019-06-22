from core.src.settings import ITA


def sec_to_time_string(sec, language, short=False):
    sec = int(sec)
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if d is not 0:
        if language == ITA:
            out = '{} {}, {} {} e {} {}'.format(
                d,
                "giorni" if d > 1 else "giorno",
                h,
                "ore" if h > 1 else "ora",
                m,
                "minuti" if m > 1 else "minuto",
            )
            short_out = '{}d, {}h'.format(d, h)
        else:
            out = '{} {}, {} {} and {} {}'.format(
                d,
                "days" if d > 1 else "day",
                h,
                "hours" if h > 1 else "hour",
                m,
                "minutes" if m > 1 else "minute",
            )
            short_out = '{}d, {}h'.format(d, h)

    elif h is not 0:
        if language == ITA:
            out = '{} {} e {} {}'.format(
                h,
                "ore" if h > 1 else "ora",
                m,
                "minuti" if m > 1 else "minuto",
            )
            short_out = '{}h, {}min'.format(h, m)
        else:
            out = '{} {} and {} {}'.format(
                h,
                "hours" if h > 1 else "hour",
                m,
                "minutes" if m > 1 else "minute",
            )
            short_out = '{}h, {}min'.format(h, m)

    elif m is not 0:
        if language == ITA:
            out = '{} {} e {} {}'.format(
                m,
                "minuti" if m > 1 else "minuto",
                s,
                "secondi" if s > 1 else "secondo",
            )
            short_out = '{}min'.format(m)
        else:
            out = '{} {} and {} {}'.format(
                m,
                "minutes" if m > 1 else "minute",
                s,
                "seconds" if s > 1 else "second",
            )
            short_out = '{}min'.format(m)

    else:
        if language == ITA:
            out = '{} {}'.format(
                s,
                "secondi" if s > 1 else "secondo",
            )
            short_out = '{}sec'.format(s)
        else:
            out = '{} {}'.format(
                s,
                "seconds" if s > 1 else "second",
            )
            short_out = '{}sec'.format(s)

    if short:
        return short_out
    else:
        return out


def weekdays_string(week_number, offset, language, short=False):

    if week_number+offset == 0:
        if language == ITA:
            out = "Lunedì"
            short_out = "Lun"
        else:
            out = "Monday"
            short_out = "Mon"

    elif week_number+offset == 1:
        if language == ITA:
            out = "Martedì"
            short_out = "Mar"
        else:
            out = "Tuesday"
            short_out = "Tue"

    elif week_number+offset == 2:
        if language == ITA:
            out = "Mercoledì"
            short_out = "Mer"
        else:
            out = "Wednesday"
            short_out = "Wed"

    elif week_number+offset == 3:
        if language == ITA:
            out = "Giovedì"
            short_out = "Gio"
        else:
            out = "Thursday"
            short_out = "Thu"

    elif week_number+offset == 4:
        if language == ITA:
            out = "Venerdì"
            short_out = "Ven"
        else:
            out = "Friday"
            short_out = "Fri"

    elif week_number+offset == 5:
        if language == ITA:
            out = "Sabato"
            short_out = "Dom"
        else:
            out = "Saturday"
            short_out = "Sat"

    elif week_number+offset == 6:
        if language == ITA:
            out = "Domenica"
            short_out = "Dom"
        else:
            out = "Sunday"
            short_out = "Sun"
    else:
        return "No Weekday"

    if short:
        return short_out
    else:
        return out


def my_data_subtitle(language, scope):

    if scope == "hourly":
        if language == ITA:
            out = "Messaggi e tempo sprecato mostrati per ora"
        else:
            out = "Messages and Time spent here shown by hour"

    elif scope == "daily":
        if language == ITA:
            out = "Messaggi e tempo sprecato mostrati per giorno"
        else:
            out = "Messages and Time spent here shown by day"

    elif scope == "monthly":
        if language == ITA:
            out = "Messaggi e tempo sprecato mostrati per mese"
        else:
            out = "Messages and Time spent here shown by month"
    else:
        out = ""

    return out


def my_data_description(language, time_scope, n_messages, n_sec):

    if time_scope == 'hourly':
        if language == ITA:
            out = 'Questo grafico rappresenta i {} che hai inviato in queste ore\n' \
                  'Per un totali {} di tempo sprecato.'
        else:
            out = 'This graph show the {} msg that\'s you\'ve sent in these hours\n' \
                  'For a total of {} of time wasted.'
    elif time_scope == 'daily':
        if language == ITA:
            out = 'Qui invece, puoi vedere i {} che hai inviato in questi giorni\n' \
                  'Per un totali {} di tempo sprecato.'
        else:
            out = 'Here you can see the {} msg that\'s you\'ve sent in these days\n' \
                  'For a total of {} of time wasted.'
    else:
        if language == ITA:
            out = 'In fine abbiamo i {} che hai inviato in questi mesi\n' \
                  'Complimenti, hai sprecato {} in tutto.'
        else:
            out = 'At the end we can see the {} msg sent in these months\n' \
                  'Congrats, {} of wasted in total.'
    return out.format(n_messages, sec_to_time_string(n_sec, language))

