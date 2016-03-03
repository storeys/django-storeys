from django.conf import admin
from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    'trader',
    url(r'^test1', 'views.test_view'),
    url(r'^test2', 'views.test_view2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test3', views.test_view3),
    url(r'^test_success_creceipt-(?P<pk>[0-9]+)$',
        StoreysView.as_view(
            template_name='storeys_urls_js/main.html',
            prerender_content='receipts/actions.htm'
        ),
        name='receipts-index-view'
    ),
)


urlpatterns += patterns(
    url(r'^test_success_new_test2', include(views.verify_phone.views2.verify_phone)),
    url(r'^test4', 'views.process_order_market'),
    url(r'^test5', 'views.process_order_spend'),
    url(r'^new_test3', include('api.urls')),
    url(r'^block_user/(?P<user_id>\d+)/', 'views.block_user', name='block_user'),
    url(r'^test_success_credit/', include(extra_patterns.views)),
    url(r'^test_pricing/$', TemplateView.as_view(template_name='storeys_urls_js/main.html'),
        name='test')
)


non_exported_urlpatterns = (
    urlref(module_name='api.urls'),
    urlref(module_name='admin.site.urls'),
    urlre(name='test'),
)
