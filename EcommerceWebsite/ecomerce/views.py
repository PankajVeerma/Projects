from django.http import HttpResponse
def home(request):
    return HttpResponse("Wellcome to home page")