import json
from datetime import datetime, timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Account, Company
from board.models import Lead, LeadAction, Task, Telegram_user
from board.serializers import LeadSerializer, TaskSerializer, CompanySerializer, Telegram_userSerializer


# Telegram bot uchun boshlanishi <<<<<<<<<


@api_view(['GET'])
def telegram_bot_get_company(request):
    try:
        token = request.GET.get('token')
        chat_id = int(request.GET.get('chat_id'))
        company = Company.objects.filter(tg_token=token).first()
        if Telegram_user.objects.filter(chat_id=chat_id, token=token).count() == 0:
            userr = Telegram_user.objects.create(
                chat_id=chat_id,
                token=token
            )
            return Response({
                "company": CompanySerializer(company).data,
                "user": Telegram_userSerializer(userr).data
            })
        else:
            return Response({
                "company": CompanySerializer(company).data,
                "user": Telegram_userSerializer(Telegram_user.objects.filter(chat_id=chat_id).first()).data
            })
    except:
        return Response({"message": "Error"}, 404)


@api_view(['GET'])
def telegram_bot_add_phone(request):
    try:
        phone = request.GET.get('phone')
        token = request.GET.get('token')
        chat_id = int(request.GET.get('chat_id'))
        user = Telegram_user.objects.filter(chat_id=chat_id, token=token).first()
        user.step = 2
        user.phone = phone
        user.save()
        return Response({
            "user": Telegram_userSerializer(user).data
        })
    except:
        return Response({"message": "Error"}, 404)


@api_view(['GET'])
def telegram_bot_add_name(request):
    try:
        name = request.GET.get('name')
        token = request.GET.get('token')
        chat_id = int(request.GET.get('chat_id'))
        user = Telegram_user.objects.filter(chat_id=chat_id, token=token).first()
        user.step = 3
        user.name = name
        user.save()
        return Response({
            "user": Telegram_userSerializer(user).data
        })
    except:
        return Response({"message": "Error"}, 404)


@api_view(['GET'])
def telegram_bot_add_company(request):
    try:
        company = request.GET.get('company')
        token = request.GET.get('token')
        chat_id = int(request.GET.get('chat_id'))
        user = Telegram_user.objects.filter(chat_id=chat_id, token=token).first()
        user.step = 4
        user.company = company
        user.save()
        return Response({
            "user": Telegram_userSerializer(user).data
        })
    except:
        return Response({"message": "Error"}, 404)


@api_view(['GET'])
def telegram_bot_add_company_address(request):
    try:
        companyadd = request.GET.get('companyaddress')
        token = request.GET.get('token')
        chat_id = int(request.GET.get('chat_id'))
        user = Telegram_user.objects.filter(chat_id=chat_id, token=token).first()
        user.step = 5
        user.companyAddress = companyadd
        user.save()
        return Response({
            "user": Telegram_userSerializer(user).data
        })
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def create_lead_by_tg(request):
    try:
        data = request.data
        name = data['name']
        company = data['company']
        address = data['address']
        phone = data['phone']
        tg_token = data['token']
        phone = str(phone).replace('+', '')
        tg_chatid = int(data['tg_chatid'])
        if Lead.objects.filter(tg_chatid=tg_chatid, created_user__company__tg_token=tg_token).count() == 0:
            companyCOm = Company.objects.filter(tg_token=tg_token).first()
            created_user = Account.objects.filter(company=companyCOm, is_director=True).first()
            lead = Lead.objects.create(
                name=name,
                company=company,
                phone=phone,
                companyAddress=address,
                created_user=created_user,
                joinBy=1,
                tg_chatid=tg_chatid
            )
            LeadAction.objects.create(lead=lead, changer=created_user)
            return Response({
                "user": LeadSerializer(lead).data
            })
        else:
            return Response({"message": "Error"}, 501)

    except:
        return Response({"message": "Error"}, 404)


# Telegram bot uchun tugashi >>>>>>>>


