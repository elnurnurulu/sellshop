from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.views.generic import View,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import get_user_model
from user.forms import  RegisterForm,UpdatePersonalInfoForm,LoginForm,CustomPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from user.utils import account_activation_token
from order.forms import BillingAddressForm
from django.db.models import Q
from order.models import Basket, BillingAddress,Country
from user.tasks import send_email_confirmation


from user.forms import (RegisterForm, ResetPasswordForm, 
        LoginForm,
        CustomSetPasswordForm
        )

USER = get_user_model()

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'forgot-password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Sizin yeni sifreniz teyin edildi')
        return super().get_success_url()
   


class ResetPasswordView(PasswordResetView):
    template_name = 'forgot-password.html'
    form_class = ResetPasswordForm
    email_template_name = 'email/reset-password-mail.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return super().get_success_url()    


# def login_register(request):
#     if not request.user.is_authenticated:
#         reg_form = RegisterForm()
#         login_form = LoginForm()
#         next_page = request.GET.get('next','/')
#         if request.method == 'POST':
#             if request.POST.get('submit') == 'login':
#                 login_form = LoginForm(data=request.POST)
#                 if login_form.is_valid():
#                     user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
#                     if user is not None:
#                         django_login(request, user)
#                         messages.add_message(request, messages.SUCCESS, 'You signed in!')
#                         return redirect(next_page)        
#                     else:
#                         messages.add_message(request, messages.ERROR, 'Email or password is wrong!')
#             elif request.POST.get('submit') == 'register':
#                 reg_form = RegisterForm(data=request.POST)
#                 if reg_form.is_valid():
#                     user = reg_form.save()
#                     user.set_password(reg_form.cleaned_data['password'])
#                     user.save()
#                     return redirect('login')
#         context = {
#                 'reg_form': reg_form,
#                 'login_form':login_form,
#             }
#         return render(request, 'login-register.html', context)
#     else:
#         return redirect('/')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login-register.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_form'] = RegisterForm()
        context['login_form'] = LoginForm()

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'login-register.html'
    success_url = reverse_lazy('login')
    context_object_name = 'reg_form'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        form.instance.set_password(form.cleaned_data['password'])
        user.is_active = False
        user.save()
        current_site = self.request.META['HTTP_HOST']
        send_email_confirmation(user, current_site)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_form'] = RegisterForm()

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

@login_required
def account(request):
    form_acc = BillingAddressForm
  
    form_pers_info = UpdatePersonalInfoForm()
    
    if request.method == 'POST':
        if request.POST.get('submit') == 'address':
            form_acc = BillingAddressForm(data=request.POST)
            if form_acc.is_valid():
                form_acc.save()
            return redirect(reverse_lazy('account'))
        elif request.POST.get('submit') == 'personal_info_submit':
            form_pers_info = UpdatePersonalInfoForm(data=request.POST)
            if form_pers_info.is_valid():
                request.user.first_name = request.POST.get('first_name')
                request.user.last_name = request.POST.get('last_name')
                request.user.email = request.POST.get('email')
                request.user.birthdate = request.POST.get('birthdate')
                request.user.sex = request.POST.get('sex')
                request.user.save()
                return redirect(reverse_lazy('account'))
    context = {
        'form_acc':form_acc,
       
        'form_pers_info':form_pers_info,
    } 
    if request.user.is_authenticated:
        return render(request, "my-account.html")
    return render(request, "error-404.html")


class Activate(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = USER.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, USER.DoesNotExist):
            user = None
        if user.is_active:
            messages.add_message(request, messages.SUCCESS, 'EMail has been confirm')
            return redirect(reverse_lazy('login'))
        elif user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Email confirmed')
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Email didnot confirm')
            return redirect(reverse_lazy('/'))


@login_required
def logout(request):
    django_logout(request)
    return redirect('/')

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'changepassword.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Ugurla sifreniz deyisdi')
        return super().get_success_url()

