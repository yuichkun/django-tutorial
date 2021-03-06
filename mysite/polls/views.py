from django.http import HttpResponse

# Create your views here.

def index(request):
    import datetime
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return HttpResponse("Hello, world. You're at the polls index." + now)

def detail(request, question_id):
    return HttpResponse("You're looking at question {}.".format(question_id))

def result(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))
