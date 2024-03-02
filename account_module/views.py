from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return  render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # print(register_form.cleaned_data)
            # todo: register user
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد.')
            else:
                new_user = User(email=user_email,
                                email_active_code=get_random_string(72),
                                is_active=False,
                                username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return  render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'account_module/LoginAdmin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('chart:show_chart'))
        else:
            messages.add_message(request, messages.ERROR, "نام کاربری یا رمز عبور اشتباه است.")
            return render(request, 'account_module/LoginAdmin.html')
