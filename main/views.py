import json
from datetime import datetime

import openpyxl
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from buyurtma.models import *
from goal.models import Goal
from .models import *


def ChartLead(request):
    zeros = []
    fours = []
    fives = []
    if request.user.is_director:
        for i in range(1, 13):
            date = datetime.today()
            year = date.year
            if i == 12:
                month2 = 1
                year2 = year + 1
            else:
                month2 = i + 1
                year2 = year
            gte = str(year) + '-' + str(i) + '-01 00:00:00'
            lte = str(year2) + '-' + str(month2) + '-01 00:00:00'

            zero = Lead.objects.filter(created_user__company=request.user.company, date__gte=gte, date__lt=lte,
                                       status__lte=3).count()
            four = Lead.objects.filter(created_user__company=request.user.company, finishedDate__gte=gte,
                                       finishedDate__lt=lte, status=4).count()
            five = Lead.objects.filter(created_user__company=request.user.company, finishedDate__gte=gte,
                                       finishedDate__lt=lte, status=5).count()
            zeros.append(zero)
            fours.append(four)
            fives.append(five)
    else:
        for i in range(1, 13):
            date = datetime.today()
            year = date.year
            if i == 12:
                month2 = 1
                year2 = year + 1
            else:
                month2 = i + 1
                year2 = year
            gte = str(year) + '-' + str(i) + '-01 00:00:00'
            lte = str(year2) + '-' + str(month2) + '-01 00:00:00'

            zero = Lead.objects.filter(created_user=request.user, date__gte=gte, date__lt=lte,
                                       status__lte=3).count()
            four = Lead.objects.filter(created_user=request.user, finishedDate__gte=gte, finishedDate__lt=lte,
                                       status=4).count()
            five = Lead.objects.filter(created_user=request.user, finishedDate__gte=gte, finishedDate__lt=lte,
                                       status=5).count()
            zeros.append(zero)
            fours.append(four)
            fives.append(five)
    dt = {
        'zeros': zeros,
        'fours': fours,
        'fives': fives,
    }
    return JsonResponse(dt)


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Home, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['home'] = 'active'
        context['users'] = Account.objects.filter(company=self.request.user.company)
        context['lead'] = Lead.objects.filter(status=0, created_user__company=self.request.user.company).count(),
        context['aktiv'] = Lead.objects.filter(status__gte=5, created_user__company=self.request.user.company).count(),
        debt = Lead.objects.filter(created_user__company=self.request.user.company, debt__gt=0)
        context['debtor'] = debt.count()
        if debt.aggregate(Sum('debt'))['debt__sum'] is None:
            context['debtor_sum'] = 0
        else:
            context['debtor_sum'] = debt.aggregate(Sum('debt'))['debt__sum']
        mijoz = Lead.objects.filter(created_user__company=self.request.user.company)
        context['lead'] = mijoz.filter(status__gte=0, status__lte=3).count()
        context['lead0'] = mijoz.filter(status=4).count()
        context['lead1'] = mijoz.filter(status=5).count()
        if self.request.user.is_director:
            accounts = Account.objects.filter(company=self.request.user.company)
            list = []
            for a in accounts:
                lc = Lead.objects.filter(created_user=a).count()
                try:
                    goal = Goal.objects.get(user=a, oy=datetime.today().month, yil=datetime.today().year)
                    t = {
                        'name': a.first_name,
                        'surname': a.last_name,
                        'foiz': int((lc / goal.mijoz_soni) * 100)
                    }
                except:
                    t = {
                        'name': a.first_name,
                        'surname': a.last_name,
                        'foiz': 0
                    }
                list.append(t)
            context['acc'] = list
        elif self.request.user.is_callcenter:
            return HttpResponseRedirect('/buyurtma/')
        else:
            lc = Lead.objects.filter(created_user=self.request.user).count()
            try:
                goal = Goal.objects.get(user=self.request.user, oy=datetime.today().month, yil=datetime.today().year)
                t = {
                    'name': self.request.user.first_name,
                    'surname': self.request.user.last_name,
                    'foiz': int((lc / goal.mijoz_soni) * 100)
                }
            except:
                t = {
                    'name': self.request.user.first_name,
                    'surname': self.request.user.last_name,
                    'foiz': 0
                }
            context['a'] = t
        return context


