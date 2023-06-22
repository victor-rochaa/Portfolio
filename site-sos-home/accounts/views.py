from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ClientSignUpForm, EmployeeSignUpForm, RatingForm, UpdateRateForm, UpdateEmployeeProfileForm, UpdateProfileForm
from .models import User, Client, Employee, Rating
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def signup(request):
    return render(request, 'registration/signup_choice.html')

class ClientSignUp(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_client.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        success(self.request, user)
        login(self.request, user)
        return redirect('home')

class EmployeeSignUp(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_employee.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        success(self.request, user)
        login(self.request, user)
        return redirect('home')

@login_required
def DetailProfile(request, user_id):
    user = User.objects.get(id=user_id)
    rating = Rating.objects.all().filter(profile_id=user_id).order_by('-rate')

    # calcula a nota media 
    rates = []
    for rate in rating:
        rates.append(rate.rate)
    if len(rates)>0:
        avg_rate = sum(rates)/len(rates)
    else:
        avg_rate=5

    age = date.today().year - user.birth_date.year
    temp_user = user
    if temp_user.is_employee:
        employee = Employee.objects.get(user_id=user_id)

        #horários de disponilidade
        available = employee.available
        a = available.split("'")
        disp = []
        if len(a)==3:
            disp.append(a[1])
        elif len(a)==5:
            disp.append(a[1])
            disp.append(a[3])
        elif len(a)==7:
            disp.append(a[1])
            disp.append(a[3])
            disp.append(a[5])
               
        temp_user.age = age
        temp_user.job = employee.job
        temp_user.available = employee.available
        context = {'employee': temp_user, 'disp':disp, 'rating':rating, 'avg_rate':avg_rate}
        return render(request, 'registration/detail_profile.html', context)
    else:
        temp_user.age = age
        context = {'client': temp_user, 'rating':rating, 'avg_rate':avg_rate}
        return render(request, 'registration/detail_profile.html', context)

class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = UpdateEmployeeProfileForm
    template_name = 'registration/update_employee.html'

    def get_object(self, queryset=None):
        user = Employee.objects.filter(pk=self.request.user.id).first()
        return user

    def get_success_url(self):
        return reverse('user-profile')

class UserUpdate(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'registration/update_user.html'

    def get_object(self, queryset=None):
        user = User.objects.filter(pk=self.request.user.id).first()
        return user
    
    def get_success_url(self):
        return reverse('user-profile')

@login_required
def MyProfile(request):
    user = request.user
    rating = Rating.objects.all().filter(profile_id=user.id).order_by('-rate')

    # calcula a nota media 
    rates = []
    for rate in rating:
        rates.append(rate.rate)
    if len(rates)>0:
        avg_rate = sum(rates)/len(rates)
    else:
        avg_rate=5

    age = date.today().year - user.birth_date.year
    temp_user = user
    if user.is_employee:
        employee = Employee.objects.get(user_id=request.user.id) 

        #horários de disponilidade
        available = employee.available
        a = available.split("'")
        disp = []
        if len(a)==3:
            disp.append(a[1])
        elif len(a)==5:
            disp.append(a[1])
            disp.append(a[3])
        elif len(a)==7:
            disp.append(a[1])
            disp.append(a[3])
            disp.append(a[5])
        
        temp_user.age = age
        temp_user.job = employee.job
        temp_user.available = employee.available
        context = {'user': temp_user, 'disp':disp, 'rating':rating, 'avg_rate':avg_rate}
        return render(request, 'registration/user_profile.html', context)
        
    else:
        temp_user.age = age
        context = {'user': temp_user, 'rating':rating, 'avg_rate':avg_rate}
        return render(request, 'registration/user_profile.html', context)

@login_required
def Rate(request, user_id):
    user = request.user
    profile = User.objects.get(pk=user_id) 

    if request.method == 'POST': 
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.author = user
            rate.profile = profile
            rate.save()
            return HttpResponseRedirect(reverse('detail', args = [user_id]))
    else:
        form = RatingForm()

    context = {'form':form, 'profile':profile}

    return render(request, 'rate.html', context)

class UpdateRate(UpdateView):
    model = Rating
    form_class = UpdateRateForm
    template_name = 'update_rate.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'user_id': self.object.profile_id})

class DeleteRate(DeleteView):
    model = Rating
    template_name = 'delete_rate.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'user_id': self.object.profile_id})

def success(request, user):
    html_content = render_to_string('registration/email_confirmation.html', {'user': user})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        'Confirmação de cadastro no SOS Home', 
        text_content, 
        settings.EMAIL_HOST_USER,
        [user.email]
        )
        
    email.attach_alternative(html_content, 'text/html')

    email.fail_silently = False
    email.send()
    user = User.objects.get(id=user.id)
    context = {'user': user}
    return render(request, 'registration/email_confirmation.html', context)