from django.shortcuts import render
from django.views import View


class DashboardView(View):
    template_name = 'dashboard/index.html'

    def get(self, request):
        chart_data = [
            {
            'labels': ['Janeiro', 'Fevereiro', 'Março'],
            'values': [10, 42, 30]
            },
            {
            'labels': ['Abril', 'Maio', 'Junho'],
            'values': [23, 50, 60]
            },
            {
            'labels': ['Janeiro', 'Fevereiro', 'Março'],
            'values': [40, 20, 10]
            },
            {
            'labels': ['Abril', 'Maio', 'Junho'],
            'values': [40, 50, 60]
            },
            {
            'labels': ['Janeiro', 'Fevereiro', 'Março'],
            'values': [10, 20, 30]
            },
            {
            'labels': ['Abril', 'Maio', 'Junho'],
            'values': [40, 50, 60]
            }
        ]

        return render(request, self.template_name, {'chart_data': chart_data})
