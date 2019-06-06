from core.src.settings import ITA


def sec_to_time(sec, language):
    minutes, seconds = divmod(sec, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days is not 0:
        if language == ITA:
            out = '{} giorni, {} ore, {} minuti e {} secondi'
        else:
            out = '{} days, {} hours, {} minutes and {} seconds'
        return out.format(days, hours, minutes, seconds)
    elif hours is not 0:
        if language == ITA:
            out = '{} ore, {} minuti e {} secondi'
        else:
            out = '{} hours, {} minutes and {} seconds'
        return out.format(hours, minutes, seconds)
    elif minutes is not 0:
        if language == ITA:
            out = '{} minuti e {} secondi'
        else:
            out = '{} minutes and {} seconds'
        return out.format(minutes, seconds)
    else:
        if language == ITA:
            out = '{} secondi'
        else:
            out = '{} seconds'
        return out.format(seconds)
