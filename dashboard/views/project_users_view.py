from django.views.generic import View
from django.shortcuts import render


class ProjectsUsersView(View):
    template_name = 'project_users/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            "users": [{'name': "erik", 'email': 'email@email.com'}, {'name': "erik", 'email': 'email@email.com'}, {'name': "erik", 'email': 'email@email.com'}]
        }
        return render(request, self.template_name, context=context)
