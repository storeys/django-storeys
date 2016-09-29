Django Storeys
==============
[![Docs](https://readthedocs.org/projects/django-storeys/badge/)](http://django-storeys.readthedocs.org) [![CI](https://travis-ci.org/storeys/django-storeys.svg?branch=master)](https://travis-ci.org/storeys/django-storeys) [![Coverage](https://coveralls.io/repos/github/storeys/django-storeys/badge.svg?branch=master)](https://coveralls.io/github/storeys/django-storeys?branch=master)
[![Version](https://badge.fury.io/py/django-storeys.svg)](https://pypi.python.org/pypi/django-storeys)



## Introduction

`django-storeys` is the server counterpart of `storeys`. It lets you generate the skeleton of a single page app using storeys, basing on an existing Django app.


## Install application

```
cd ${MY_DJANGO_APP}
mkdir -p ${MY_DJANGO_APP}/submodules
git submodule add submodules/django-storeys
git submodule update --recursive --init
ln -s submodules/django-storeys lib/storeys
```

## Generate skeleton

Run `collect_storeys_routes` django management command.
It collects `urls.js` files with routes based on `urls.py`.

```
python tests/manage.py collect_storeys_routes
```

This command scans all applications inside the current project for `urls.py` to create route files 'urls.js` for the client-side use.

It creates stub for `TemplateView` or `StoreysView`, and other views is ignored!


#### Example:
```
# application/urls.py

# Will be included into Storeys routes
url('^test/$', StoreysView.as_view(
        template_name='index.html',
    ),
    name='tests'
),

# Will be included into Storeys routes
url('^another_test/$', TemplateView.as_view(
        template_name='index.html',
    ),
    name='tests_view'
),

# Will be ignored and not included into routes. Due to `TestView`
url('^another_test/$', TestView.as_view(
        template_name='index.html',
    ),
    name='tests_view'
),
```

### Non-exported apps

Storeys let you specific `urlpatterns` to exclude. The references of excluded urls can be added in `non_exported_urlpatterns` tuples.

#### Example:

```
# application/urls.py
# ...

# Url patterns `admin.site.urls`, and named patterns with names `exclude2` and `test` will be ignored by parser.

non_exported_urlpatterns = (
    urlref(module_name='admin.site.urls'),
    urlref(name='exclude2'),
    urlref(name='test'),
)

```

#### Running the server:

```
python tests/manage.py runserver
```

And then just visit `127.0.0.1:8000/tests/` into your browser



## Test

### Django Tests
```
git submodule sync --recursive
git submodule update --init --recursive

./bin/test.sh test
```

### QUnit Tests
```
git submodule sync --recursive
git submodule update --init --recursive

./bin/test.sh runserver

## Open browser at http://localhost:8000/tests
```


## Examples

```
git submodule sync --recursive
git submodule update --init --recursive

./bin/example.sh runserver

## Open browser at http://localhost:8000/
```

