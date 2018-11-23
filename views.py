from django.http import HttpResponse
from django.shortcus import redirect

def index(request):
    return HttpREspone("index")

def login(request):
    return Redirect('./index')