@api_view(['POST'])
def create_lead(request):
    try:
        data = request.data
        name = data['name']
        price = int(data['price'])
        company = data['company']
        address = data['address']
        user = int(data['user'])
        lead = Lead.objects.create(name=name, price=price, company=company,
                                   companyAddress=address, created_user_id=user)
        LeadAction.objects.create(lead=lead, changer_id=user)

        return Response(LeadSerializer(lead).data)
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def edit_lead(request):
    try:
        data = request.data
        leadId = int(data['lead'])
        name = data['name']
        price = int(data['price'])
        company = data['company']
        address = data['address']
        user = int(data['user'])

        lead = Lead.objects.get(id=leadId)
        lead.name = name
        lead.price = price
        lead.company = company
        lead.companyAddress = address
        LeadAction.objects.create(lead=lead, changer_id=user, status=1)
        lead.save()

        return Response(LeadSerializer(lead).data)
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def change_lead_status(request):
    try:
        data = request.data
        izoh = data['izoh']
        leadID = int(data['lead'])
        user = int(data['user'])
        status = int(data['status'])
        lead = Lead.objects.get(id=leadID)
        LeadAction.objects.create(lead=lead, changer_id=user, note=izoh, oldStatus=lead.status,
                                  newStatus=status, status=2)
        lead.status = status
        lead.status_date = datetime.now()
        lead.save()
        return Response(LeadSerializer(lead).data)
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def lead_finished(request):
    try:
        data = request.data
        price = int(data['price'])
        leadID = int(data['lead'])
        user = int(data['user'])
        lead = Lead.objects.get(id=leadID)
        LeadAction.objects.create(lead=lead, changer_id=user, oldStatus=lead.status, newStatus=5, status=2)
        lead.status = 5
        lead.finishedPrice = price
        lead.finishedDate = datetime.now()
        lead.save()
        return Response(LeadSerializer(lead).data)
    except:
        return Response({"message": "Error"}, 404)


@api_view(['POST'])
def lead_losed(request):
    try:
        data = request.data
        izoh = data['izoh']
        leadID = int(data['lead'])
        user = int(data['user'])
        lead = Lead.objects.get(id=leadID)
        LeadAction.objects.create(lead=lead, changer_id=user, note=izoh, oldStatus=lead.status, newStatus=4, status=2)
        lead.status = 4
        lead.save()
        return Response(LeadSerializer(lead).data)
    except:
        return Response({"message": "Error"}, 404)


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


@api_view(['POST'])
def get_lead_count(request):
    try:
        data = request.data
        status = list(json.loads(data['status']))
        user = int(data['user'])
        User = Account.objects.get(id=user)
        LeadsCount = Lead.objects.filter(status__in=status, created_user__company=User.company).count()
        return Response({"count": LeadsCount})
    except:
        return Response({"message": "Error"}, 404)


class Board(LoginRequiredMixin, TemplateView):
    template_name = 'Board.html'

    def get_context_data(self, *args, **kwargs):
        super(Board, self).get_context_data(**kwargs)
        leads = Lead.objects.filter(status__lt=4, created_user=self.request.user)
        group1_leads = leads.filter(status=0)
        group2_leads = leads.filter(status=1)
        group3_leads = leads.filter(status=2)
        group4_leads = leads.filter(status=3)
        all_lead = []
        for i in leads:
            all_lead.append(
                {"id": i.id,
                 "name": i.name,
                 "date": i.date.strftime("%Y-%m-%d, %H:%M"),
                 "price": i.price,
                 "company": i.company,
                 "address": i.companyAddress
                 }
            )

        context = {
            "Board": "active",
            "group1_leads": group1_leads,
            "group2_leads": group2_leads,
            "group3_leads": group3_leads,
            "group4_leads": group4_leads,
            "all_leads": json.dumps(all_lead)
        }
        return context


class TaskClass(LoginRequiredMixin, TemplateView):
    template_name = 'task.html'

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
