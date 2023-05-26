from django.views.generic import View
from django.shortcuts import render


class SensorReadsView(View):
    template_name = 'sensor_reads/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'datamodels': [
                {
                    'name': 'Dado A',
                    'description': 'Descrição do Dado A',
                    'model': 'Modelo A',
                    'reference_tag': 'Tag A',
                    'alert_per_time': '02:00:00',
                    'warning_alert': 10.5,
                    'danger_alert': 8.0
                },
                {
                    'name': 'Dado B',
                    'description': 'Descrição do Dado B',
                    'model': 'Modelo B',
                    'reference_tag': 'Tag B',
                    'alert_per_time': None,
                    'warning_alert': 20.0,
                    'danger_alert': 15.0
                },
                {
                    'name': 'Dado C',
                    'description': 'Descrição do Dado C',
                    'model': 'Modelo C',
                    'reference_tag': 'Tag C',
                    'alert_per_time': '01:30:00',
                    'warning_alert': 5.0,
                    'danger_alert': 3.0
                }
            ]

        }
        return render(request, self.template_name, context=context)
