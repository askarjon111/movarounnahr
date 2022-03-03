from django.urls import path

from .views import Board, create_lead, change_lead_status, lead_finished, lead_losed, edit_lead, get_lead_count, \
    create_lead_by_tg, telegram_bot_get_company, telegram_bot_add_phone, telegram_bot_add_company, \
    telegram_bot_add_company_address, telegram_bot_add_name

urlpatterns = [
    path("", Board.as_view(), name="board"),
    path("create_lead/", create_lead),
    path("change_lead_status/", change_lead_status),
    path("lead_finished/", lead_finished),
    path("lead_losed/", lead_losed),
    path("edit_lead/", edit_lead),
    path("create_lead_by_tg/", create_lead_by_tg),
    path("telegram_bot_get_company/", telegram_bot_get_company),
    path("telegram_bot_add_name/", telegram_bot_add_name),
    path("telegram_bot_add_phone/", telegram_bot_add_phone),
    path("telegram_bot_add_company/", telegram_bot_add_company),
    path("telegram_bot_add_company_address/", telegram_bot_add_company_address),
    path("get_lead_count/", get_lead_count, name='get_lead_count')
]
