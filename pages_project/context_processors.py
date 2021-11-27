from django.conf import settings

def analytics_import(request):
    return {
        'ANALYTICS_ID': settings.ANALYTICS_ID
    }
