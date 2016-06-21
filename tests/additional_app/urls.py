from django.contrib import admin
from django.conf.urls import patterns, url, include
from storeys.views import StoreysView
from views import TempView, include_test
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    'test',
    url(r'^test_success/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html'
        ),
        name='receipts'
    ),
    url(r'^test_success_6/((([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})))/phone-((\d{3})-(\d{3})-(\d{4}))/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='receipts'
    ),
)

urlpatterns += patterns(
    url(r'^test_admin/', TempView.as_view(template_name='notexist/main.html')),
    url(r'^test_success_pricing/$', StoreysView.as_view(template_name='storeys_urls_js/main.html'),
        name='pricing')
)
