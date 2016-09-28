"use strict";

/**
* TODO:
* TESTS:
* - separate '/'
* - separate `include()`
*
* Exceptions tests (Exception works, but tests wasn't realized):
* - `params` wrong type check
* - wrong args order
* - nested arguments
* - reverse() with `args` not found
* - reverse() with `kwargs` not found
*/

define(
    ['settings'],
    function(settings) {
        var TEST_PREFIX = '[ urlresolver.reverse ]',
            REGEXP_NUMERIC = /\d+/,
            REGEXP_WORD = /\w+/,
            REGEXP_PHONE = /((\d{3})-(\d{3})-(\d{4}))/,
            REGEXP_EMAIL = /(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;

        var run = function() {
            require(
                [settings.ROOT_URLCONF, 'storeys/core/urlresolver', 'QUnit'],
                function(spec, urlresolver, QUnit) {

                    QUnit.asyncTest(TEST_PREFIX, function (assert) {
                        expect(7);
                        QUnit.stop(6);


                        // SUCCESS REVERSE TEST WITHOUT ARGS
                        urlresolver.reverse('receipts', {}, function(url){
                            assert.equal(url, '/test_success/test_success/', 'Numeric validation `reverse("receipts")`. RegExp pattern "^test_success/$" ||| But the return is "/test_success/test_success/". By the reason of include(``)');
                            QUnit.start();
                        });


                        // SUCCESS `KWARGS` TESTS
                        urlresolver.reverse('receipts', {'numeric': '1234567890'}, function(url){
                            assert.equal(url, '/test_success_1/1234567890/', 'Numeric validation `reverse("receipts", {"numeric": "1234567890"})`. RegExp pattern is "^test_success_1/(\\?P<numeric>[0-9]+)/$" ||| The return is "/test_success_2/1234567890/".');
                            QUnit.start();
                        });

                        urlresolver.reverse('receipts', {'word': 'asdsaasd_1234567890'}, function(url){
                            assert.equal(url, '/test_success_2/asdsaasd_1234567890', 'Alphanumeric validation `reverse("receipts", {"word": "asdsaasd1234567890_"})`. RegExp pattern is "^test_success_2/(\\?P<word>\\w+)$" ||| The return is  "/test_success_3/asdsaasd_1234567890".');
                            QUnit.start();
                        });

                        urlresolver.reverse('receipts', {'email_from': 'a@gmail.com', 'email_to': 'b@gmail.com'}, function(url){
                            assert.equal(url, '/test_success_3/from-a%40gmail.com/to-b%40gmail.com/', 'Complex email validation `reverse("receipts", {"email_from": "a@gmail.com", "email_to": "b@gmail.com"})`. RegExp pattern is "^test_success_3/from-(\\?P<email_from>' + REGEXP_EMAIL.toString() + ')/to-(\\?P<email_from>' + REGEXP_EMAIL.toString() + ')/$" ||| The return is  /test_success_7/from-a%40gmail.com/to-b%40gmail.com/".');
                            QUnit.start();
                        });


                        // SUCCESS `ARGS` TESTS
                        urlresolver.reverse('receipts', ['test@gmail.com'], function(url){
                            assert.equal(url, '/test_success_4/test%40gmail.com/', 'Email validation `reverse("receipts", ["test@gmail.com"])`. RegExp pattern is "^test_success_4' + REGEXP_EMAIL.toString() + '/$ ||| The return is "/test_success_4/test%40gmail.com/".');
                            QUnit.start();
                        });

                        urlresolver.reverse('receipts', ['444-666-7777'], function(url){
                            assert.equal(url, '/test_success_5/phone-444-666-7777/', 'Phone validation `reverse("receipts", ["444-666-7777"])`. RegExp pattern is `/test_success_5'+ REGEXP_PHONE.toString() +'/` ||| The return is "/test_success_5/phone-444-666-7777/".');
                            QUnit.start();
                        });

                        urlresolver.reverse('receipts', ['test@gmail.com', '444-666-7777'], function(url){
                            assert.equal(url, '/test_success/test_success_6/test%40gmail.com/phone-444-666-7777/', 'Complex email and phone validation `reverse("receipts", ["test@gmail.com", "444-666-7777"])`. RegExp pattern is `/test_success_6/' + REGEXP_EMAIL.toString() + '/phone-' + REGEXP_PHONE.toString() + '/` But the return should be "/test_success/test_success_5/test%40gmail.com/phone-444-666-7777/". By the reason of include(``)');
                            QUnit.start();
                        });

                    });

                    // TODO: add tests for Exceptions
                    // TEST FOR EXCEPTION
                    //   assert.throws(
                    //     function() {
                    //       window.setTimeout(function() {
                    //           throw "description";
                    //       }, 10)
                    //     },
                    //       /description/,
                    //       "raised error message contains 'descriptions'"
                    //   );

            })

        }
        return {run: run}
    }
);
