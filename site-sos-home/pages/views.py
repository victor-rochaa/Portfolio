from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category
from accounts.models import User, Employee
from django.urls import reverse_lazy


def handler404(request, exception):
    return render(request, '404.html')

class Home(ListView):
    model = Category
    template_name = 'home.html'

class About(ListView):
    model = Category
    template_name = 'about.html'

class Categories(ListView):
    model = Category
    template_name = 'categories.html'
    fields = '__all__'

def CategoryDetail(request, cat_id):
    cat = get_object_or_404(Category, pk=cat_id)
    employees = Employee.objects.filter(job=cat_id)
    context = {'cat':cat, 'users':employees}
    return render(request, 'category_details.html', context)

def Search(request):
    return render(request, 'search.html')

def SearchCategory(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cat = Category.objects.filter(name__contains=searched)
        return render(request, 'search_category.html', {'searched':searched,'cat':cat}) 
    else:
        return render(request, 'search_category.html')