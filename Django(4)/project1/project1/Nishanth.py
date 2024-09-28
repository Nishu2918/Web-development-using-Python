from django.http import HttpResponse # type: ignore

def Registration(request):
    return HttpResponse('<h1>Registration Page</h1>')

def Aboutus(request):
    return HttpResponse('<h2>Welcome to college</h1>')
