from django.contrib import admin
from django.conf.urls import patterns, url, include
from storeys.views import StoreysView
from storeys.utils import urlref
from django.views.generic.base import TemplateView



urlpatterns = patterns(
    'test',
    url(r'^test_1_(?P<pk>[0-9]+)$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
            prerender_content='receipts/actions.htm'
        ),
        name='receipts-index-view'
    ),
)
