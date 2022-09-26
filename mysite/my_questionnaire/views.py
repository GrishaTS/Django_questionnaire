from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'my_questionnaire/index.html'


