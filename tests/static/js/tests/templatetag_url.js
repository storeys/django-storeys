"use strict";

/**
* TODO:
*/

define(
    ['require', 'settings'],
    function(require, settings) {

        var run = function() {
            require(
                ['slib/nunjucks', '/submodules/storeys/storeys/js/template/defaulttags.js'],
                function(nunjucks, defaulttags) {

                    var LOG_PREFIX = "[SUCCESS. TEMPLATETAG `URL`]",
                        env = new nunjucks.configure();
                    env.addExtension('defaulttags', defaulttags);


                    var res = env.renderString("{% url 'tests' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render url without params`', function(assert) {
                            expect(1);

                            equal(res, '/tests/');
                        });
                    });

                    var res = env.renderString("{% url 'receipts' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render subapp-url without params`', function(assert) {
                            expect(1);

                            equal(res, '/test_success/test_success/');
                        });
                    });

                    var res = env.renderString("{% url 'receipts', numeric='1234567890' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render with named numeric param`', function(assert) {
                            expect(1);

                            equal(res, '/test_success_1/1234567890/');
                        });
                    });

                    var res = env.renderString("{% url 'receipts', word='asdsaasd_1234567890' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render with named alphanumeric param`', function(assert) {
                            expect(1);

                            equal(res, '/test_success_2/asdsaasd_1234567890');
                        });
                    });

                    var res = env.renderString("{% url 'receipts', email_from='a@gmail.com', email_to='b@gmail.com' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render with named email params`', function(assert) {
                            expect(1);

                            equal(res, '/test_success_3/from-a%40gmail.com/to-b%40gmail.com/');
                        });
                    });

                    var res = env.renderString("{% url 'receipts', 'test@gmail.com' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render with simple email param`', function(assert) {
                            expect(1);

                            equal(res, '/test_success_4/test%40gmail.com/');
                        });
                    });

                    var res = env.renderString("{% url 'receipts', '444-666-7777' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render with simple phone param`', function(assert) {
                            expect(1);

                            equal(res, '/test_success_5/phone-444-666-7777/');
                        });
                    });

                    var res = env.renderString("{% url 'receipts', 'test@gmail.com', '444-666-7777' %}", {}, function(err, res){
                        test(LOG_PREFIX + ' Render with complex params`', function(assert) {
                            expect(1);

                            equal(res, '/test_success/test_success_6/test%40gmail.com/phone-444-666-7777/');
                        });
                    });

            })

        }
        return {run: run}
    }
);