class Table(LoginRequiredMixin, TemplateView):
    template_name = 'table.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Table, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Table, self).get_context_data(**kwargs)
        context['table'] = 'active'

        return context


class Chart(LoginRequiredMixin, TemplateView):
    template_name = 'chart.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Chart, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Chart, self).get_context_data(**kwargs)
        context['chart'] = 'active'

        return context


class CalenApp(LoginRequiredMixin, TemplateView):
    template_name = 'apps-calendar.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(CalenApp, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CalenApp, self).get_context_data(**kwargs)
        context['appcalendar'] = 'active'
        context['users'] = Account.objects.filter(is_director=True)

        return context

class BookHistory(LoginRequiredMixin, TemplateView):
    template_name = 'bookhistory.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(BookHistory, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(BookHistory, self).get_context_data(**kwargs)
        context['bookhistory'] = 'active'
        today = datetime.today()
        sana0 = datetime(today.year, today.month, today.day)
        context['book'] = 'active'
        context['books'] = Books.objects.filter(date__gte=sana0)

        return context

class Roomlar(LoginRequiredMixin, TemplateView):
    template_name = 'roomlar.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Roomlar, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Roomlar, self).get_context_data(**kwargs)
        context['rooms'] = 'active'
        context['filial'] = Filial.objects.all()
        context['rooms0'] = Rooms.objects.filter(status=0)
        context['rooms1'] = Rooms.objects.filter(status=1)

        return context


class ClientSotuv(LoginRequiredMixin, TemplateView):
    template_name = 'clientsotuv.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(ClientSotuv, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ClientSotuv, self).get_context_data(**kwargs)
        context['clientsotuv'] = 'active'
        context['clients'] = Books.objects.values('client__name', 'client__surname', 'client__phone', 'client__birthday').annotate(count=Count('id'))
        # b = Books.objects.values('client__name', 'client__surname', 'client__phone').annotate(count=Count('id'))

        return context

def GetCalendar(request):
    if request.user.is_director:
        calens = Calendar.objects.filter(user=request.user)
    else:
        calens = Calendar.objects.filter(created_user=request.user)
    c = []
    for i in calens:
        j = {
            'id': i.id,
            'color': i.color,
            'event': i.event,
            'date': i.date
        }
        c.append(j)
    dt = {
        "calendars": c,
    }
    return JsonResponse(dt)


def AddEvent(request):
    user = request.user
    if request.method == "POST":
        r = request.POST
        event = r['event']
        date = r['date']
        color = r['color']
        Calendar.objects.create(event=event, date=date, color=color, created_user=user)
    return redirect('calendar1')


class Form(LoginRequiredMixin, TemplateView):
    template_name = 'form.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Form, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Form, self).get_context_data(**kwargs)
        context['form'] = 'active'

        return context


class Ill(LoginRequiredMixin, TemplateView):
    template_name = 'ill.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Ill, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Ill, self).get_context_data(**kwargs)
        context['ill'] = 'active'

        return context


class Form1(LoginRequiredMixin, TemplateView):
    template_name = 'form1.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Form1, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Form1, self).get_context_data(**kwargs)
        context['form1'] = 'active'

        return context


class Etiroz(LoginRequiredMixin, TemplateView):
    template_name = 'etiroz.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Etiroz, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Etiroz, self).get_context_data(**kwargs)
        context['etiroz'] = 'active'
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


