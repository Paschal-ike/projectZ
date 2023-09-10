from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

class ApiView(View):
    def get(self, request, *args, **kwargs):
        slack_name = request.GET.get('Paschal Johnpaul')
        track = request.GET.get('backend')

        utc_time = datetime.datetime.utcnow()

        response = {
            'slack_name': slack_name,
            'current_day': utc_time.strftime('%A'),
            'utc_time': utc_time.isoformat(),
            'track': track,
            'github_file_url': None,
            'github_repo_url': 'https://github.com/Paschal-ike/projectZ.git',
            'status_code': 200,
        }

        

# Create your views here.
