define(
    ['storeys/conf/urls'],
    function(urls) {
      var url = urls.url,
          include = urls.include;

      return [
          
              url('^test_success_1/', include('test_dir/additional_app/urls')), 
              url('^test_success_2/(?P<pk>[0-9]+)/$', StoreysView.as_view('storeys_urls_js/main.html', 'receipts/actions.htm'), 'receipts-index-view')
      ];
    }
);
