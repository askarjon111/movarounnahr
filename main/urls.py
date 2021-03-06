from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('table/', Table.as_view(), name='table'),
    path('chart/', Chart.as_view(), name='chart'),
    path('app-calendar/', CalenApp.as_view(), name='app-calendar'),
    path('bookhistory/', BookHistory.as_view(), name='bookhistory'),
    path('xonalar/', Roomlar.as_view(), name='roomlar'),
    path('clientsotuv/', ClientSotuv.as_view(), name='clientsotuv'),
    path('form/', Form.as_view(), name='form'),
    path('form1/', Form1.as_view(), name='form1'),
    path('setting/', Setting.as_view(), name='setting'),
    path('edit/', Edit, name='edit'),
    path('up/', Up, name='up'),
    path('target/', Target.as_view(), name='target'),
    path('clients/', Clients.as_view(), name='clientsd'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('smsgateway/', SmsGateway, name='smsgateway'),
    path('sms/', Sms.as_view(), name='sms'),
    path('getcalendar/', GetCalendar, name='getcalendar'),
    path('addevent/', AddEvent, name='addevent'),
    path('ill/', Ill.as_view(), name='ill'),
    path('etiroz/', Etiroz.as_view(), name='etiroz'),
    path('objectionwrite/', ObjectWrite, name='objectionwrite'),
    path('object/', Obj, name='object'),
    path('delete1/', Delete, name='delete1'),
    path('edito/', Edito, name='edito'),
    path('save/', Save, name='save'),
    path('ckeditor/', Ckeditor, name='ckeditor'),
    path('adduser/', AddUser, name='adduser'),
    path('debt/', Debt.as_view(), name='debtd'),
    path('hodim/', Hodim.as_view(), name='hodim'),
    path('calenedit/', CalenEdit, name='calenedit'),
    path('caleneditform/', CalenEditForm, name='caleneditform'),
    path('calendel/', CalenDel, name='calendel'),
    path('saveeditcalen/', SaveEditCalen, name='saveeditcalen'),
    path('addnotes/', AddNotes, name='addnotes'),
    path('debthistory/', DebtHistory, name='debthistory'),
    path('adddebt/', AddDebt, name='adddebt'),
    path('adddebtor/', AddDebtor, name='adddebtor'),
    path('editspin/', EditSpin, name='editspin'),
    path('postevent/', PostEvent, name='postevent'),
    path('delevent/', DelEvent, name='delevent'),
    path('editevent/', EditEvent, name='editevent'),
    path('bugunlik/', Bugunlik, name='bugunlik'),
    path('haftalik/', Haftalik, name='haftalik'),
    path('oylik/', Oylik, name='oylik'),
    path('range/', Range, name='range'),
    path('addhodim/', AddHodim, name='addhodim'),
    path('deletehodim/', DeleteHodim, name='deletehodim'),
    path('importLead/', importLead, name='importLead'),
    path('addtoken/', addtoken, name='addtoken'),
    path('addsms/', addsms, name='addsms'),
    path('chartlead/', ChartLead, name='chartlead'),
    path('edituser/', EditUser, name='edituser'),
    path('edithodim/', EditHodim, name='edithodim'),
    path('getregion/', GetRegion, name='getregion'),
    path('gethodim/', GetHodim, name='gethodim'),
]
