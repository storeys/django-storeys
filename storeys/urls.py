from django.contrib import admin
from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
from views import StoreysView


urlpatterns = patterns(
    '',
    url(r'^test_success_admin/', include(admin.site.urls))
)
