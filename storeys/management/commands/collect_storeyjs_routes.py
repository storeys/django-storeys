import os
import ast
import fnmatch
from storeys.utils import parse_ast_tree
from django.conf import settings
from django.template import loader, Context
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand


TEST_CASE = {
    'base_path': './test',
    'settings_path': 'test/main_app',
}


class StoreysUrlsNotFound(Exception):
    def __init__(self, path):
        self.txt_err = ("'TemplateView.as_view()', 'StoreysView.as_view()' or "
                "'include()' wasn't found at the module: %s If this module"
                " shouldn't be parsed, please add it to 'non_exported_urlpatterns'" % path)
    def __str__(self):
        return self.txt_err


class StoreysUrlsSettingsPyNotFound(Exception):
    def __init__(self):
        self.txt_err = "Can't find settings.py file."
    def __str__(self):
        return self.txt_err


class Command(BaseCommand):
    help = 'Creates a static "urls.js" files inside static folder. '

    def add_arguments(self, parser):
        parser.add_argument('is_test', nargs='?', type=str)

    def handle(self, *args, **options):

        if not hasattr(settings, 'BASE_DIR') or not getattr(
                settings, 'BASE_DIR', False):
            raise ImproperlyConfigured(
                'The collect_storey_routes command needs settings.BASE_DIR to be set.')

        base_path = TEST_CASE['base_path'] if 'is_test' in options.keys() and \
            options['is_test']=='test' else '.'

        settings_path = False
        for root, dirnames, filenames in os.walk(base_path):
            if 'settings.py' in filenames:
                settings_path = os.path.join(settings.BASE_DIR, root)
                settings_root = root
        if not settings_path:
            raise StoreysUrlsSettingsPyNotFound()

        create_js_file(settings_path+'/urls.py', base_path, '.', 'main.html')

        testCases = []
        for root, dirnames, filenames in os.walk(base_path):
            if root != settings_root:
                for filename in fnmatch.filter(filenames, 'urls.py'):
                    urls_file_path = os.path.join(root, filename)[2:]
                    if 'test' in base_path:
                            root = root.replace('/test', '')
                    create_js_file(urls_file_path, base_path, root, 'included.html')


def create_js_file(urls_file_path, base_path, root, template, ):
    with open(urls_file_path) as f:
        source = f.read()
    urls = parse_ast_tree(source)
    if len(urls) == 0:
        raise StoreysUrlsNotFound(urls_file_path)
    else:
        t = loader.get_template('storeys_urls_js/%s' % template)
        c = Context({ 'urls': urls })
        result = t.render(c)
    folder_path = '%s/static/%s' % (base_path, root)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(folder_path + '/urls.js','w') as f:
        f.write(result)
