from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django import forms

class ChartView(View):
    template_name = 'chart/index.html'

    def get(self, request):        
        labels = ["January", "February", "March", "April", "May", "June", "July"]
        data = [65, 59, 80, 81, 56, 55, 40]        
        return render(request, self.template_name, {"data": {"labels":labels, "data":data}})
