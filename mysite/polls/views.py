from django.http import HttpResponse

# Create your views here.

def index(request):
    import datetime
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return HttpResponse("Hello, world. You're at the polls index." + now)
