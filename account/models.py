from django.contrib.auth.models import AbstractUser
from django.db import models
# from buyurtma.models import Filial



class Company(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    manzil = models.CharField(max_length=255)
    max_worker_count = models.IntegerField(default=0)
    worker_count = models.IntegerField(default=0)
    creator = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True)

    sms_token = models.TextField(null=True)
    sms_balans = models.IntegerField(default=0)
    sms_from = models.CharField(max_length=255, null=True, blank=True)
    sms_callback_url = models.CharField(max_length=255, null=True, blank=True)
    sms_activated = models.BooleanField(default=False)

    tg_token = models.TextField(null=True)

    def __str__(self):
        return self.name

class Filial(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bot_token = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    chat_id = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Account(AbstractUser):
    is_director = models.BooleanField(default=False)
    is_callcenter = models.BooleanField(default=False)
    token = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def save(self, *args, **kwargs):
        if self.company:
            count = Account.objects.filter(company=self.company).count()
            self.company.worker_count = count
            self.company.save()
        super(Account, self).save(*args, **kwargs)
