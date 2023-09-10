from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import datetime

class ApiView(View):
    def get(self, request, *args, **kwargs):
        slack_name = request.GET.get('Paschal Johnpaul')
        track = request.GET.get('Backend')

        utc_time = datetime.datetime.utcnow()

        response = {
            'slack_name': 'Paschal Johnpaul',
            'current_day': utc_time.strftime('%A'),
            'utc_time': utc_time.isoformat(),
            'track': 'Backend',
            'github_file_url': 'https://github.com/Paschal-ike/projectZ/tree/main/myproject',
            'github_repo_url': 'https://github.com/Paschal-ike/projectZ.git',
            'status_code': 200,
            
        } 
        
        if 'github_file_url' in request.GET:
            response['github_file_url'] = request.GET['github_file_url']

        if 'github_repo_url' in request.GET:
            response['github_repo_url'] = request.GET['github_repo_url']

        return JsonResponse(response)

        

# Create your views here.
