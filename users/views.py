from django.shortcuts import render

def some_view(request):
    return render(request, 'index.html')

def registration_success(request):
    return render(request, 'registration_success.html')