class Target(LoginRequiredMixin, TemplateView):
    template_name = 'target.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Target, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Target, self).get_context_data(**kwargs)
        context['target'] = 'active'
        if self.request.user.is_director:
            context['lead'] = Lead.objects.filter(status__gte=1, status__lte=4,
                                                  created_user__company=self.request.user.company)
            context['mijoz'] = Lead.objects.filter(status=5, created_user__company=self.request.user.company)
            context['lead0'] = Lead.objects.filter(status=0, created_user__company=self.request.user.company)
            context['promouter'] = Lead.objects.filter(status=6, created_user__company=self.request.user.company)
            context['lead_count'] = Lead.objects.filter(status__gte=1, status__lte=4,
                                                        created_user__company=self.request.user.company).count()
            context['mijoz_count'] = Lead.objects.filter(status=5,
                                                         created_user__company=self.request.user.company).count()
            context['lead0_count'] = Lead.objects.filter(status=0,
                                                         created_user__company=self.request.user.company).count()
            context['promouter_count'] = Lead.objects.filter(status=6,
                                                             created_user__company=self.request.user.company).count()
        else:
            context['lead'] = Lead.objects.filter(
                status__gte=1, status__lte=4, created_user=self.request.user)
            context['mijoz'] = Lead.objects.filter(status=5, created_user=self.request.user)
            context['lead0'] = Lead.objects.filter(status=0, created_user=self.request.user)
            context['promouter'] = Lead.objects.filter(status=6, created_user=self.request.user)
            context['lead_count'] = Lead.objects.filter(status__gte=1, status__lte=4,
                                                        created_user=self.request.user).count()
            context['mijoz_count'] = Lead.objects.filter(status=5, created_user=self.request.user).count()
            context['lead0_count'] = Lead.objects.filter(status=0, created_user=self.request.user).count()
            context['promouter_count'] = Lead.objects.filter(status=6,
                                                             created_user=self.request.user).count()

        return context


class Clients(LoginRequiredMixin, TemplateView):
    template_name = 'clients.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

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


class Setting(LoginRequiredMixin, TemplateView):
    template_name = 'setting.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Setting, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Setting, self).get_context_data(**kwargs)
        context['setting'] = 'active'
        context['token'] = self.request.user.company.tg_token
        context['smstoken'] = self.request.user.company.sms_token
        context['users'] = Account.objects.filter(company=self.request.user.company)
        return context


@login_required
def importLead(request):
    if request.method == 'GET':
        return render(request, 'importLead.html')
    else:
        try:
            excel_file = request.FILES['leads']
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb.active
            count = 0
            user = request.user

            for row in worksheet.iter_rows():
                if count == 0:
                    count += 1
                else:
                    try:

                        name = row[0].value
                        surname = row[1].value
                        price = int(1)
                        company = row[3].value
                        companyAddress = row[4].value
                        phone = str(998)+str(row[5].value)
                        lead = Lead.objects.create(
                            name=name,
                            status=5,
                            surname=surname,
                            price=1,
                            company=company,
                            companyAddress=companyAddress,
                            phone=phone,
                            created_user=user
                        )
                        LeadAction.objects.create(lead=lead, changer=user)
                    except Exception as er:
                        print(f'{er}')
            messages.success(request, "Mijozlar muvaffaqqiyatli yuklandi")
        except:
            messages.error(request, "Yuklashda xatolik")
        return redirect('clients')


class Debt(LoginRequiredMixin, TemplateView):
    template_name = 'debt.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Debt, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Debt, self).get_context_data(**kwargs)
        context['debt'] = 'active'
        context['debtors'] = Lead.objects.filter(debt__gt=0, created_user__company=self.request.user.company)

        return context


class Sms(LoginRequiredMixin, TemplateView):
    template_name = 'sms.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Sms, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Sms, self).get_context_data(**kwargs)
        context['lead_count'] = Lead.objects.filter(created_user__company=self.request.user.company).count()
        context['sms'] = 'active'
        context['illness'] = CategoryProduct.objects.all()
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


def SmsGateway(request):
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
    return redirect('sms')


class Hodim(LoginRequiredMixin, TemplateView):
    template_name = 'hodim.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.request.user.is_callcenter:
            return redirect('/buyurtma/')
        elif not self.request.user.is_director:
            return redirect('/buyurtma/buyurtmaolish/')

        return super(Hodim, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Hodim, self).get_context_data(**kwargs)
        context['hodim'] = 'active'
        context['users'] = Account.objects.filter(company=self.request.user.company)

        return context


