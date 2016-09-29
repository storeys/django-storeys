import os
import ast
import fnmatch
import shutil
from storeys.utils import parse_ast_tree
from django.conf import settings
from django.template import loader, Context
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand


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

        if not hasattr(settings, 'ROOT_URLCONF') or not getattr(
                settings, 'ROOT_URLCONF', False):
            raise ImproperlyConfigured(
                'The collect_storey_routes command needs settings.ROOT_URLCONF to be set.')

        if 'is_test' in options.keys() and options['is_test'] == 'test':
            core_url_module = 'test_dir.%s' % settings.ROOT_URLCONF
        else:
            core_url_module = settings.ROOT_URLCONF

        try:
            non_exported_urlpatterns = getattr(
                __import__(core_url_module,
                           fromlist=['non_exported_urlpatterns']),
                'non_exported_urlpatterns'
            )
            if not isinstance(non_exported_urlpatterns, tuple):
                non_exported_urlpatterns = [non_exported_urlpatterns]
        except AttributeError:
            non_exported_urlpatterns = ()

        ne_names, ne_module_names = [], []
        for non_exported_urlpattern in non_exported_urlpatterns:
            if 'module_name' in non_exported_urlpattern:
                ne_module_names.append(non_exported_urlpattern['module_name'])
            else:
                ne_names.append(non_exported_urlpattern['name'])

        base_path = settings.BASE_DIR + ('/test_dir'  if 'is_test' \
            in options.keys() and options['is_test'] == 'test' else '')
        root_urlconf_path = settings.ROOT_URLCONF.replace('.', '/').replace('/urls', '')
        settings_path = '%s/%s' % (base_path, root_urlconf_path)
        settings_root = root_urlconf_path

        # if os.path.isdir('%s/static' % settings_path):
        #    shutil.rmtree('%s/static' % settings_path)
        create_js_file(settings_path+ '/urls.py', base_path,
                       'main.html', ne_names, ne_module_names)

        print 'Storeys. Excluded url-names: ', ne_names

        for value in os.listdir(base_path):
            dir_path = "%s/%s" % (base_path, value)
            if os.path.isdir(dir_path):
                subdir_list = os.listdir(dir_path)
                if 'urls.py' in subdir_list and settings_path != dir_path:
                    # if 'static' in subdir_list:
                    #    shutil.rmtree('%s/static' % dir_path)
                    if not is_module_excluded(dir_path.replace('/', '.'), ne_module_names):
                        create_js_file('%s/urls.py' % dir_path, base_path,
                                       'included.html', [], [])
                    else:
                        print 'Storeys. This module was excluded: ', dir_path


def create_js_file(urls_file_path, base_path, template, ne_names, ne_module_names):
    root = urls_file_path.replace(base_path, '').replace('/urls.py','')
    with open(urls_file_path) as f:
        source = f.read()
    urls = parse_ast_tree(source, ne_names, ne_module_names)
    if len(urls) == 0:
        raise StoreysUrlsNotFound(urls_file_path)
    else:
        t = loader.get_template('storeys_urls_js/%s' % template)
        result = t.render({'urls': urls})
    folder_path = '%s%s/static%s' % (base_path, root, root)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(folder_path + '/urls.js', 'w') as f:
        f.write(result)


def is_module_excluded(base, ne_module_names):
    for excluded_module in ne_module_names:
        excluded_module = excluded_module.replace('.urls','')
        if base[-len(excluded_module):] == excluded_module or \
           excluded_module+'.' in base:
            return True
    return False
