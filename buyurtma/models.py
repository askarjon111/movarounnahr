from django.db import models
from django.contrib.auth.models import User
from board.models import Lead
from account.models import Company, Filial
from django.contrib.auth import get_user_model

class TypeRoom(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(TypeRoom, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=0)
    capacity = models.IntegerField()
    def __str__(self):
        return self.name


class Books(models.Model):
    ordertype = models.IntegerField()  # 0 - xona, 1 - dastavka, 2 - saboy
    client = models.ForeignKey(Lead, on_delete=models.SET_NULL, null=True)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True)
    address = models.TextField(null=True, blank=True)
    people = models.IntegerField(null=True, blank=True)
    meals = models.CharField(max_length=255, null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.SET_NULL, null=True, related_name='books')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_from = models.DateTimeField(null=True)
    date_to = models.DateTimeField(null=True)
    ordertime = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)
    comment=models.TextField(blank=True,null=True)
    def __str__(self):
        try:
            return self.client.name
        except:
            return "O'chirilgan"


class Maxsulotlar(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    chois = (
        ('1', 'bor'),
        ('2', 'yoq'),
    )
    bor_yoqligi = models.CharField(choices=chois, max_length=255)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    izoh = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

