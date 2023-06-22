from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Client, Employee, Rating
from pages.models import Category
from django.db import transaction

GENDER_CHOICES = [('Masculino','Masculino'), ('Feminino','Feminino'), ('Prefiro Não Informar', 'Prefiro Não Informar')]

class ClientSignUpForm(UserCreationForm):
    name = forms.CharField(label='Nome Completo', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Data de Nascimento', required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    gender = forms.CharField(label='Sexo', required=True, widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}))
    adress = forms.CharField(label='Endereço', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imageURL = forms.URLField(label='URL da Foto de Perfil', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.cpf = self.cleaned_data.get('cpf')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.gender = self.cleaned_data.get('gender')
        user.adress = self.cleaned_data.get('adress')
        user.imageURL = self.cleaned_data.get('imageURL')
        user.save()

        client = Client.objects.create(user=user)
        client.save()

        return user

AVAILABLE_CHOICES = [('Manhã','Manhã'), ('Tarde','Tarde'), ('Noite', 'Noite')]

class EmployeeSignUpForm(UserCreationForm):
    name = forms.CharField(label='Nome Completo', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Data de Nascimento', required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    gender = forms.CharField(label='Sexo', required=True, widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}))
    adress = forms.CharField(label='Endereço', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imageURL = forms.URLField(label='URL da Foto de Perfil', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    available = forms.CharField(label='Disponibilidade', required=False, widget=forms.CheckboxSelectMultiple(choices=AVAILABLE_CHOICES))
    job = forms.ModelMultipleChoiceField(label='Profissão/Especialidades', required=True, queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.cpf = self.cleaned_data.get('cpf')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.gender = self.cleaned_data.get('gender')
        user.adress = self.cleaned_data.get('adress')
        user.imageURL = self.cleaned_data.get('imageURL')
        user.save()
        
        employee = Employee.objects.create(user=user)
        employee.available = self.cleaned_data.get('available')
        employee.job.add(*self.cleaned_data.get('job'))
        employee.save()

        return user


RATE_CHOICES = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]

class RatingForm(forms.ModelForm):
    body = forms.CharField(label='Comentário', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    rate = forms.ChoiceField(label='Nota', required=True, choices = RATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Rating
        fields = ('body', 'rate')

class UpdateRateForm(forms.ModelForm):
    body = forms.CharField(label='Comentário', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    rate = forms.ChoiceField(label='Nota', required=True, choices = RATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Rating
        fields = ('body', 'rate')

class UpdateProfileForm(forms.ModelForm):
    name = forms.CharField(label='Nome Completo', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Data de Nascimento', required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    adress = forms.CharField(label='Endereço', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imageURL = forms.URLField(label='URL da Foto de Perfil', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('name', 'email', 'cpf', 'birth_date', 'adress', 'imageURL')

class UpdateEmployeeProfileForm(forms.ModelForm):
    available = forms.CharField(label='Disponibilidade', required=False, widget=forms.CheckboxSelectMultiple(choices=AVAILABLE_CHOICES))
    job = forms.ModelMultipleChoiceField(label='Profissão/Especialidades', required=True, queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Employee
        fields = ('available', 'job')