def DeleteHodim(request):
    h_id = request.GET.get('id')
    Account.objects.get(id=h_id).delete()

    return redirect('hodim')


def ObjectWrite(request):
    if request.method == "POST":
        obj = request.POST['objection']
        sol = request.POST['solution']

        ObjectionWrite.objects.create(objection=obj, solution=sol, create_user=request.user)
        if request.user.is_callcenter:
            return redirect('etirozcall')
        else:
            return redirect('etiroz')
    else:
        return redirect('etiroz')


def Obj(request):
    if request.method == "POST":
        obj = request.POST['objection']
        sol = request.POST['solution']

        Objections.objects.create(objection=obj, solution=sol, create_user=request.user)
        if request.user.is_callcenter:
            return redirect('etirozcall')
        else:
            return redirect('etiroz')
    else:
        return redirect('etiroz')


def CalenEdit(request):
    today = datetime.now()
    c = Calendar.objects.filter(date__gte=today).order_by('date')

    context = {
        'calens': c,
    }
    return render(request, 'calenedit.html', context)


def CalenEditForm(request):
    context = {}
    if request.method == "GET":
        pk = request.GET.get('id')
        c = Calendar.objects.get(id=pk)

        context = {
            'calen': c
        }

    return render(request, 'caleneditform.html', context)


def CalenDel(request):
    if request.method == "GET":
        pk = request.GET.get('id')
        Calendar.objects.get(id=pk).delete()
    return redirect('calenedit')


def Delete(request):
    if request.method == "GET":
        pk = request.GET.get('id')
        t = request.GET.get('t')
        if t == '1':
            o = Objections.objects.get(id=pk)
            o.delete()
        elif t == '2':
            o = ObjectionWrite.objects.get(id=pk)
            o.delete()
        if request.user.is_callcenter:
            return redirect('etirozcall')
        else:
            return redirect('etiroz')
    else:
        return redirect('etiroz')


def SaveEditCalen(request):
    if request.method == "POST":
        r = request.POST
        pk = r['id']
        event = r['event']
        date = r['date']
        color = r['color']

        c = Calendar.objects.get(id=pk)
        c.event = event
        c.color = color
        c.date = date
        c.save()

    return redirect('calenedit')


def AddHodim(request):
    if request.method == "POST":
        r = request.POST
        fam = r['fam']
        ism = r['ism']
        username = r['username']
        password = r['password']

        Account.objects.create(username=username, password=make_password(password), first_name=ism, last_name=fam,
                               company=request.user.company)
        return redirect('hodim')


def Edito(request):
    if request.method == "GET":
        pk = request.GET.get('id')
        t = request.GET.get('t')
        try:
            ck = Script.objects.first()
        except:
            ck = None
        if t == '1':
            o = Objections.objects.get(id=pk)
            context = {
                'objections': Objections.objects.filter(create_user__company=request.user.company),
                'objectionwrite': ObjectionWrite.objects.filter(create_user__company=request.user.company),
                'obj': o,
                'ckeditor': ck,
                't': 1
            }
            return render(request, 'etiroz.html', context)
        elif t == '2':
            o = ObjectionWrite.objects.get(id=pk)
            context = {
                'objections': Objections.objects.filter(create_user__company=request.user.company),
                'objectionwrite': ObjectionWrite.objects.filter(create_user__company=request.user.company),
                'obj': o,
                'ckeditor': ck,
                't': 2
            }
            return render(request, 'etiroz.html', context)
    else:
        return redirect('etiroz')


def Save(request):
    if request.method == "POST":
        o = request.POST['objection']
        s = request.POST['solution']
        id = request.POST['id']
        t = request.POST['t']
        if t == '1':
            obj = Objections.objects.get(id=id)
            obj.objection = o
            obj.solution = s
            obj.save()
        elif t == '2':
            obj = ObjectionWrite.objects.get(id=id)
            obj.objection = o
            obj.solution = s
            obj.save()

    if request.user.is_callcenter:
        return redirect('etirozcall')
    else:
        return redirect('etiroz')


