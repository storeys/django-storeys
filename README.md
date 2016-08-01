Django Storeys
==============
[![Docs](https://readthedocs.org/projects/django-storeys/badge/)](http://django-storeys.readthedocs.org) [![CI](https://travis-ci.org/storeys/django-storeys.svg?branch=master)](https://travis-ci.org/storeys/django-storeys) [![Coverage](https://coveralls.io/repos/github/storeys/django-storeys/badge.svg?branch=master)](https://coveralls.io/github/storeys/django-storeys?branch=master) 
[![Version](https://badge.fury.io/py/django-storeys.svg)](https://pypi.python.org/pypi/django-storeys)

Example of how-to start using `Storeys` with Django.
This project scans all applications inside it and creates similar applications with the same routes suitable for `Storeys` framework.
All `urls.py` files in django project will be scanned and all of them that returns an `TemplateView` or `StoreysView` will be ported to Storeys routes `urls.js`. All other views will be ignored!

#### Example:
```
# applicaation/urls.py

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
Also you have an ability to add a list of urlpatterns that will be ignored by Storeys parser.
####Eexample:

```
# application/urls.py
...
# Url patterns `admin.site.urls`, and named patterns with names `exclude2` and `test` will be ignored by parser.

non_exported_urlpatterns = (
    urlref(module_name='admin.site.urls'),
    urlref(name='exclude2'),
    urlref(name='test'),
)

```

#Install application

You have to clone all submodules and install requirements:
```
git submodule sync --recursive
git submodule update --init --recursive

pip install virtualenv
virtualenv venv/
source ./venv/bin/activate
pip install -r requirements.txt
```

---

# Run application

Just run `collectstatic_storeys` django management command. It will create `urls.js` files with routes based on `urls.py`.

```
python tests/manage.py collectstatic_storeys
```

And you need to run `nginx` or another local version of web server.
```
# nginx config:
server {
   listen      8000;

   location / {
       root your_path/django-storeys;
   }
}
```
And then just visit `127.0.0.1:8000/tests/` into your browser

To Run Tests
============

```
git submodule sync --recursive
git submodule update --init --recursive

pip install virtualenv
virtualenv venv/
source ./venv/bin/activate
pip install -r requirements.txt
python tests/manage.py
```
