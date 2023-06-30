from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

from accounts.models import Profile
from core.models import Project
from core.forms import AssignUserProjectForm

class ProjectUserListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/project_users.html'

    def get_queryset(self):
        return Profile.objects.filter(projects__id=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.kwargs['pk']
        return context


class ProjectAssignUserView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/project_users.html'
    form_class = AssignUserProjectForm

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs['pk'])
        if not self.request.user.profile.is_researcher:
            raise Exception("User is not owner a researcher")

        user = form.clean_profile()
        project.users.add(user)
        project.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('dashboard:project_user_list', kwargs={'pk': self.kwargs['pk']})

class ProjectUserRemoveView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/project_users.html'
    form_class = AssignUserProjectForm

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs['pk'])
        if not self.request.user.profile.is_researcher:
            raise Exception("User is not owner of project")

        project.users.remove(self.kwargs['user_pk'])
        project.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('dashboard:project_user_list', kwargs={'pk': self.kwargs['pk']})