def Ckeditor(request):
    if request.method == 'POST':
        ck = request.POST['editor1']
        try:
            s = Script.objects.filter(create_user__company=request.user.company).first()
            s.text = ck
            s.save()
        except:
            Script.objects.create(text=ck, create_user=request.user)
        if request.user.is_callcenter:
            return redirect('etirozcall')
        else:
            return redirect('etiroz')
    else:
        return redirect('etiroz')


def Edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        # step = request.GET.get('s')
        c = Lead.objects.get(id=id)
        # try:
        if c.step1 is None:
            step = 1
        elif c.step2 is None:
            step = 2
        elif c.step3 is None:
            step = 3
        elif c.step4 is None:
            step = 4
        else:
            step = 5
        try:
            user = {
                'id': c.id,
                'first_name': c.name,
                'last_name': c.surname,
                'birthday': c.birthday,
                'phone': c.phone,
                'region': c.district.region.name,
                'district': c.district.name,
                'degree': c.degr[c.degree - 1][1],
                'status': c.status_types[c.status][1],
                'abcxyz': c.abcxyz,
                'step1': c.step1,
                'step2': c.step2,
                'step3': c.step3,
                'step4': c.step4,
                'step5': c.step5,
                'note': c.note,
            }
        except:
            user = {
                'id': c.id,
                'first_name': c.name,
                'last_name': c.surname,
                'birthday': c.birthday,
                'phone': c.phone,
                'degree': c.degr[c.degree - 1][1],
                'status': c.status_types[c.status][1],
                'abcxyz': c.abcxyz,
                'step1': c.step1,
                'step2': c.step2,
                'step3': c.step3,
                'step4': c.step4,
                'step5': c.step5,
                'note': c.note,
            }
        context = {
            'userr': user,
            'step': step,
            'region': Region.objects.all(),
            'district': District.objects.all(),
            'notes': LeadAction.objects.filter(lead_id=id),
        }
        return render(request, 'edit.html', context)

    elif request.method == 'POST':
        id = int(request.POST['id'])
        u = Lead.objects.get(id=id)
        try:
            surname = request.POST['surname']
            u.surname = surname
        except:
            pass
        try:
            phone = request.POST['phone']
            u.phone = phone
        except:
            pass
        try:
            region = request.POST['region']
            u.region = region
        except:
            pass
        try:
            district = request.POST['district']
            u.district = district
        except:
            pass
        try:
            birthday = request.POST['birthday']
            u.birthday = birthday
        except:
            pass
        try:
            district = request.POST['district']
            u.district_id = district
        except:
            pass
        try:
            abc = request.POST['abc']
            u.abcxyz = abc
        except:
            pass
        try:
            notes = request.POST['notes']
            u.note = notes
        except:
            pass
        u.save()

        return redirect('target')


def AddUser(request):
    u = request.user
    if request.method == "POST":
        r = request.POST
        ism = r['ism']
        fam = r['fam']
        phone = r['tel']
        birthday = r['birth']
        dis = r['district']
        abc = r['abc']
        com = r['com']
        comadd = r['comadd']
        price = r['price']
        illness = r.getlist('ill')
        try:
            Lead.objects.get(phone=phone)
            messages.add_message(request, messages.ERROR, f"{ism} avval ro'yxatdan o'tgan")
            return redirect('adduser')
        except:
            u = Lead.objects.create(name=ism, surname=fam, phone=phone, birthday=birthday, abcxyz=abc,
                                    status=0, district_id=dis, created_user=u, price=price, companyAddress=comadd,
                                    company=com)
            # token, created = Token.objects.get_or_create(user=cs)
            for i in illness:
                ii = CategoryProduct.objects.get(id=i)
                u.categoryproduct.add(ii)
                u.save()
            messages.add_message(request, messages.SUCCESS, f"{phone} Qo'shildi")
        return redirect('target')
    else:
        context = {
            'ills': CategoryProduct.objects.all(),
            'region': Region.objects.all(),
            'district': District.objects.all()
        }

        return render(request, 'adduser.html', context)


