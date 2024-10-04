from django.shortcuts import render
from django.shortcuts import redirect

def custom_login_redirect(request):
    # Получаем URL из сессии или задаем значение по умолчанию
    redirect_url = request.session.get('redirect_url', '/default-url')
    return redirect(redirect_url)

def some_view(request):
    return render(request, 'index.html')

def registration_success(request):
    return render(request, 'registration_success.html')

def question_post(request):
    return render(request, 'question.html')
