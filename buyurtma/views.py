from cmath import log
import json
from datetime import datetime

import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from board.models import Task
from board.serializers import TaskSerializer
from .models import *
from .serializers import BooksSerializer
from main.models import *

#filialdagi va call centrdagi xonalar bosh yoki boshmasligi
class Room(LoginRequiredMixin, TemplateView):
    template_name = 'room.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # if self.request.user.is_callcenter:
        #     return redirect('/buyurtma/buyurtmaolish/')
        # el
        # if self.request.user.is_director:
        #     return redirect('')

        return super(Room, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Room, self).get_context_data(**kwargs)
        context['rooms'] = 'active'
        context['filial'] = Filial.objects.all()
        if self.request.user.is_callcenter:
            pass
        else:
            context['rooms0'] = Rooms.objects.filter(status=0, filial=self.request.user.filial)
            context['rooms1'] = Rooms.objects.filter(status=1, filial=self.request.user.filial)

        return context


class Products(LoginRequiredMixin, TemplateView):
    template_name = 'products.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return self.handle_no_permission()
    #
    #     if self.request.user.is_callcenter:
    #         return redirect('/buyurtma/products/')

    def get_context_data(self, *args, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context['maxsulot'] = Maxsulotlar.objects.all()
        context['filial'] = Filial.objects.all()
        return context


#buyurtmalar filialdagi
class Book(LoginRequiredMixin, TemplateView):
    template_name = 'book.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish/')
        # elif self.request.user.is_director:
        #     return redirect('')

        return super(Book, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Book, self).get_context_data(**kwargs)
        today = datetime.today()
        sana0 = datetime(today.year, today.month, today.day)
        context['book'] = 'active'
        context['books'] = Books.objects.filter(date__gte=sana0, filial=self.request.user.filial)

        return context

# savdo page callcentr uchun
class EtirozCall(LoginRequiredMixin, TemplateView):
    template_name = 'etirozcall.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(EtirozCall, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(EtirozCall, self).get_context_data(**kwargs)
        context['etirozcall'] = 'active'
        if self.request.user.is_director:
            context['objections'] = Objections.objects.filter(create_user__company=self.request.user.company)
            context['objectionwrite'] = ObjectionWrite.objects.filter(create_user__company=self.request.user.company)
            try:
                context['ckeditor'] = Script.objects.filter(create_user__company=self.request.user.company).first()
            except:
                context['ckeditor'] = None
        else:
            context['objections'] = Objections.objects.filter(create_user=self.request.user)
            context['objectionwrite'] = ObjectionWrite.objects.filter(create_user=self.request.user)
            try:
                context['ckeditor'] = Script.objects.filter(create_user=self.request.user).first()
            except:
                context['ckeditor'] = None

        return context

#xana buyurtmalari callcentrda
class Calendar(LoginRequiredMixin, TemplateView):
    template_name = 'xonabuyurtma.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(Calendar, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Calendar, self).get_context_data(**kwargs)
        context['calendar'] = 'active'
        today = datetime.today()
        newdate = datetime(today.year, today.month, today.day)
        context['books'] = Books.objects.filter(ordertype=0, status=0, date__gte=newdate)
        context['filial'] = Filial.objects.all()
        return context

#xana buyurtmalari filialda
class CalendarFil(LoginRequiredMixin, TemplateView):
    template_name = 'xonabuyurtmafil.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish/')
        # elif self.request.user.is_director:
        #     return redirect('')

        return super(CalendarFil, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CalendarFil, self).get_context_data(**kwargs)
        context['xonabuyurtmafil'] = 'active'
        today = datetime.today()
        newdate = datetime(today.year, today.month, today.day)
        user = self.request.user
        print(user)
        context['books'] = Books.objects.filter(ordertype=0,  status=0, date__gte=newdate, filial_id=user.filial.id)
        return context


# def Band(request):
#     id = request.GET.get('id')
#     r = Rooms.objects.get(id=id)
#     r.status = 1
#     r.save()

#     return redirect('rooms')


# def Bosh(request):
#     id = request.GET.get('id')
#     r = Rooms.objects.get(id=id)
#     r.status = 0
#     r.save()

#     return redirect('rooms')