def Up(request):
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        s = int(request.GET.get('s'))
        u = Lead.objects.get(id=id)
        u.status = s
        # u.date = datetime(2021, 2, 3, 0, 0, 0)
        u.date = datetime.now()
        u.save()
    return redirect('target')


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_director:
                return redirect('home')
            elif user.is_callcenter:
                return redirect('/buyurtma/buyurtmaolish/')
            else:
                return redirect('/buyurtma/')
        else:
            messages.error(request, 'Login yoki Parol noto`g`ri kiritildi!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Tizimdan chiqish muvaffaqiyatli yakunlandi!")
    return redirect('login')


def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response


def AddNotes(request):
    u = request.user
    if request.method == "POST":
        note = request.POST['note']
        id = request.POST['id']
        color = request.POST['color']

        LeadAction.objects.create(note=note, lead_id=id, color=color, changer=u)
        url = '/edit/?id=' + str(id)
        return redirect(url)


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

        return render(request, 'debthistory.html', context)


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
        url = '/debthistory/?id=' + u_id
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
        return render(request, 'adddebtor.html', context)


def EditSpin(request):
    if request.method == "POST":
        r = request.POST
        u_id = r['u_id']
        step = r['step']
        st = r['st']
        url = '/edit/?id=' + u_id
        user = Lead.objects.get(id=u_id)
        if st == '1':
            user.step1 = step
        elif st == '2':
            user.step2 = step
        elif st == '3':
            user.step3 = step
        elif st == '4':
            user.step4 = step
        elif st == '5':
            user.step5 = step
        user.save()
        return redirect(url)
    else:
        return redirect('target')


def PostEvent(request):
    data = json.loads(request.body)
    user = data['user']
    title = data['title']
    time = data['start']
    className = data['className']
    c = Calendar.objects.create(user_id=user, event=title, date=time, color=className, created_user=request.user)

    return JsonResponse({})


def DelEvent(request):
    id = request.GET.get('id')

    Calendar.objects.get(id=id).delete()

    return JsonResponse({})


def EditEvent(request):
    data = json.loads(request.body)
    id = data['id']
    user = data['user']
    title = data['title']
    time = data['start']
    className = data['className']

    c = Calendar.objects.get(id=id)
    c.user_id = user
    c.event = title
    c.date = time
    c.color = className
    c.save()

    return JsonResponse({})


def Bugunlik(request):
    uuu = int(request.GET.get('id'))
    sana = datetime.today()
    kun = sana.date()
    num_kun = datetime.toordinal(kun)
    sana2 = datetime.fromordinal(num_kun + 1)
    sana1 = datetime(kun.year, kun.month, kun.day)
    user = request.user
    company = user.company
    users = Account.objects.filter(company=company)
    # response_data = list(Lead.objects.filter(created_user__company=company, date__gte=sana1, date__lt=sana2)
    #     .values('created_user__first_name', 'created_user__last_name').annotate(
    #     total_count=Count(F('id')),
    #     total_price=Sum(F('price'))
    # ))
    us = []
    for i in users:
        count = Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                    created_user__company=company).count()
        summ = \
            Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                created_user__company=company).aggregate(
                Sum('price'))['price__sum']
        if summ:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': summ
            }
        else:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': 0
            }
        us.append(t)

    if user.is_director:
        if uuu == 0:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'users': us
            }
        else:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              created_user_id=uuu,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us
            }
    else:
        dt = {
            'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).count(),
            'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                          status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('finishedPrice'))['finishedPrice__sum'],

            'task0': Task.objects.filter(status=0, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task1': Task.objects.filter(status=1, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task2': Task.objects.filter(status=2, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task3': Task.objects.filter(status=3, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'zero0': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=0).count(),
            'zero0s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero1': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=1).count(),
            'zero1s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero2': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=2).count(),
            'zero2s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero3': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=3).count(),
            'zero3s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
        }
    return JsonResponse(dt)


