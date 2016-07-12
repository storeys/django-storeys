"use strict";

require.config({
    paths: {
        'jquery' : 'http://code.jquery.com/jquery-1.12.1.min',
        'QUnit': 'static/libs/qunit',
        'slib': '../submodules/storeys/storeys/lib'
    },
    shim: {
       'QUnit': {
           exports: 'QUnit',
           init: function() {
               QUnit.config.autoload = false;
               QUnit.config.autostart = false;
           }
       },
       'nunjucks': {
           exports: 'nunjucks',
           init: function() {
           }
       }
    }
});

define('settings', ['module'], function(module) {
    var config = module.config() || {},
        instance = {};

    instance.DEFAULT_URL = '/tests/';
    instance.ROOT_URLCONF = 'tests/static/tests/urls';
    instance.ROOT_HASHCONF = 'tests/hashes';
    instance.MIDDLEWARE_CLASSES = [
    ];

    instance.URL_ROOT = 'http://storeys-django-starter.herokuapp.com';
    instance.URL_API_ROOT =  instance.URL_ROOT + '/api/v1';
    instance.URL_API_LOGIN = instance.URL_API_ROOT + '/login/';
    instance.URL_API_LOGOUT = instance.URL_API_ROOT + '/logout/';
    instance.STATIC_ROOT = './';

    instance.PROJECT_APPS = [
      'tests',
      'additional_app',
      'excluded_app',
    ];

    instance.URL_LOGIN = '/accounts/login/';
    instance.URL_PENDING_ACTIVATION = '/accounts/pending/';
    instance.REDIRECT_FIELD_NAME = 'next';

    return instance;
  });


  // tests.
  require(
      [   'storeys',
          'QUnit',
          'settings',
          'static/js/tests/urls',
          'static/js/tests/reverse',
          'static/js/tests/templatetag_url',
      ],
      function(storeys, QUnit, settings, test_urls, test_reverse, templatetag_url) {

        storeys.start();

        QUnit.load();
        QUnit.start();

        test_urls.run();
        test_reverse.run();
        templatetag_url.run();

      }
  );