def BookRange(request):
    date1 = request.GET.get('sana1')
    date2 = request.GET.get('sana2')
    dt1 = date1.split('/')
    dt2 = date2.split('/')
    sana1 = datetime(int(dt1[2]), int(dt1[0]), int(dt1[1]))
    sana2 = datetime(int(dt2[2]), int(dt2[0]), int(dt2[1]))

    if sana1 == sana2:
        bs = Books.objects.filter(date__gte=sana1, filial__company=request.user.company)
        d = []
        for b in bs:
            try:
                t = {
                    'ordertype': b.ordertype,
                    'client': b.client.name,
                    'people': b.people,
                    'phone': b.client.phone,
                    'meal': b.meals,
                    'room': b.room.name,
                    'filial': b.filial.name,
                    'date_from': b.date_from.strftime('%m-%d-%Y %H:%M'),
                    'date_to': b.date_to.strftime('%m-%d-%Y %H:%M'),
                    'comment': b.comment,
                }
            except:
                t = {
                    'ordertype': b.ordertype,
                    'client': b.client.name,
                    'people': b.people,
                    'phone': b.client.phone,
                    'meal': b.meals,
                    # 'room': b.room.name,
                    'filial': b.filial.name,
                    'date_from': b.date_from.strftime('%m-%d-%Y %H:%M'),
                    'date_to': b.date_to.strftime('%m-%d-%Y %H:%M'),
                    'comment': b.comment,
                }
            d.append(t)
    dt = {
        'books': d
    }
    return JsonResponse(dt)

#buyurtma olish callcentrdan
class BuyurtmaOlish(LoginRequiredMixin, TemplateView):
    template_name = 'buyurtmaolish.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(BuyurtmaOlish, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(BuyurtmaOlish, self).get_context_data(**kwargs)
        context['buyurtmaolish'] = 'active'
        context['filial'] = Filial.objects.all()
        if self.request.user.is_callcenter:

            context['olibketish'] = Books.objects.filter(ordertype=2, status=0)
            context['yetkazibberish'] = Books.objects.filter(ordertype=1, status=0)
            context['bandqilish'] = Books.objects.filter(ordertype=0, status=0)
            context['maxsulot'] = Maxsulotlar.objects.all()
            context['maxsulotjs'] = json.dumps(list(Maxsulotlar.objects.values('id', 'price', 'name', 'filial', 'bor_yoqligi')))
            context['mijoz'] = Lead.objects.filter(created_user__company=self.request.user.company)
        else:
            context['olibketish'] = Books.objects.filter(ordertype=2, status=0, filial=self.request.user.filial)
            context['yetkazibberish'] = Books.objects.filter(ordertype=1, status=0, filial=self.request.user.filial)
            context['bandqilish'] = Books.objects.filter(ordertype=0, status=0, filial=self.request.user.filial)

        return context


# xona band qilish filialdan
class BuyurtmaOlishFil(LoginRequiredMixin, TemplateView):
    template_name = 'buyurtmaolishfil.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish/')
        # elif self.request.user.is_director:
        #     return redirect('')

        return super(BuyurtmaOlishFil, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(BuyurtmaOlishFil, self).get_context_data(**kwargs)
        context['buyurtmaolishfil'] = 'active'
        context['filial'] = Filial.objects.all()
        context['mijoz'] = Lead.objects.filter(created_user__company=self.request.user.company)
        context['bandqilish'] = Books.objects.filter(ordertype=0, status=0, filial=self.request.user.filial)

        return context

#aktiv buyurtmalar filialda
class Aktiv(LoginRequiredMixin, TemplateView):
    template_name = 'activ.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish/')
        # elif self.request.user.is_director:
        #     return redirect('')

        return super(Aktiv, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Aktiv, self).get_context_data(**kwargs)
        context['aktiv'] = 'active'

        context['olibketish'] = Books.objects.filter(ordertype=2, status=0, filial=self.request.user.filial)
        context['yetkazibberish'] = Books.objects.filter(ordertype=1, status=0, filial=self.request.user.filial)
        context['bandqilish'] = Books.objects.filter(ordertype=0, status=0, filial=self.request.user.filial)

        return context

# callcentrdagi calendar
class CalenAppCall(LoginRequiredMixin, TemplateView):
    template_name = 'apps-calendarcall.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(CalenAppCall, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CalenAppCall, self).get_context_data(**kwargs)
        context['appcalendarcall'] = 'active'
        context['users'] = Account.objects.filter(is_director=True)

        return context

# filialdagi sms
class SmsFilial(LoginRequiredMixin, TemplateView):
    template_name = 'smsfilial.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(SmsFilial, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SmsFilial, self).get_context_data(**kwargs)
        context['lead_count'] = Lead.objects.filter(created_user__company=self.request.user.company).count()
        context['smsfilial'] = 'active'
        # context['illness'] = CategoryProduct.objects.all()
        context['lead_status_types'] = Lead.status_types
        context['leads'] = Lead.objects.filter(created_user__company=self.request.user.company)

        return context


