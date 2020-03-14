from django.shortcuts import render, HttpResponse
from .models import Post, Contact
from django.contrib import messages

# Create your views here.
def start(request):
    posts = Post.objects.filter(deleted=False)
    return render(request, 'start.html', {'posts': posts})


def contact(request):
    Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        message = request.POST['message']

    )
    name = request.POST['name']
    messages.success(request, 
    f'Obrigado {name} por entrar em contato, irei atende-lo o mais rapido possivel')
    return render(request, 'start.html')
