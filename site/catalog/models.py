from django.db import models
from django.urls import reverse
from datetime import date
import datetime
# Create your models here.
class departament(models.Model):
    name = models.CharField(max_length = 200, help_text="Введите название отдела")

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200, help_text="Введите должность")

    def __str__(self):
        return self.name

class worker(models.Model):
    id = models.BigAutoField(primary_key=True)
    FIO = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to = 'photo/', height_field=None, width_field=None, max_length=100, default='cat.jpg')
    date_of_birth = models.DateField(null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    Departament = models.ManyToManyField(departament,help_text="Выберете отдел для сотрудника")

    def __str__(self):
        return self.FIO

    def get_absolute_url(self):
        return reverse('worker-detail', args=[str(self.id)])

    def display_dep(self):
        return ', '.join([ dep.name for dep in self.Departament.all()[:3] ])
    display_dep.short_description = 'Departament'

    def age(self):
        if self.date_of_birth:
            today = date.today()
            if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                return (today.year - self.date_of_birth.year) - 1
            else:
                return today.year - self.date_of_birth.year
        else:
            return ""


class news(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    short_desc = models.CharField(max_length = 250)
    date = models.DateField(null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])



    class Meta:
        ordering = ["-date"]

class product(models.Model):
    id = models.BigAutoField(primary_key = True)
    name  = models.CharField(max_length=80)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'img/', height_field=None, width_field=None, max_length=100, default='cat.jpeg')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])