class Clients(LoginRequiredMixin, TemplateView):
    template_name = 'clientscall.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(Clients, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Clients, self).get_context_data(**kwargs)
        context['client'] = 'active'
        if self.request.user.is_director:
            context['clients'] = Lead.objects.filter(created_user__company=self.request.user.company)
        else:
            context['clients'] = Lead.objects.filter(created_user=self.request.user)
        context['template_excel'] = ImportTemplate.objects.first()
        return context

#sms callcenter
class SmsCall(LoginRequiredMixin, TemplateView):
    template_name = 'smscall.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(SmsCall, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SmsCall, self).get_context_data(**kwargs)
        context['lead_count'] = Lead.objects.filter(created_user__company=self.request.user.company).count()
        context['smscall'] = 'active'
        # context['illness'] = CategoryProduct.objects.all()
        context['lead_status_types'] = Lead.status_types
        context['leads'] = Lead.objects.filter(created_user__company=self.request.user.company)

        return context

def checkPhone(phone):
    try:
        int(phone)
        if len(phone) == 12:
            return True, phone
        else:
            return False, None
    except:
        return False, None


def sendSmsOneContact(phone, message):
    dt = {
        "messages": [
            {
                "recipient": phone,
                "message-id": "abc000000001",
                "sms": {
                    "originator": "3700",
                    "content": {
                        "text": message
                    }
                }
            }
        ]
    }
    result = requests.post(url="http://91.204.239.44/broker-api/send",
                           auth=('movoraunnahr', '5iZ4iF3aK4'),
                           headers={'content-type': 'application/json'},
                           data=json.dumps(dt))
    return result


def SmsGatewayF(request):
    if request.method == 'POST':
        sms = request.POST['sms']
        status_codes = request.POST.get('user_type')
        if status_codes == "":
            status = []
        else:
            status = json.loads(status_codes)
        leads_id = request.POST.getlist('leads')
        leads = Lead.objects.filter(id__in=leads_id)
        success_send_count = 0
        error_send_count = 0
        Leads = Lead.objects.filter(status__in=status, created_user__company=request.user.company)
        for lead in Leads:
            can, phone = checkPhone(lead.phone)
            if can:
                result = sendSmsOneContact(phone, sms)
                if result.status_code == 200:
                    success_send_count += 1
                else:
                    error_send_count += 1
            else:
                error_send_count += 1
        for lead in leads:

            can, phone = checkPhone(lead.phone)
            if can:
                result = sendSmsOneContact(phone, sms)
                if result.status_code == 200:
                    success_send_count += 1
                else:
                    error_send_count += 1
            else:
                error_send_count += 1
        if success_send_count > 0:
            messages.success(request, f"{success_send_count} ta sms jo'natildi!")
        if error_send_count > 0:
            messages.error(request, f"{error_send_count} ta sms jo'natilmadi!")
    return redirect('smsfilial')


def OlibKetish(request):
    try:
        r = request.POST
        ism = r['ism']
        fam = r['fam']
        tel = r['tel']
        filial = r['filial']
        comment = r['comment']
        total_buyurtma = ''

        try:
            id = r['buyurtma1']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni1']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['buyurtma2']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni2']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['buyurtma3']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni3']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['buyurtma4']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni4']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma5']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni5']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma6']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni6']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma7']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni7']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma8']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni8']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma9']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni9']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma10']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni10']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma11']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni11']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma12']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni12']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma13']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni13']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma14']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni14']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma15']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni15']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma16']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni16']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma17']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni17']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma18']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni18']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma19']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni19']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma20']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni20']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma21']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni21']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma22']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni22']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma23']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni23']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma24']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni24']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma25']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni25']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma26']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni26']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma27']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni27']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma28']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni28']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma29']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni29']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma30']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni30']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['buyurtma31']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni31']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        sana = r['sana']
        where = r['where']
        birthday = r.get('birthday')
        ss = sana.split('T')
        birr = ss[0]
        ikkii = ss[1]

        bir = birr.split('-')
        ikki = ikkii.split(':')

        yangisana = datetime(int(bir[0]), int(bir[1]), int(bir[2]), int(ikki[0]), int(ikki[1]))
        try:
            l = Lead.objects.get(phone=tel)
        except:
            if birthday == "":
                l = Lead.objects.create(name=ism, surname=fam, phone=tel, created_user=request.user, where=where, comment=comment)
            else:
                l = Lead.objects.create(name=ism, surname=fam, phone=tel, created_user=request.user, where=where,comment=comment, birthday=birthday)
            messages.success(request, 'Yangi mijoz qo`shildi')
        Books.objects.create(ordertype=2, client=l, filial_id=filial, meals=total_buyurtma, ordertime=yangisana,comment=comment)
        fil = Filial.objects.get(id=filial)
        sn = sana.split('T')
        ids = fil.chat_id.split(' ')
        for id in ids:
            text = 'Olib ketishga: \n\nMijoz: ' + ism + '\nTelefon: ' + tel + '\nBuyurtma: ' + total_buyurtma + '\nSana: ' + \
                   sn[0] + ' ' + sn[1]
            url = 'https://api.telegram.org/bot' + fil.bot_token + '/sendMessage?chat_id='
            requests.get(url + id + '&text=' + text)
        messages.success(request, 'Buyurtma qabul qilindi')
    except Exception as e:
        print(e)
        messages.error(request, 'Buyurtma qabul qilinmadi')
    return redirect('buyurtmaolish')


