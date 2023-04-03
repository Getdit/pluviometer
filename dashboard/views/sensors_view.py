from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django import forms

class SensorsView(View):
    template_name = 'sensors/index.html'

    def get(self, request):
        return render(request, self.template_name)
