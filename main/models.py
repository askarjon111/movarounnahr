from account.models import Account
from ckeditor.fields import RichTextField
from board.models import *
from django.db import models


class Calendar(models.Model):
    col = (
        ("bg-primary", "Ko'k"),
        ("bg-warning", "Sariq"),
        ("bg-info", "Fiolet"),
        ("bg-success", "Yashil"),
        ("bg-danger", "Qizil")
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='director', blank=True)
    color = models.CharField(choices=col, default="bg-primary", max_length=255)
    event = models.CharField(max_length=255)
    created_user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='creator')
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Kalendar'


class Objections(models.Model):
    objection = models.TextField()
    solution = models.TextField()
    create_user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.objection

    class Meta:
        verbose_name_plural = 'Ko`p takrorlanadigan e`tirozlar'


class ObjectionWrite(models.Model):
    objection = models.TextField()
    solution = models.TextField()
    create_user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.objection

    class Meta:
        verbose_name_plural = 'Mijoz e`tirozlari'


class Script(models.Model):
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    text = RichTextField()
    create_user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Sotuv Transkript'


class Debtors(models.Model):
    create_user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Lead, on_delete=models.CASCADE)
    summa = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    debt = models.BooleanField()

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name_plural = 'Qarzdorliklar'


class ImportTemplate(models.Model):
    xlsx = models.FileField(upload_to="template")

    def __str__(self):
        return "Excel"

    class Meta:
        verbose_name_plural = 'Excel'