def YetkazibBerish(request):
    try:
        r = request.POST
        ism = r['ism']
        fam = r['fam']
        tel = r['tel']
        filial = r['filial']
        comment= r['comment']
        total_buyurtma = ''
        try:
            id = r['yet_buyurtma']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma1']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni1']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['yet_buyurtma2']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni2']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['yet_buyurtma3']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni3']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['yet_buyurtma4']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni4']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma5']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni5']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma6']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni6']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma7']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni7']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma8']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni8']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma9']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni9']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma10']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni10']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma11']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni11']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma12']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni12']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma13']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni13']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma14']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni14']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma15']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni15']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma16']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni16']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma17']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni17']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma18']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni18']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma19']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni19']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma20']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni20']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma21']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni21']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma22']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni22']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma23']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['buyurtma_soni23']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma24']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni24']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma25']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni25']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma26']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni26']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma27']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni27']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma28']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni28']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma29']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni29']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma30']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni30']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['yet_buyurtma31']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['yet_buyurtma_soni31']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        sana = r['sana']
        address = r['address']
        where = r['where']
        birthday = r.get('birthday')
        ss = sana.split('T')
        birr = ss[0]
        ikkii = ss[1]

        bir = birr.split('-')
        ikki = ikkii.split(':')

        yangisana = datetime(int(bir[0]), int(bir[1]), int(bir[2]), int(ikki[0]), int(ikki[1]))
        try:
            l = Lead.objects.get(phone=tel)
        except:
            if birthday == "":
                l = Lead.objects.create(name=ism, surname=fam, phone=tel, created_user=request.user, where=where)
            else:
                l = Lead.objects.create(name=ism, surname=fam, phone=tel, created_user=request.user, where=where,
                                        birthday=birthday)
            messages.success(request, 'Yangi mijoz qo`shildi')
        Books.objects.create(ordertype=1, client=l, filial_id=filial, meals=total_buyurtma, ordertime=yangisana, address=address, comment=comment)
        fil = Filial.objects.get(id=filial)
        sn = sana.split('T')
        ids = fil.chat_id.split(' ')
        for id in ids:
            text = 'Yetkazib berish: \n\nMijoz: ' + ism + '\nTelefon: ' + tel + '\nBuyurtma: ' + total_buyurtma + '\nManzil: ' + address + '\nSana: ' + \
                   sn[0] + ' ' + sn[1]
            url = 'https://api.telegram.org/bot' + fil.bot_token + '/sendMessage?chat_id='
            requests.get(url + id + '&text=' + text)
        messages.success(request, 'Buyurtma qabul qilindi')
    except Exception as e:
        print(e)
        messages.error(request, 'Buyurtma qabul qilinmadi')
    return redirect('buyurtmaolish')

from django.db.models import Q

