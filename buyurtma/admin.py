from django.contrib import admin
from .models import *

@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name')

@admin.register(Maxsulotlar)
class MaxsulotlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')

@admin.register(TypeRoom)
class TypeRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'filial', 'type', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('filial', 'type', 'status')

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'room', 'ordertype', 'client', 'filial', 'people', 'meals','date' , 'date_from', 'date_to', 'ordertime', 'status','comment')
    list_display_links = ('id', 'client')
    date_hierarchy = 'date'
    list_filter = ('ordertype', 'filial',)



