from django.http import JsonResponse
from django.utils import timezone

def api_endpoint(request):
    
    slack_name = request.GET.get('slack_name', 'Paschal Johnpaul')
    track = request.GET.get('track', 'Backend')

    # current day of the week
    current_day = timezone.now().strftime("%A")

    #current UTC time
    utc_time = timezone.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    # JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Paschal-ike/projectZ/tree/main/myproject",
        "github_repo_url": "https://github.com/Paschal-ike/projectZ.git",
        "status_code": 200
    }

    return JsonResponse(response_data)
