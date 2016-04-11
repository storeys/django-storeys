from django.views.generic.base import TemplateView


class TempView(TemplateView):
    prerender_content = 'test'
    
    def get_context_data(self, **kwargs):
        return ''


def include_test(arg):
    pass
