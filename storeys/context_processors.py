from django.conf import settings

def storeys(request):
    """
    Returns storeys settings
    """
    paths = settings.ROOT_URLCONF.rsplit('.', 1)
    if len(paths) == 2:
        app_path = paths[0].replace('.', '/')

        if len(app_path) > 0:
            app_path = '%s/' % app_path
    else:
        app_path = ''

    return {
        'storeys': {
            'app_path': app_path
        }
    }
