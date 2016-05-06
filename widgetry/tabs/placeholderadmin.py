#-*- coding: utf-8 -*-
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from widgetry.tabs.admin import ModelAdminWithTabs
from django.forms.widgets import Media


class ModelAdminWithTabsAndCMSPlaceholder(PlaceholderAdminMixin, ModelAdminWithTabs):
    def _media(self):
        try:
            placeholdermedia = super(PlaceholderAdminMixin, self).media
        except AttributeError:
            placeholdermedia = Media()
        return super(ModelAdminWithTabs, self).media + placeholdermedia
    media = property(_media)