def Haftalik(request):
    uuu = int(request.GET.get('id'))
    sana = datetime.today()
    kun = sana.date()
    num_kun = datetime.toordinal(kun)
    sana2 = datetime.fromordinal(num_kun + 1)
    sana1 = datetime.fromordinal(num_kun - 6)
    user = request.user
    company = user.company
    users = Account.objects.filter(company=company)
    us = []
    for i in users:
        count = Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                    created_user__company=company).count()
        summ = \
            Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                created_user__company=company).aggregate(
                Sum('price'))['price__sum']
        if summ:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': summ
            }
        else:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': 0
            }
        us.append(t)

    if user.is_director:
        if uuu == 0:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us

            }
        else:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              created_user_id=uuu,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us
            }
    else:
        dt = {
            'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).count(),
            'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                          status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('finishedPrice'))['finishedPrice__sum'],

            'task0': Task.objects.filter(status=0, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task1': Task.objects.filter(status=1, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task2': Task.objects.filter(status=2, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task3': Task.objects.filter(status=3, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'zero0': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                               oldStatus=0).count(),
            'zero0s': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                                oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero1': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                               oldStatus=1).count(),
            'zero1s': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                                oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero2': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                               oldStatus=2).count(),
            'zero2s': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                                oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero3': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                               oldStatus=3).count(),
            'zero3s': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                                oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
        }
    return JsonResponse(dt)


def Oylik(request):
    uuu = int(request.GET.get('id'))
    sana = datetime.today()
    kun = sana.date()
    num_kun = datetime.toordinal(kun)
    sana2 = datetime.fromordinal(num_kun + 1)
    sana1 = datetime.fromordinal(num_kun - 29)
    user = request.user
    company = user.company
    users = Account.objects.filter(company=company)
    us = []
    for i in users:
        count = Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                    created_user__company=company).count()
        summ = \
            Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                created_user__company=company).aggregate(
                Sum('price'))['price__sum']
        if summ:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': summ
            }
        else:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': 0
            }
        us.append(t)

    if user.is_director:
        if uuu == 0:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us

            }
        else:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              created_user_id=uuu,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us
            }
    else:
        dt = {
            'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).count(),
            'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                          status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('finishedPrice'))['finishedPrice__sum'],

            'task0': Task.objects.filter(status=0, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task1': Task.objects.filter(status=1, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task2': Task.objects.filter(status=2, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task3': Task.objects.filter(status=3, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'zero0': LeadAction.objects.filter(date__gte=sana1, changeruser=user, date__lt=sana2,
                                               newStatus=4, oldStatus=0).count(),
            'zero0s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero1': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=1).count(),
            'zero1s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero2': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=2).count(),
            'zero2s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero3': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=3).count(),
            'zero3s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
        }
    return JsonResponse(dt)


