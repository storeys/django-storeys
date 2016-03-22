from django.contrib import admin
from django.conf.urls import patterns, url, include
from storeys.views import StoreysView
from views import TempView, include_test
from django.views.generic.base import TemplateView


urlpatterns = patterns(
    'test',
    url(r'^test_success/creceipt-(?P<pk>[0-9]+)/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
            prerender_content='storeys_urls_js/actions.htm'
        ),
        name='receipts'
    ),
)

urlpatterns += patterns(
    url(r'^test_admin/', TempView.as_view(template_name='storeys_urls_js/main.html')),
    url(r'^test_success_pricing/$', TemplateView.as_view(template_name='storeys_urls_js/main.html'),
        name='pricing')
)