def BandQilish(request):
    user = request.user
    try:
        r = request.POST
        ism = r['ism']
        fam = r['fam']
        filial = r['filial']
        quan = r['quan']
        tel = r['tel']
        sanafrom = r['sanafrom']
        sanato = r['sanato']
        comment=r['comment']
        xona = r['xona']
        where = r['where']

        total_buyurtma = ''
        try:
            id = r['band_buyurtma']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma1']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni1']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['band_buyurtma2']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni2']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['band_buyurtma3']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni3']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        try:
            id = r['band_buyurtma4']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni4']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma5']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni5']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma6']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni6']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma7']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni7']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma8']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni8']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma9']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni9']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma10']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni10']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma11']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni11']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma12']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni12']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma13']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni13']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma14']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni14']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma15']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni15']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma16']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni16']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma17']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni17']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma18']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni18']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma19']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni19']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma20']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni20']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma21']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni21']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma22']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni22']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma23']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni23']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma24']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni24']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma25']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni25']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma26']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni26']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma27']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni27']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma28']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni28']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma29']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni29']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma30']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni30']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass
        try:
            id = r['band_buyurtma31']
            print(id)
            buyurtma = Maxsulotlar.objects.get(id=id)
            print(buyurtma)
            buyurtma_soni = r['band_buyurtma_soni31']
            total_buyurtma += "" + buyurtma.name + '    ' + buyurtma_soni + 'ta   '""
        except:
            pass

        birthday = r.get('birthday')
        ssfrom = sanafrom.split('T')
        ssto = sanato.split('T')

        birrfrom = ssfrom[0]
        ikkiifrom = ssfrom[1]
        birrto = ssto[0]
        ikkiito = ssto[1]

        birfrom = birrfrom.split('-')
        ikkifrom = ikkiifrom.split(':')
        birto = birrto.split('-')
        ikkito = ikkiito.split(':')

        yangisanafrom = datetime(int(birfrom[0]), int(birfrom[1]), int(birfrom[2]), int(ikkifrom[0]), int(ikkifrom[1]))
        yangisanato = datetime(int(birto[0]), int(birto[1]), int(birto[2]), int(ikkito[0]), int(ikkito[1]))
        try:
            l = Lead.objects.get(phone=tel)
        except:
            if birthday == "":
                l = Lead.objects.create(name=ism, surname=fam, phone=tel, created_user=request.user, where=where)
            else:
                l = Lead.objects.create(name=ism, surname=fam, phone=tel, created_user=request.user, where=where,
                                        birthday=birthday)
            messages.success(request, 'Yangi mijoz qo`shildi')
        
        b = Books.objects.create(ordertype=0, client=l, filial_id=filial, meals=total_buyurtma, people=quan,
                                 date_from=yangisanafrom, date_to=yangisanato,
                                 room_id=xona,comment=comment)
        fil = Filial.objects.get(id=filial)
        sfrom = sanafrom.split('T')
        sto = sanato.split('T')
        ids = fil.chat_id.split(' ')
        xona = Rooms.objects.get(id=xona)
                      
        for id in ids:
                     text = 'Xona band qilish: \n\nMijoz: ' + l.name + '\nTelefon: ' + l.phone + '\nXona: ' + xona.name + '\nNechi kishi: ' + quan + '\nSana: ...dan  ' + \
                     sfrom[0] + ' ' + sfrom[1]+'\nSana: ...gacha ' +  sto[0] + ' ' + sto[1]
                     url = 'https://api.telegram.org/bot' + fil.bot_token + '/sendMessage?chat_id='
                     requests.get(url + id + '&text=' + text)
                      
        messages.success(request, 'Buyurtma qabul qilindi')                 


        # b = Books.objects.create(ordertype=0, client=l, filial_id=filial, meals=total_buyurtma, people=quan, date_from=yangisanafrom, date_to=yangisanato,
        #                          room_id=xona,comment=comment)
        # # rr= Rooms.objects.get(id=xona)
        # # rr.status = 1;
        # # rr.save()
        # fil = Filial.objects.get(id=filial)
        # sfrom = sanafrom.split('T')
        # sto = sanato.split('T')
        # ids = fil.chat_id.split(' ')
        # xona = Rooms.objects.get(id=xona)
        # for id in ids:
        #     text = 'Xona band qilish: \n\nMijoz: ' + l.name + '\nTelefon: ' + l.phone + '\nXona: ' + xona.name + '\nNechi kishi: ' + quan + '\nSana: ...dan  ' + \
        #            sfrom[0] + ' ' + sfrom[1]+'\nSana: ...gacha ' +  sto[0] + ' ' + sto[1]
        #
        #     url = 'https://api.telegram.org/bot' + fil.bot_token + '/sendMessage?chat_id='
        #     requests.get(url + id + '&text=' + text)
        # messages.success(request, 'Buyurtma qabul qilindi')
    except:
        messages.error(request, 'Buyurtma qabul qilinmadi')
    if user.filial is not None:
        return redirect('buyurtmaolishfil')
    else:
        return redirect('buyurtmaolish')

def Change(request):
    id = request.GET.get('id')
    b = Books.objects.get(id=id)
    b.status = 1
    b.save()
    try:
        b.room.status = 0
        b.room.save()
    except:
        pass
    return redirect('buyurtmaolish')

