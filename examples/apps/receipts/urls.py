from django.conf.urls import patterns, url
from storeys.views import StoreysView

urlpatterns = [
    url('^receipt-(?P<pk>[0-9]+)$',
        StoreysView.as_view(
          prerender_content='receipts/item.html',
        ),
        name='receipts-item-view'),
    url(r'^create/$',
        StoreysView.as_view(
            prerender_content='receipts/create.html',
        ),
        name='receipts-create-view'
    ),
    url(r'^list/$',
        StoreysView.as_view(
            prerender_content='receipts/list.html',
        ),
        name='receipts-list-view'
    ),
    url(r'^$',
        StoreysView.as_view(
            prerender_content='receipts/index.html',
        ),
        name='receipts-index-view'
    ),
]
