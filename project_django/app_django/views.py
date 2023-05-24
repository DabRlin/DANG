from django.shortcuts import render
from .models import MyModel


def my_view(request):
    message = "Hello, World!"
    return render(request, 'my_template.html', {'message': message})

