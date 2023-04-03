from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django import forms


class ReportsView(View):
    template_name = 'reports/index.html'

    def get(self, request):
        datas = [
            1,2,3,4,5,6
        ]

        return render(request, self.template_name, {'datas': datas })
