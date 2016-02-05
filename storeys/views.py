import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic.base import TemplateView

EXPORTED_SETTINGS = ['STOREYS_APPS']

class StoreysView(TemplateView):
    prerender_content = None

    def get_context_data(self, **kwargs):
        context = super(StoreysView, self).get_context_data(**kwargs)
        if ('prerender_content' not in context and self.prerender_content is not None):
            context['prerender_content'] = self.prerender_content

        context['settings'] = {key: getattr(settings, key) for key in EXPORTED_SETTINGS if hasattr(settings, key)}
        context['renderer'] = 'django'
        return context
