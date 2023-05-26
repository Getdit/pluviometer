from django.views.generic import TemplateView

from core.models import Location

class LoginView(TemplateView):
    template_name = 'login/login.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context["locations"] = Location.objects.all()
    #     return context
