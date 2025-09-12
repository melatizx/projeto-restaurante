from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField
from phonenumber_field.modelfields import PhoneNumberField

class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    cpf = BRCPFField(unique=True)
    numero = PhoneNumberField(region="BR", unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome