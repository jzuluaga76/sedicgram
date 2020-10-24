from django.http import HttpResponse

def hola(request):
    return HttpResponse('Hello')
    
def saludo(request):
    return HttpResponse('buen dia')
