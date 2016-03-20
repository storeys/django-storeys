from django.contrib import admin
from django.conf.urls import patterns, url, include
from storeys.views import StoreysView
from storeys.utils import urlref
from django.views.generic.base import TemplateView



urlpatterns = patterns(
    'test',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test_success_1/', include('test_dir.additional_app.urls')),
    url(r'^additional_app2/', include('test_dir.additional_app2.urls')),
    url(r'^test_success_2/(?P<pk>[0-9]+)/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
            prerender_content='receipts/actions.htm'
        ),
        name='receipts-index-view'
    ),
    url(r'^test_3/(?P<pk>[0-9]+)/$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
            prerender_content='receipts/actions.htm'
        ),
        name='test_exclude'
    ),
)


non_exported_urlpatterns = (
    urlref(module_name='admin.site.urls'),
    urlref(module_name='test_dir.additional_app2.urls'),
    urlref(name='test_exclude')
)
