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
        var TEST_PREFIX = '[RegExp test]: ',
            TEST_PREFIX_KWARGS = '[SUCCESS. `KWARG` TEST]',
            TEST_PREFIX_ARGS = '[SUCCESS. `ARG` TEST]',
            REGEXP_NUMERIC = /\d+/,
            REGEXP_WORD = /\w+/,
            REGEXP_PHONE = /((\d{3})-(\d{3})-(\d{4}))/,
            REGEXP_EMAIL = /(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;

        var run = function() {
            require(
                [settings.ROOT_URLCONF, 'storeys/core/urlresolver'],
                function(spec, urlresolver) {

                    // SUCCESS REVERSE TEST WITHOUT ARGS
                    urlresolver.reverse('receipts', {}, function(url){
                        test('[SUCCESS TEST WITHOUT ARGS] Numeric validation `reverse("receipts")`', function(t) {
                            expect(1);
                            equal(url, '/test_success/test_success/', TEST_PREFIX + 'RegExp pattern "^test_success/$" ||| But the return is "/test_success/test_success/". By the reason of include(``)');
                        })
                    })

                    // SUCCESS `KWARGS` TESTS
                    urlresolver.reverse('receipts', {'numeric': '1234567890'}, function(url){
                        test(TEST_PREFIX_KWARGS + 'Numeric validation `reverse("receipts", {"numeric": "1234567890"})`', function(t) {
                            expect(1);
                            equal(url, '/test_success_1/1234567890/', TEST_PREFIX + 'RegExp pattern is "^test_success_1/(\\?P<numeric>[0-9]+)/$" ||| The return is "/test_success_2/1234567890/".');
                        })
                    })

                    urlresolver.reverse('receipts', {'word': 'asdsaasd_1234567890'}, function(url){
                        test(TEST_PREFIX_KWARGS + 'Alphanumeric validation `reverse("receipts", {"word": "asdsaasd1234567890_"})`', function(t) {

                            expect(1);
                            equal(url, '/test_success_2/asdsaasd_1234567890', TEST_PREFIX + 'RegExp pattern is "^test_success_2/(\\?P<word>\\w+)$" ||| The return is  "/test_success_3/asdsaasd_1234567890".');
                        })
                    })

                    urlresolver.reverse('receipts', {'email_from': 'a@gmail.com', 'email_to': 'b@gmail.com'}, function(url){
                        test(TEST_PREFIX_KWARGS + 'Complex email validation `reverse("receipts", {"email_from": "a@gmail.com", "email_to": "b@gmail.com"})`', function(t) {

                            expect(1);
                            equal(url, '/test_success_3/from-a%40gmail.com/to-b%40gmail.com/', TEST_PREFIX + 'RegExp pattern is "^test_success_3/from-(\\?P<email_from>' + REGEXP_EMAIL.toString() + ')/to-(\\?P<email_from>' + REGEXP_EMAIL.toString() + ')/$" ||| The return is  /test_success_7/from-a%40gmail.com/to-b%40gmail.com/".');
                        })
                    })

                    // SUCCESS `ARGS` TESTS
                    urlresolver.reverse('receipts', ['test@gmail.com'], function(url){
                        test(TEST_PREFIX_ARGS + 'Email validation `reverse("receipts", ["test@gmail.com"])`', function(t) {

                            expect(1);
                            equal(url, '/test_success_4/test%40gmail.com/', TEST_PREFIX + 'RegExp pattern is "^test_success_4' + REGEXP_EMAIL.toString() + '/$ ||| The return is "/test_success_4/test%40gmail.com/".');
                        })
                    })

                    urlresolver.reverse('receipts', ['444-666-7777'], function(url){
                        test(TEST_PREFIX_ARGS + 'Phone validation `reverse("receipts", ["444-666-7777"])`', function(t) {

                            expect(1);
                            equal(url, '/test_success_5/phone-444-666-7777/', TEST_PREFIX + 'RegExp pattern is `/test_success_5'+ REGEXP_PHONE.toString() +'/` ||| The return is "/test_success_5/phone-444-666-7777/".');
                        })
                    })


                    urlresolver.reverse('receipts', ['test@gmail.com', '444-666-7777'], function(url){
                        test(TEST_PREFIX_ARGS + 'Complex email and phone validation `reverse("receipts", ["test@gmail.com", "444-666-7777"])`', function(t) {

                            expect(1);
                            equal(url, '/test_success/test_success_6/test%40gmail.com/phone-444-666-7777/', TEST_PREFIX + 'RegExp pattern is `/test_success_6/' + REGEXP_EMAIL.toString() + '/phone-' + REGEXP_PHONE.toString() + '/` But the return should be "/test_success/test_success_5/test%40gmail.com/phone-444-666-7777/". By the reason of include(``)');
                        })
                    })


                    // EXCEPTION TESTS

                    // test('[EXCEPTION `ARG` TEST] Pattern not found dur to wrong order of `arguments`: `reverse("receipts", ["444-666-7777", "test@gmail.com"])`', function(t) {
                    //     expect(1);
                    //
                    //     t.throws(
                    //         urlresolver.reverse('receipts', ['444-666-7777', 'test@gmail.com'], function(url){}),
                    //         /Uncaught Reverse for 'receipts' with arguments '\["444-666-7777","test@gmail\.com"\]'/,
                    //         "Correct Exception'"
                    //     );
                    //
                    // })

            })

        }
        return {run: run}
    }
);
