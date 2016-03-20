"use strict";

require.config({
    paths: {
        'QUnit': 'static/libs/qunit',
        'nunjucks': 'static/libs/nunjucks'
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

    instance.DEFAULT_URL = '/receipts/';
    instance.ROOT_URLCONF = 'additional_app/static/additional_app/urls';
    instance.ROOT_HASHCONF = 'app/hashes';
    instance.MIDDLEWARE_CLASSES = [
    ];

    instance.URL_ROOT = 'http://storeys-django-starter.herokuapp.com';
    instance.URL_API_ROOT =  instance.URL_ROOT + '/api/v1';
    instance.URL_API_LOGIN = instance.URL_API_ROOT + '/login/';
    instance.URL_API_LOGOUT = instance.URL_API_ROOT + '/logout/';
    instance.STATIC_ROOT = './';

    instance.PROJECT_APPS = [
      'storeys',
      'additional_app',
      'additional_app2',
    ];

    instance.URL_LOGIN = '/accounts/login/';
    instance.URL_PENDING_ACTIVATION = '/accounts/pending/';
    instance.REDIRECT_FIELD_NAME = 'next';

    return instance;
  });

  // require(['storeys'], function(storeys) {
  //   storeys
  //     .start();
  // });


// require the unit tests.
require(
    ['QUnit', 'static/js/urls_test', 'settings'],
    function(QUnit, urls_test, settings) {
        urls_test.run();
        QUnit.load();
        QUnit.start();
    }
);
