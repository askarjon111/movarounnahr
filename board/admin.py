from django.contrib import admin
from board.models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_display_links = ('id', 'name')
    list_filter = ('region',)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'company', 'companyAddress', 'status', 'date', 'created_user', 'phone']
    list_filter = ['created_user__company', 'status']
    search_fields = ['name']


@admin.register(LeadAction)
class LeadActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'lead', 'status', 'oldStatus', 'newStatus', 'date', 'note', 'changer']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'note', 'status', 'date', 'finishedDate', 'created_user']
    list_filter = ['created_user__company', 'status']
    search_fields = ['name']


@admin.register(Telegram_user)
class Telegram_userAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'name', 'company', 'companyAddress', 'phone', 'step']
