
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def get_details(request):
    return Response(
        {
            'email': 'damilolajoseph91@gmail.com',
            'current_datetime': timezone.now().strftime('%Y-%m-%dtH:%M:%SZ'),
            'github_url': 'https://github.com/Nobelwrite/personaldetails'
        }
    )

