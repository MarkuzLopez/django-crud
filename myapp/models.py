from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title()
    
# step create model for BD
# after in cosole the migrations: 
# python manage.py makemigrations and python manage.py migrate
class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Ingrese email valido",
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="el numero debe tener entre 9 y 15 digitos",                
            )
        ],
        verbose_name="Numero de Telefono"
    )
    
    def __str__(self):
         return f"{self.name} - {self.email}"
         