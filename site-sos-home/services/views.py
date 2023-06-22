from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from accounts.models import User, Employee, Client
from .models import Services
from pages.models import Category
from .forms import UpdateScheduleForm, BudgetForm, UpdateBudgetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ServiceList(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_client:
        client = user
        services = Services.objects.all().filter(client_id=user_id)

        return render(request, 'services.html', {'client':client, 'services':services})
    elif user.is_employee:
        employee = user 
        services = Services.objects.all().filter(employee_id=user_id)
        return render(request, 'services.html', {'employee': employee, 'services':services})
    return render(request, 'services.html')

class DeleteServices(DeleteView):
    model = Services
    template_name = 'delete_services.html'

    def get_success_url(self):
        return reverse('services', kwargs={'user_id': self.object.client_id})

class UpdateSchedule(UpdateView):
    model = Services
    form_class = UpdateScheduleForm
    template_name = 'update_schedule.html'

    def get_success_url(self):
        return reverse('services', kwargs={'user_id': self.object.client_id})

@login_required
def Budget(request, employee_id):
    employee = Employee.objects.get(user_id=employee_id)
    client = Client.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form=BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.description = form.cleaned_data['description']
            budget.price = form.cleaned_data['price']
            budget.client = client
            budget.employee = employee
            budget.save()
            return HttpResponseRedirect(reverse('services', args = [request.user.id]))
    else:
        form=BudgetForm()
    context={'form':form,'employee':employee, 'client':client}
    return render(request, 'budget.html', context)

class UpdateBudget(UpdateView):
    model = Services
    form_class = UpdateBudgetForm
    template_name = 'update_budget.html'

    def get_success_url(self):
        return reverse('services', kwargs={'user_id': self.object.client_id})