from django.views.generic import View
from django.shortcuts import render


class ProjectsSensorsView(View):
    template_name = 'project_sensors/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'devices': [
                {
                    'mac': 'AB:CD:EF:12:34:56',
                    'model': 'Device A',
                    'last_call': '2023-05-20 09:15:00',
                    'location': 'Local A',
                    'latitude': '123.456',
                    'longitude': '789.012'
                },
                {
                    'mac': '12:34:56:78:90:AB',
                    'model': 'Device B',
                    'last_call': '2023-05-19 14:30:00',
                    'location': 'Local B',
                    'latitude': '456.789',
                    'longitude': '012.345'
                },
                {
                    'mac': 'EF:GH:IJ:KL:MN:OP',
                    'model': 'Device C',
                    'last_call': '2023-05-18 19:45:00',
                    'location': 'Local C',
                    'latitude': '789.012',
                    'longitude': '345.678'
                },
            ],
        }
        return render(request, self.template_name, context=context)
