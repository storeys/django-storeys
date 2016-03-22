import os
from django.conf import settings
from django.test import TestCase
from django.template import TemplateDoesNotExist
from django.core.management import call_command
from storeys.management.commands.collect_storeyjs_routes import StoreysUrlsNotFound


class UrlsParseSuccess(TestCase):

    def test_urls_parse_success(self):
        call_command('collect_storeyjs_routes', *['tests'], **{})
        self.assertTrue(os.path.join(settings.BASE_DIR, 'additional_app/static/additional_app/urls.js'))
        self.assertTrue(os.path.join(settings.BASE_DIR, 'tests/static/storeys/urls.js'))

        with open(os.path.join(settings.BASE_DIR, 'additional_app/static/additional_app/urls.js')) as f:
            file_content = f.read()
        self.assertEqual(file_content.count("url("), 2)
        self.assertEqual(file_content.count(
            "url("), file_content.count("test_success"))

        with open(os.path.join(settings.BASE_DIR, 'tests/static/tests/urls.js')) as f:
            file_content = f.read()
        self.assertEqual(file_content.count("url("), 2)
        self.assertEqual(file_content.count("test_success"), 2)

        # Check. 'static' folder wasn't created at the excluded app.
        self.assertFalse(os.path.isdir(os.path.join(settings.BASE_DIR, 'additional_app2/static')))


class UrlsParseErrors(TestCase):

    def test_urls_parse_template_not_exist(self):
        template_not_exists_flag = False

        # Replase template path with broken path
        file_path = os.path.join(settings.BASE_DIR, 'additional_app/urls.py')
        content = file_read(file_path)
        file_write(file_path, content.replace('storeys_urls_js/main.html',
                                              'notexist/main.html'))
        with self.assertRaises(TemplateDoesNotExist) as e:
            call_command('collect_storeyjs_routes', *['tests'], **{})
        file_write(file_path, content)

    def test_urls_parse_entries_not_found(self):
        template_not_exists_flag = False

        # Replase all needed functions with uninteresting for script functions
        file_path = os.path.join(settings.BASE_DIR, 'additional_app/urls.py')
        content = file_read(file_path)
        empty_content = content.replace('TemplateView.as_view', 'TempView.as_view')\
            .replace('StoreysView.as_view', 'TempView.as_view')\
            .replace('include(', 'include_test(')

        file_write(file_path, empty_content)
        with self.assertRaises(StoreysUrlsNotFound) as e:
            call_command('collect_storeyjs_routes', *['tests'], **{})
        file_write(file_path, content)


def file_read(path):
    f = open(path, 'r')
    file_content = f.read()
    return file_content


def file_write(path, content):
    f = open(path, 'w')
    f.seek(0)
    f.truncate()
    f.write(content)
