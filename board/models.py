from django.db import models
from account.models import Account, Company


class CategoryProduct(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name


class Region(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Viloyat'


class District(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tuman'


class Lead(models.Model):
    status_types = (
        (0, "Boshlang'ich"),
        (1, "Muhokamada"),
        (2, "Qaror qabul qilish"),
        (3, "Shartnoma"),
        (4, "Yo'qotish"),
        (5, "Muvaffaqqiyatli yakunlash"),
        (6, "Promouter"),
    )
    degr = (
        (1, "Past"),
        (2, "O`rta"),
        (3, "Yuqori"),
    )
    joinByChoise = (
        (0, "Odatiy"),
        (1, "Telegram orqali")
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(default=0)

    finishedPrice = models.IntegerField(default=0)
    company = models.CharField(max_length=255, null=True, blank=True)
    companyAddress = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(default=0, choices=status_types)
    date = models.DateTimeField(auto_now_add=True)
    finishedDate = models.DateTimeField(null=True, blank=True)
    created_user = models.ForeignKey(Account, on_delete=models.CASCADE)

    degree = models.IntegerField(choices=degr, default=1)
    phone = models.CharField(max_length=255, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    birthday = models.DateField(null=True, blank=True)
    categoryproduct = models.ManyToManyField(CategoryProduct, blank=True)
    abcxyz = models.CharField(max_length=255, null=True)
    step1 = models.TextField(default="-", blank=True, null=True)
    step2 = models.TextField(default="-", blank=True, null=True)
    step3 = models.TextField(default="-", blank=True, null=True)
    step4 = models.TextField(default="-", blank=True, null=True)
    step5 = models.TextField(default="-", blank=True, null=True)
    status_date = models.DateTimeField(auto_now_add=True)

    where = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    debt = models.IntegerField(default=0)

    joinBy = models.IntegerField(default=0, choices=joinByChoise)
    tg_chatid = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class LeadAction(models.Model):
    status_types = (
        (0, "Lead yaratildi"),
        (1, "Lead taxrirlandi"),
        (2, "Status o'zgardi"),
        (3, "Izoh qo'shildi"),
    )
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    status = models.IntegerField(default=0, choices=status_types)
    oldStatus = models.IntegerField(default=0)
    newStatus = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    color = models.CharField(default="primary", max_length=255)
    changer = models.ForeignKey(Account, on_delete=models.CASCADE)


class Task(models.Model):
    status_types = (
        (0, "Ro'yxatga olindi"),
        (1, "Bajarilmoqda"),
        (2, "Bajarildi"),
        (3, "O'chirildi"),
    )
    name = models.CharField(max_length=255)
    note = models.TextField()
    status = models.IntegerField(default=0, choices=status_types)
    date = models.DateTimeField(auto_now_add=True)
    finishedDate = models.DateTimeField(null=True)
    created_user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Telegram_user(models.Model):
    step_choise = (
        (0, 'Start'),
        (1, 'Contact'),
        (2, 'Name'),
        (3, 'Company'),
        (4, 'Company Address'),
        (5, 'Finished')
    )
    chat_id = models.IntegerField(default=0)
    name = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    companyAddress = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True)
    step = models.IntegerField(default=1, choices=step_choise)
    token = models.CharField(max_length=255, null=True, blank=True)
