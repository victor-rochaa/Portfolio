from django import forms
from django.forms import ModelForm
from .models import Services
from pages.models import Category
from django.contrib.admin import widgets

choices = Category.objects.all().values_list('name','name')
CAT_CHOICES = []
for cat in choices:
    CAT_CHOICES.append(cat)

class BudgetForm(forms.ModelForm):
    category = forms.CharField(label='Tipo de Serviço', required=True, widget=forms.Select(choices=CAT_CHOICES, attrs={'class': 'form-control'}))
    description = forms.CharField(label='Descrição do Serviço', required=True, widget = forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='Valor do Orçamento (R$)', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Services
        fields = ('category', 'description','price',)

class UpdateBudgetForm(forms.ModelForm):
    description = forms.CharField(label='Descrição do Serviço', required=True, widget = forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='Valor do Orçamento (R$)', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Services
        fields = ('description','price',)

class UpdateScheduleForm(forms.ModelForm):
    job_date = forms.DateField(label='Data do Serviço', widget=forms.SelectDateWidget(years=range(2020, 2024)))
    job_time = forms.TimeField(label='Horário do Serviço', widget=forms.TimeInput())
    
    class Meta:
        model = Services
        fields = ('job_date', 'job_time')