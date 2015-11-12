import json
import settings

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic.base import TemplateView

class StoreysView(TemplateView):
    prerender_content = None

    def get_context_data(self, **kwargs):
        context = super(StoreysView, self).get_context_data(**kwargs)
        if ('prerender_content' not in context and self.prerender_content is not None):
            context['prerender_content'] = self.prerender_content
        return context
