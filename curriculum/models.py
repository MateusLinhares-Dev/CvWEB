from typing import Iterable
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='fotos/')
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Perfil"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateField()
    current_work = models.BooleanField(default=True)
    end = models.DateField(blank=True, null=True, verbose_name="Desligamento")

    def clean(self):
        if not self.current_work and not self.end:
            raise ValidationError({
                'end': "Preencha o campo de quando ocorreu o desligamento!."
            }) # type: ignore
        return super().clean()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Experiência"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Projeto"

class Testemunho(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    photo = models.ImageField(upload_to='testemunhos/', blank=True, null=True)
    date_create = models.DateTimeField(default=now)
    confirm = models.BooleanField(default=False)  # Para controle manual no admin

    def __str__(self):
        return self.name


class Skill(models.Model):
    class Suit(models.IntegerChoices):
        INICIANTE = 1
        INTERMEDIARIO = 2
        AVANCADO = 3
        ESPECIALISTA = 4
        MASTER = 5

    title = models.CharField(max_length=100, verbose_name="Skill")
    classification = models.IntegerField(choices=Suit.choices, default=Suit.INICIANTE, verbose_name="Nivel de conhecimento") # type: ignore
    points = models.IntegerField(editable=False, verbose_name="Pontuação")

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if self.classification:
            label_classification = self.Suit(self.classification)
            self.points = label_classification.value
        super(Skill, self).save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=70, verbose_name="Nome")
    message = models.TextField(blank=False, null=False, verbose_name="Mensagem") # type: ignore
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Telofone", region="BR", default="+55") # type: ignore

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Contato"