def Range(request):
    uuu = request.GET.get('id')
    date1 = request.GET.get('sana1')
    date2 = request.GET.get('sana2')
    dt1 = date1.split('/')
    dt2 = date2.split('/')
    sana1 = datetime(int(dt1[2]), int(dt1[0]), int(dt1[1]))
    sana2 = datetime(int(dt2[2]), int(dt2[0]), int(dt2[1]))
    user = request.user
    company = user.company
    users = Account.objects.filter(company=company)
    us = []
    for i in users:
        count = Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                    created_user__company=company).count()
        summ = \
            Lead.objects.filter(created_user=i, date__gte=sana1, date__lt=sana2,
                                created_user__company=company).aggregate(
                Sum('price'))['price__sum']
        if summ:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': summ
            }
        else:
            t = {
                'id': i.id,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'count': count,
                'summ': 0
            }
        us.append(t)

    if user.is_director:
        if uuu == 0:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer__company=company, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us

            }
        else:
            dt = {
                'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                           created_user_id=uuu,
                                           status_date__lt=sana2).count(),
                'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).count(),
                'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).count(),
                'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user__company=company,
                                            created_user_id=uuu,
                                            status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user__company=company,
                                              created_user_id=uuu,
                                              status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
                'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             status_date__lt=sana2).aggregate(Sum('finishedPrice'))[
                    'finishedPrice__sum'],

                'task0': Task.objects.filter(status=0, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task1': Task.objects.filter(status=1, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task2': Task.objects.filter(status=2, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'task3': Task.objects.filter(status=3, date__gte=sana1, created_user__company=company,
                                             created_user_id=uuu,
                                             date__lt=sana2).count(),
                'zero0': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=0).count(),
                'zero0s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero1': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=1).count(),
                'zero1s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero2': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=2).count(),
                'zero2s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
                'zero3': LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2,
                                                   newStatus=4, oldStatus=3).count(),
                'zero3s':
                    LeadAction.objects.filter(date__gte=sana1, changer_id=uuu, date__lt=sana2, newStatus=4,
                                              oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
                'users': us
            }
    else:
        dt = {
            'zero': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'one': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'two': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                       status_date__lt=sana2).count(),
            'three': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).count(),
            'four': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'five': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).count(),
            'zeros': Lead.objects.filter(status=0, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'ones': Lead.objects.filter(status=1, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'twos': Lead.objects.filter(status=2, status_date__gte=sana1, created_user=user,
                                        status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'threes': Lead.objects.filter(status=3, status_date__gte=sana1, created_user=user,
                                          status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fours': Lead.objects.filter(status=4, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('price'))['price__sum'],
            'fives': Lead.objects.filter(status=5, status_date__gte=sana1, created_user=user,
                                         status_date__lt=sana2).aggregate(Sum('finishedPrice'))['finishedPrice__sum'],

            'task0': Task.objects.filter(status=0, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task1': Task.objects.filter(status=1, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task2': Task.objects.filter(status=2, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'task3': Task.objects.filter(status=3, date__gte=sana1, created_user=user, date__lt=sana2).count(),
            'zero0': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=0).count(),
            'zero0s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=0).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero1': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=1).count(),
            'zero1s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=1).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero2': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=2).count(),
            'zero2s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=2).aggregate(Sum('lead__price'))['lead__price__sum'],
            'zero3': LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2,
                                               newStatus=4, oldStatus=3).count(),
            'zero3s':
                LeadAction.objects.filter(date__gte=sana1, changer=user, date__lt=sana2, newStatus=4,
                                          oldStatus=3).aggregate(Sum('lead__price'))['lead__price__sum'],
        }
    return JsonResponse(dt)


def addtoken(request):
    t = request.POST['token']
    a = Account.objects.get(company=request.user.company, is_director=True)
    a.company.tg_token = t
    a.save()
    return redirect('setting')


def addsms(request):
    t = request.POST['token']
    n = request.POST['nickname']
    c = request.POST['callback']
    a = Account.objects.get(company=request.user.company, is_director=True)
    a.company.sms_token = t
    a.company.sms_from = n
    a.company.sms_callback_url = c
    a.company.sms_activated = True
    a.save()
    return redirect('setting')


def EditUser(request):
    r = request.POST
    id = r['id']
    ism = r['ism']
    fam = r['fam']
    phone = r['phone']
    birthday = r['date']
    a = Lead.objects.get(id=id)
    a.ism = ism
    a.fam = fam
    a.phone = phone
    a.birthday = birthday
    a.save()
    url = '/edit/?id=' + str(id)
    return redirect(url)


def GetRegion(request):
    id = request.GET.get('id')
    dist = District.objects.filter(region_id=id)
    dis = []
    for d in dist:
        t = {
            'id': d.id,
            'name': d.name
        }
        dis.append(t)

    data = {
        'district': dis
    }
    return JsonResponse(data)


def GetHodim(request):
    pk = request.GET.get('id')
    us = Account.objects.get(id=pk)
    dis = {
        'id': us.id,
        'fam': us.last_name,
        'ism': us.first_name
    }

    data = {
        'user': dis
    }
    return JsonResponse(data)


def EditHodim(request):
    r = request.POST
    id = r['id']
    fam = r['fam']
    ism = r['ism']
    username = r['username']
    password = r['password']
    us = Account.objects.get(id=id)
    try:
        Account.objects.get(username=username)
        messages.error(request, 'Loginni o`zgartiring')
        return redirect('setting')
    except:
        us.username = username
    us.first_name = ism
    us.last_name = fam
    us.password = make_password(password)
    us.save()
    messages.success(request, 'Hodim taxrirlandi')
    return redirect('setting')
