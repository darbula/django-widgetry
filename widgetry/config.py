#-*- coding: utf-8 -*-

from django.conf import settings

STATICMEDIA_PREFIX = getattr(settings, 'WIDGETRY_STATICMEDIA_PREFIX', None)
if not STATICMEDIA_PREFIX:
    STATICMEDIA_PREFIX = (getattr(settings,'STATIC_URL', None) or settings.MEDIA_URL) + 'widgetry/'

JQUERY_URLS = getattr(settings, 'WIDGETRY_JQUERY_URLS', getattr(settings, 'JQUERY_URLS', None))
if not JQUERY_URLS:
    JQUERY_URLS = {
            'core': STATICMEDIA_PREFIX + 'js/jquery-1.9.0.min.js',
            'admincompat': STATICMEDIA_PREFIX + 'js/admincompat.js',
            'ui.core': STATICMEDIA_PREFIX + 'js/ui/jquery-ui-1.9.2.js',
            'plugins.fkautocomplete': STATICMEDIA_PREFIX + 'js/plugins/jquery.fkautocomplete.js',
            'plugins.autocomplete': STATICMEDIA_PREFIX + 'js/plugins/jquery.autocomplete.js',
        }