def changemaxsulot(request):
    id = request.GET.get('id')
    b = Maxsulotlar.objects.get(id=id)
    print(b, b.bor_yoqligi, '?')
    if b.bor_yoqligi == '1':
        b.bor_yoqligi = 2
        b.save()
    else:
        b.bor_yoqligi = 1
        b.save()
    return redirect('products')


def GetXona(request):
    id = request.GET.get('id')
    sanafrom = request.GET.get('sanafrom')
    sanato = request.GET.get('sanato')
    # ssfrom = sanafrom.split('T')
    # ssto = sanato.split('T')

    # birrfrom = ssfrom[0]
    # ikkiifrom = ssfrom[1]
    # birrto = ssto[0]
    # ikkiito = ssto[1]

    # birfrom = birrfrom.split('-')
    # ikkifrom = ikkiifrom.split(':')
    # birto = birrto.split('-')
    # ikkito = ikkiito.split(':')

    # yangisanafrom = datetime(int(birfrom[0]), int(birfrom[1]), int(birfrom[2]), int(ikkifrom[0]), int(ikkifrom[1]))
    # yangisanato = datetime(int(birto[0]), int(birto[1]), int(birto[2]), int(ikkito[0]), int(ikkito[1]))
    # c=Books.objects.all()
    # for i in c:
    #     if not ((i.date_from > yangisanafrom and i.date_from < yangisanato) or (i.date_to > yangisanafrom and i.date_to < yangisanato)):      
    #                 #newsanafrom<date_from<newsanato                                #newsanafrom<date_to<newsanato
    rooms = Rooms.objects.exclude(
                (
                        Q(books__date_from__lte=sanafrom)#date_from<newsanafrom<date_to
                        & Q(books__date_to__gte=sanafrom)
                ) | (
                        Q(books__date_from__lte=sanato)  #date_from<newsanato<date_to
                        & Q(books__date_to__gte=sanato)
                )).filter(filial=id)
    x = []
    for i in rooms:
                    t = {
                        'id': i.id,
                        'name': i.name,
                        'type': i.type.name,
                        'capacity': i.capacity,
                    }
                    x.append(t)
    dt = {
                    'rooms': x
                }
    return JsonResponse(dt)
     

def GetXonalar(request):
    id = request.GET.get('id')
    r0 = Rooms.objects.filter(filial_id=id, status=0)
    r1 = Rooms.objects.filter(filial_id=id, status=1)
    x = []
    for i in r0:
        t = {
            'id': i.id,
            'name': i.name,
            'type': i.type.name,
            'capacity': i.capacity,
        }
        x.append(t)
    y = []
    for i in r1:
        m = {
            'id': i.id,
            'name': i.name,
            'type': i.type.name,
            'capacity': i.capacity,

        }
        y.append(m)
    dt = {
        'room0': x,
        'room1': y
    }

    return JsonResponse(dt)


def GetBuyurtmalar(request):
    id = request.GET.get('id')
    today = datetime.today()
    newdate = datetime(today.year, today.month, today.day)
    books = Books.objects.filter(ordertype=0, status=0, filial_id=id, date__gte=newdate)
    bk = []
    for b in books:
        t = {
            'ordertype': b.ordertype,
            'name': b.client.name,
            'phone': b.client.phone,
            'filial': b.filial.name,
            'people': b.people,
            'room':  b.room.name,
            'date': b.date.strftime('%Y-%m-%d %H:%M'),
            'date_from': b.date_from.strftime('%Y-%m-%d %H:%M'),
            'date_to': b.date_to.strftime('%Y-%m-%d %H:%M'),
            'status': b.status,
            'comment': b.comment
        }
        bk.append(t)
    dt = {
        'books': bk
    }
    return JsonResponse(dt)


def GetUser(request):
    id = request.GET.get('id')
    user = Lead.objects.get(id=id)
    dt = {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "phone": user.phone,
        "birthday": user.birthday,
        "where": user.where,
    }

    return JsonResponse(dt)

def getmaxsulot(request):
    id = request.GET.get('id')
    max = Maxsulotlar.objects.get(id=id)
    dt = {
        "id": max.id,
        "name": max.name,
        "price": max.price,
    }

    return JsonResponse(dt)



def BookDelete(request):
    books = Books.objects.all()
    for b in books:
        b.delete()
    return JsonResponse({'message': 'dane'})


class BooksViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


def check_book(req):
    today = datetime.today().strftime('%Y-%m-%d %H:%M')
    t = today.split(' ')
    t1 = t[0].split('-')
    t2 = t[1].split(':')
    today = datetime(int(t1[0]), int(t1[1]), int(t1[2]), int(t2[0]), int(t2[1]))
    bs = Books.objects.filter(ordertype=0, status=0)
    for b in bs:
        exp = b.date_from.strftime('%Y-%m-%d %H:%M')
        tt = exp.split(' ')
        tt1 = tt[0].split('-')
        tt2 = tt[1].split(':')
        exp = datetime(int(tt1[0]), int(tt1[1]), int(tt1[2]), int(tt2[0]), int(tt2[1]))
        if exp < today:
            b.room.status = 1
            b.room.save()

    return JsonResponse({'message': 'dane'})


