from django.contrib import admin
from django.conf.urls import patterns, url, include
from storeys.views import StoreysView
from storeys.utils import urlref
from django.views.generic.base import TemplateView



urlpatterns = patterns(
    'test',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test_success/', include('additional_app.urls')),
    url(r'^excluded_app/', include('excluded_app.urls')),
    url('^tests/$', StoreysView.as_view(
            template_name='main.html',
        ),
        name='tests'
    ),

    url(r'^test_success_1/(?P<numeric>[0-9]+)/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='receipts'
    ),

    url(r'^test_success_2/(?P<word>\w+)$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='receipts'
    ),

    url(r'^test_success_3/from-(?P<email_from>(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})))/to-(?P<email_to>(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})))/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='receipts'
    ),

    url(r'^test_success_4/((([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})))/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='receipts'
    ),
    url(r'^test_success_5/phone-((\d{3})-(\d{3})-(\d{4}))/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='receipts'
    ),
    url(r'^test_3/(?P<pk>[0-9]+)/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
        ),
        name='exclude'
    ),
)


non_exported_urlpatterns = (
    urlref(module_name='admin.site.urls'),
    urlref(module_name='excluded_app.urls'),
    urlref(name='exclude')
)
