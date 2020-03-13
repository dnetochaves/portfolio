from django.shortcuts import render, HttpResponse

# Create your views here.
def start(request):
    return render(request, 'start.html')
