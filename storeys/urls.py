from django.contrib import admin
from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
from views import StoreysView

def urlref(*args, **kwargs):
    return kwargs

urlpatterns = patterns(
    '',
    url(r'^test_success_admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
    url(r'^customer/(\d+)/phone/cancel/$', TemplateView.as_view(template_name='storeys/base.html'), name='exclude2')
)


non_exported_urlpatterns = (
    # urlref(module_name='app.urls'),
    urlref(module_name='admin.site.urls'),
    # urlref(name='exclude2'),
    # urlref(name='test'),

)
