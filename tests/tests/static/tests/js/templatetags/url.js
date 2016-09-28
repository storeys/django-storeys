"use strict";

/**
* TODO:
*/

define(
    ['require', 'settings', 'QUnit'],
    function(require, settings, QUnit) {

        var run = function() {
            require(
                ['slib/nunjucks', 'storeys/template/defaulttags'],
                function(nunjucks, defaulttags) {

                    var LOG_PREFIX = "[ defaulttags.url ]",
                        env = new nunjucks.configure();

                    env.addExtension('defaulttags', defaulttags);

                    QUnit.asyncTest(LOG_PREFIX, function (assert) {
                        expect(8);
                        QUnit.stop(7);

                        env.renderString("{% url 'tests' %}", {}, function(err, res){
                            assert.strictEqual(res, '/tests/', 'Render url without params');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts' %}", {}, function(err, res){
                            assert.equal(res, '/test_success/test_success/', 'Render subapp-url without params');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts', numeric='1234567890' %}", {}, function(err, res){
                            equal(res, '/test_success_1/1234567890/', 'Render url with named numeric param');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts', word='test_1234567890' %}", {}, function(err, res){
                            equal(res, '/test_success_2/test_1234567890', 'Render url with named alphanumeric param');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts', email_from='a@gmail.com', email_to='b@gmail.com' %}", {}, function(err, res){
                            equal(res, '/test_success_3/from-a%40gmail.com/to-b%40gmail.com/', 'Render url with named email params');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts', 'test@gmail.com' %}", {}, function(err, res){
                            equal(res, '/test_success_4/test%40gmail.com/', 'Render url with simple email param');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts', '444-666-7777' %}", {}, function(err, res){
                            equal(res, '/test_success_5/phone-444-666-7777/', 'Render url with simple phone param');
                            QUnit.start();
                        });

                        env.renderString("{% url 'receipts', 'test@gmail.com', '444-666-7777' %}", {}, function(err, res){
                            equal(res, '/test_success/test_success_6/test%40gmail.com/phone-444-666-7777/', 'Render url with many simple params');
                            QUnit.start();
                        });
                    });

            })

        }
        return {run: run}
    }
);