def changeroom1(request):
    id = request.GET.get('id')
    r = Rooms.objects.get(id=id)
    r.status = 1
    r.save()

    return redirect('rooms')


def changeroom0(request):
    id = request.GET.get('id')
    r = Rooms.objects.get(id=id)
    r.status = 0
    r.save()

    return redirect('rooms')

# task board filial
class TaskClass1(LoginRequiredMixin, TemplateView):
    template_name = 'task1.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish')

        return super(TaskClass1, self).dispatch(request, *args, **kwargs)
    def get_context_data(self, *args, **kwargs):
        super(TaskClass1, self).get_context_data(**kwargs)
        tasks = Task.objects.filter(status__lt=2, created_user=self.request.user)
        group1 = tasks.filter(status=0)
        group2 = tasks.filter(status=1)
        all_tasks = []
        for i in tasks:
            all_tasks.append({
                "id": i.id,
                "name": i.name,
                "date": i.date.strftime("%Y-%m-%d, %H:%M"),
                "note": i.note
            })

        context = {
            "Task1": "active",
            "group1": group1,
            "group2": group2,
            "all_tasks": json.dumps(all_tasks)
        }
        return context

# task callcenter
class TaskClass(LoginRequiredMixin, TemplateView):
    template_name = 'task2.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(TaskClass, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        super(TaskClass, self).get_context_data(**kwargs)
        tasks = Task.objects.filter(status__lt=2, created_user=self.request.user)
        group1 = tasks.filter(status=0)
        group2 = tasks.filter(status=1)
        all_tasks = []
        for i in tasks:
            all_tasks.append({
                "id": i.id,
                "name": i.name,
                "date": i.date.strftime("%Y-%m-%d, %H:%M"),
                "note": i.note
            })

        context = {
            "Task": "active",
            "group1": group1,
            "group2": group2,
            "all_tasks": json.dumps(all_tasks)
        }
        return context


@api_view(['POST'])
def create_task(request):
    try:
        data = request.data
        name = data['name']
        user = int(data['user'])
        task = Task.objects.create(name=name, created_user_id=user)
        return Response(TaskSerializer(task).data)
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def change_task_status(request):
    try:
        data = request.data
        taskId = int(data['task'])
        status = int(data['status'])
        task = Task.objects.get(id=taskId)
        task.status = status
        if status == 2:
            task.finishedDate = datetime.now()
        task.save()
        return Response(TaskSerializer(task).data)
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def note_task(request):
    try:
        data = request.data
        taskId = int(data['task'])
        note = data['note']
        task = Task.objects.get(id=taskId)
        task.note = note
        task.save()
        return Response(TaskSerializer(task).data)
    except:
        return Response({"message": "Error"}, 404)


# qarzdorlar filial
class Debt1(LoginRequiredMixin, TemplateView):
    template_name = 'debt1.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.is_callcenter:
            return redirect('/buyurtma/buyurtmaolish')

        return super(Debt1, self).dispatch(request, *args, **kwargs)
    def get_context_data(self, *args, **kwargs):
        context = super(Debt1, self).get_context_data(**kwargs)
        context['debt1'] = 'active'
        context['debtors'] = Lead.objects.filter(debt__gt=0, created_user__company=self.request.user.company)

        return context

# qarzdorlar callcenter
class Debt(LoginRequiredMixin, TemplateView):
    template_name = 'debt2.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.is_director:
            return redirect('home')
        elif self.request.user.filial:
            return redirect('/buyurtma/')

        return super(Debt, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Debt, self).get_context_data(**kwargs)
        context['debt'] = 'active'
        context['debtors'] = Lead.objects.filter(debt__gt=0, created_user__company=self.request.user.company)

        return context

#qarz tarixi
def DebtHistory(request):
    if request.method == "GET":
        id = request.GET.get('id')
        lead = Lead.objects.get(id=id)
        ol = Debtors.objects.filter(user_id=id, debt=1, user__created_user__company=request.user.company).order_by(
            '-id')
        ber = Debtors.objects.filter(user_id=id, debt=0, user__created_user__company=request.user.company).order_by(
            '-id')

        context = {
            'olingan': ol,
            'berilgan': ber,
            'usr': id,
            'lead': lead,
        }

        return render(request, 'debthistory2.html', context)



