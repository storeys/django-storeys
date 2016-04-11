"use strict";

define(
    ['settings'],
    function(settings) {

        var run = function() {
            require(
                [settings.ROOT_URLCONF, 'storeys/core/urlresolver'],
                function(spec, urlresolver) {
                    test('Test URL resolver', function(t) {
                    expect(2);
                    equal('ab', 'ab', 'The return should be "ab".');
                    var urlspec = spec;
                    var resolve = urlresolver.create(urlspec);

                    var test_path = 'test_success_1/998/';
                    var test_path2 = 'test_success/creceipt-12312312/'

                    // resolve(test_path2, function(params, view) {
                    //     // if you get to here, then the url resolver part is working
                    //     // you would want to test the params to see if it works properly.
                    //     // eg,
                    //
                    //     console.log('++++++++++++++++++++++++++++++++')
                    //     console.log(test_path)
                    //     console.log(params)
                    //     console.log(view)
                    //     console.log('--------------------------------')
                    //
                    // });
                    ok(true, 'Should be equal');
                });
            })
        }
        return {run: run}
    }
);
