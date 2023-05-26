from django.views.generic import TemplateView

from core.models import Location

class ProjectView(TemplateView):
    template_name = 'project/project.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context["locations"] = Location.objects.all()
    #     return context