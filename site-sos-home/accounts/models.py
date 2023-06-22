from django.db import models
from django.contrib.auth.models import AbstractUser
from pages.models import Category
from django.conf import settings


class User(AbstractUser):
    is_client = models.BooleanField('É cliente', default=False)
    is_employee = models.BooleanField('É prestador', default=False)

    name = models.CharField('Nome Completo', max_length=255)
    email = models.CharField('E-mail', max_length=255)
    cpf = models.CharField('CPF', max_length=14)
    birth_date = models.DateField('Data de Nascimento')
    gender = models.CharField('Sexo', max_length=30)
    adress = models.CharField('Endereço', max_length=255)
    imageURL = models.URLField('URL da Foto de Perfil', blank=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #exclusive fields: (NONE)
    
    def __str__(self):
        return self.user.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #exclusive fields: 
    available = models.CharField('Disponibilidade', max_length=255, blank=True, default='Nenhuma')
    job = models.ManyToManyField(Category)

    def __str__(self):
        return self.user.name

RATE_CHOICES = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]

class Rating(models.Model):
    # perfil do avaliador (author)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    # pegando o perfil do avaliado (client/employee)
    profile = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' %(self.author.name, self.rate)

