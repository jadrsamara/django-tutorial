from django.shortcuts import HttpResponse

def index(request):
    """
    Index Page
    """
    print(request)
    return HttpResponse("Hello world")
