define(
    ['storeys/conf/urls', 'storeys/contrib/auth/decorators', 'storeys/views/generic/base'],
    function(urls, decorators, base) {
      var url = urls.url,
          include = urls.include,
          TemplateView = base.TemplateView;

      return [
          
              url('^test_success/', include('additional_app/urls'))  , 
          
              url('^tests/$', new TemplateView({
                target: 'body',
                templatepath: 'index.html',
                page: '#receipts'
              })              
, 'tests')  , 
          
              url('^test_success_1/(?P<numeric>[0-9]+)/$', new TemplateView({
                target: 'body',
                templatepath: 'storeys_urls_js/main.html',
                page: '#receipts'
              })              
, 'receipts')  , 
          
              url('^test_success_2/(?P<word>\\w+)$', new TemplateView({
                target: 'body',
                templatepath: 'storeys_urls_js/main.html',
                page: '#receipts'
              })              
, 'receipts')  , 
          
              url('^test_success_3/from-(?P<email_from>(([^<>()\\[\\]\\\\.,;:\\s@"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,})))/to-(?P<email_to>(([^<>()\\[\\]\\\\.,;:\\s@"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,})))/$', new TemplateView({
                target: 'body',
                templatepath: 'storeys_urls_js/main.html',
                page: '#receipts'
              })              
, 'receipts')  , 
          
              url('^test_success_4/((([^<>()\\[\\]\\\\.,;:\\s@"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,})))/$', new TemplateView({
                target: 'body',
                templatepath: 'storeys_urls_js/main.html',
                page: '#receipts'
              })              
, 'receipts')  , 
          
              url('^test_success_5/phone-((\\d{3})-(\\d{3})-(\\d{4}))/$', new TemplateView({
                target: 'body',
                templatepath: 'storeys_urls_js/main.html',
                page: '#receipts'
              })              
, 'receipts')  
          
      ];
    }
);
