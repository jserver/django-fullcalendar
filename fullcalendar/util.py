# coding: utf-8
import json


def date_handler(obj):
    """
    Handles JSON serialization for datetime values
    """
    # return obj.isoformat() if hasattr(obj, 'isoformat') else obj
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError("Unserializable object {} of type {}".format(obj, type(obj)))


def convert_field_names(event_list):
    """
    Converts atribute names from Python code convention to the
    attribute names used by FullCalendar
    """
    for event in event_list:
        for key in event.keys():
            if '__' in key:
                save_to_key = key.split('__')[0]
            else:
                save_to_key = key
            event[snake_to_camel_case(save_to_key)] = event.pop(key)
    return event_list


def snake_to_camel_case(s):
    """
    Converts strings from 'snake_case' (Python code convention)
    to CamelCase
    """
    new_string = s

    leading_count = 0
    while new_string.find('_') == 0:
        new_string = new_string[1:]
        leading_count += 1

    trailing_count = 0
    while new_string.rfind('_') == len(new_string) - 1:
        new_string = new_string[:-1]
        trailing_count += 1

    new_string = ''.join([word.title() for word in new_string.split('_')])
    leading_underscores = '_' * leading_count
    trailing_underscores = '_' * trailing_count
    return leading_underscores + new_string[0].lower() + new_string[1:] + trailing_underscores


def events_to_json(events_queryset):
    """
    Dumps a CalendarEvent queryset to the JSON expected by FullCalendar
    """
    events_queryset = events_queryset.select_related('iso', 'state').prefetch_related('utilities', 'years', 'rfp_types')

    events_values = []
    for event in events_queryset:
        evdict = {
            'id': event.id,
            'title': event.title,
            'start': event.start,
            'end': event.end,
            'all_day': event.all_day,
            'description': event.description,
            'state': event.state.name if event.state else None,
            'iso': event.iso.name if event.iso else None,
        }
        evdict['utilities'] = [ev.name for ev in event.utilities.all()]
        evdict['years'] = [ev.value for ev in event.years.all()]
        evdict['rfptypes'] = [ev.value for ev in event.rfp_types.all()]
        events_values.append(evdict)

    events_values = convert_field_names(events_values)
    for event in events_values:
        if 'allDay' in event and event['allDay']:
            event['start'] = event['start'].date()
            event['end'] = event['end'].date()
    return json.dumps(events_values, default=date_handler)


def calendar_options(event_url, options):
    """
    Builds the Fullcalendar options array

    This function receives two strings. event_url is the url that returns a JSON array containing
    the calendar events. options is a JSON string with all the other options.
    """
    event_url_option = 'events: "%s"' % (event_url,)
    s = options.strip()
    if s is not None and '{' in s:
        pos = s.index('{') + 1
    else:
        return '{%s}' % (event_url_option)
    return s[:pos] + event_url_option + ', ' + s[pos:]
