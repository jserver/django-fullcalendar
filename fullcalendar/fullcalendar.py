from django.conf import settings

# django-fullcalendar static file location defaults to FullCalendar default
# folder structure, expected to be under the STATIC_URL

FULLCALENDAR_DEFAULTS = {
    'css_url': '//cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.1.0/fullcalendar.css',
    'print_css_url': '//cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.1.0/fullcalendar.print.css',
    'javascript_url': '//cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.1.0/fullcalendar.min.js',
    'jquery_url': '//code.jquery.com/jquery-2.1.0.min.js',
    'jquery_ui_url': '//code.jquery.com/ui/1.11.4/jquery-ui.js',
    'momentjs_url': '//cdnjs.cloudflare.com/ajax/libs/moment.js/2.9.0/moment.min.js',
}

# Updates location based on configuration defined by
# settings.py of the project

FULLCALENDAR = FULLCALENDAR_DEFAULTS.copy()
FULLCALENDAR.update(getattr(settings, 'FULLCALENDAR', {}))


def css_url():
    return FULLCALENDAR['css_url']


def print_css_url():
    return FULLCALENDAR['print_css_url']


def javascript_url():
    return FULLCALENDAR['javascript_url']


def jquery_url():
    return FULLCALENDAR['jquery_url']


def jquery_ui_url():
    return FULLCALENDAR['jquery_ui_url']


def momentjs_url():
    return FULLCALENDAR['momentjs_url']
