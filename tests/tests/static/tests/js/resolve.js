"use strict";

define(
    ['storeys/conf/settings'],
    function(settings) {

        var TEST_PREFIX = '[ urlresolver.resolve ]';

        var run = function() {
            require(
                [settings.ROOT_URLCONF, 'storeys/core/urlresolver', 'QUnit'],
                function(spec, urlresolver, QUnit) {

                    QUnit.asyncTest(TEST_PREFIX, function (assert) {
                        expect(8);
                        QUnit.stop(6);

                        var urlspec = spec;
                        var resolve = urlresolver.create(urlspec);

                        // SUCCESS RESOLVE TEST WITHOUT ARGS
                        resolve('tests/', function(params, view){
                            assert.equal(
                                JSON.stringify(params),
                                '{}',
                                'Resolve simple path "tests/"'
                            );

                            assert.ok(
                                'config' in view,
                                'Resolve simple path "tests/" (view returned)'
                            );
                            QUnit.start();
                        });

                        // SUCCESS `ARGS` TESTS
                        resolve('test_success_4/test@gmail.com/', function(params, view){
                            assert.equal(
                                JSON.stringify(params),
                                "{\"0\":\"test@gmail.com\",\"1\":\"test\",\"2\":\"test\",\"5\":\"gmail.com\",\"7\":\"gmail.com\",\"8\":\"gmail.\"}",
                                'Resolve path using simple email regexp "test_success_4/test%40gmail.com/".'
                            );
                            QUnit.start();
                        });

                        resolve('test_success_5/phone-111-222-3333/', function(params, view) {
                            assert.equal(
                                JSON.stringify(params) ,
                                "{\"0\":\"111-222-3333\",\"1\":\"111\",\"2\":\"222\",\"3\":\"3333\"}",
                                'Resolve path using simple phone regexp "test_success_5/phone-111-222-3333/".'
                            );
                            QUnit.start();
                        });

                        resolve('test_success/test_success_6/test@gmail.com/phone-111-222-3333/', function(params, view) {
                            assert.equal(
                                JSON.stringify(params) ,
                                '{\"0\":\"test@gmail.com\",\"1\":\"test\",\"2\":\"test\",\"5\":\"gmail.com\",\"7\":\"gmail.com\",\"8\":\"gmail.\",\"9\":\"111-222-3333\",\"10\":\"111\",\"11\":\"222\",\"12\":\"3333\"}',
                                'Resolve path using two simple regexps "test_success/test_success_6/test@gmail.com/phone-111-222-3333/".'
                            );
                            QUnit.start();
                        });



                        // SUCCESS `KWARGS` TESTS
                        resolve('test_success_1/1234567890/', function(params, view) {
                            assert.equal(
                                JSON.stringify(params) ,
                                "{\"numeric\":\"1234567890\"}",
                                'Resolve path using <keyword> regexp "test_success_1/1234567890/".'
                            );
                            QUnit.start();
                        });

                        resolve('test_success_2/asdsaasd_1234567890', function(params, view) {
                            assert.equal(
                                JSON.stringify(params) ,
                                "{\"word\":\"asdsaasd_1234567890\"}",
                                'Resolve path using <keyword> regexp "test_success_2/asdsaasd_1234567890".'
                            );
                            QUnit.start();
                        });

                        resolve('test_success_3/from-a@gmail.com/to-b@gmail.com/', function(params, view) {
                            assert.equal(
                                JSON.stringify(params) ,
                                "{\"email_from\":\"a@gmail.com\",\"email_to\":\"b@gmail.com\"}",
                                'Resolve path using two keyword regexps "test_success_3/from-a@gmail.com/to-b@gmail.com/".'
                            );
                            QUnit.start();
                        });

                    });
            })
        }
        return {run: run}
    }
);
