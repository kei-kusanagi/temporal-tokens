from django.shortcuts import render
from django.shortcuts import render

from django.contrib.auth.tokens import PasswordResetTokenGenerator

def home(request):

    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(request.user)

    # is_valid = Token.objects.filter(user=request.user).filter(token=token).exists()

    return render(request, 'home.html', {
        'token': token
    })

def validate_token(request):
    token = request.GET.get('token')

    token_generator = PasswordResetTokenGenerator()
    is_valid = token_generator.check_token(request.user, token)

    return render(request, 'home.html', {
        'is_valid': is_valid
    })