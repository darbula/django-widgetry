#-*- coding: utf-8 -*-
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from widgetry.tabs.admin import ModelAdminWithTabs

class ModelAdminWithTabsAndCMSPlaceholder(ModelAdminWithTabs, PlaceholderAdminMixin):
    def _media(self):
        return super(ModelAdminWithTabs, self).media + super(PlaceholderAdminMixin, self).media
    media = property(_media)