def AddDebt(request):
    if request.method == "POST":
        r = request.POST
        u_id = r['u_id']
        debt = r['debt']
        izoh = r['izoh']
        summa = int(r['summa'])
        user = Lead.objects.get(id=u_id)
        if debt == '1':
            user.debt += summa
            user.save()
        else:
            user.debt -= summa
            user.save()
        Debtors.objects.create(user_id=u_id, summa=summa, comment=izoh, debt=debt, create_user=request.user)
        url = '/buyurtma/debthistory/?id=' + u_id

        return redirect(url)

def AddDebtor(request):
    if request.method == "POST":
        r = request.POST
        u_id = r['debtor']
        debt = int(r['debt'])
        user = Lead.objects.get(id=u_id)
        user.debt += debt
        user.save()
        Debtors.objects.create(user_id=u_id, summa=debt, debt=1, create_user=request.user)

        return redirect('debt')
    else:
        context = {
            'debtors': Lead.objects.filter(debt=0, created_user__company=request.user.company),
            'method': 'get',
        }
        return render(request, 'adddebtor2.html', context)


def getbuyurtma(request):
    id = request.GET.get('id')
    book = Books.objects.get(id=id)
    t = {
        'id':book.id,
        'phone':book.client.phone,
        'name':book.client.name,
        'surname':book.client.surname,
        'filial':book.filial.name,
        'meals':book.meals,
        'ordertime':book.ordertime
    }

    return JsonResponse(t)

def getbuyurtma1(request):
    id = request.GET.get('id')
    book = Books.objects.get(id=id)
    t = {
        'id':book.id,
        'phone':book.client.phone,
        'name':book.client.name,
        'surname':book.client.surname,
        'filial':book.filial.name,
        'people':book.people,
        'meals':book.meals,
        'room':book.room.name,
        'ordertime':book.ordertime
    }

    return JsonResponse(t)

def editbuyurtma(request):
    r = request.POST
    buyurtma = r.get('buyurtma')
    sana = r.get('sana')
    modalbookid = r.get('modalbookid')
    book = Books.objects.get(id=modalbookid)
    book.meals = buyurtma
    book.ordertime = sana
    book.save()
    sn = sana.split('T')
    fil = book.filial
    client = book.client
    ids = fil.chat_id.split(' ')
    for id in ids:
        text = 'Olib ketishga: \n\nMijoz: ' + client.name + '\nTelefon: ' + client.phone + '\nBuyurtma: ' + buyurtma + '\nSana: ' + \
               sn[0] + ' ' + sn[1]
        url = 'https://api.telegram.org/bot' + fil.bot_token + '/sendMessage?chat_id='
        requests.get(url + id + '&text=' + text)
    messages.success(request, 'Buyurtma o`zgartirildi')
    return redirect('buyurtmaolish')

def editbuyurtma1(request):
    r = request.POST
    buyurtma = r.get('buyurtma1')
    phone = r.get('phone')
    sanafrom = r.get('sanafrom')
    sanato = r.get('sanato')
    modalbookid1 = r.get('modalbookid1')
    filial = r.get('filial')
    xona = r.get('xona')
    people = r.get('people')
    book = Books.objects.get(id=modalbookid1)
    book.meals = buyurtma
    book.date_from = sanafrom
    book.date_to = sanato
    book.filial_id = filial
    book.room_id = xona
    book.phone=phone
    book.people = people
    book.save()
    sn = sanafrom.split('T')
    st = sanato.split('T')
    fil = book.filial
    client = book.client
    ids = fil.chat_id.split(' ')
    for id in ids:
        text = '#TAXRIRLANDI  \n\n Olib ketishga: \n\nMijoz: ' + client.name + '\nTelefon: ' + client.phone + '\nBuyurtma: ' + str(buyurtma) + '\nSana: ...dan ' + \
           sn[0] + ' ' + sn[1]+ '\nSana:..gacha ' +st[0] + ' ' + st[1]
        url = 'https://api.telegram.org/bot' + fil.bot_token + '/sendMessage?chat_id='
        requests.get(url + id + '&text=' + text)
    messages.success(request, 'Buyurtma o`zgartirildi')
    return redirect('buyurtmaolish')

def addmaxsulot(request):
    user = request.user
    if request.method == "POST":
        nomi = request.POST.get('nomi')
        narxi = request.POST.get('narxi')
        izoh = request.POST.get('izoh')

        Maxsulotlar.objects.create(name=nomi, price=narxi, bor_yoqligi=1, izoh=izoh, filial=user.filial)
        messages.success(request, 'Maxsulot muvoffaqiyatli qoshildi')
        return redirect("addmaxsulot")
    return render(request, 'addmaxsulot.html')

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result
