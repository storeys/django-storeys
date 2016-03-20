define(
    ['storeys/conf/urls', 'storeys/contrib/auth/decorators', 'storeys/views/generic/base'],
    function(urls, decorators, views) {
      var url = urls.url,
          View = views.View;

      return [

              url('^test_success/creceipt-(?P<pk>[0-9]+)/$', View.get('storeys_urls_js/main.html')),
              url('^test_success_pricing/$', View.get('storeys_urls_js/main.html'))
      ];
    }
);
