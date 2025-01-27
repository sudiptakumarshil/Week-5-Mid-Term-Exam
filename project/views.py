from django.views.generic import TemplateView
from brand.models import Brand

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = 'Welcome to my website!'
        context['brands'] = Brand.objects.all()
        return context
