from .models import Books
from datetime import datetime

def check_book():
    today = datetime.today().strftime('%Y-%m-%d %H:%M')
    t = today.split(' ')
    t1 = t[0].split('-')
    t2 = t[1].split(':')
    today = datetime(int(t1[0]), int(t1[1]), int(t1[2]), int(t2[0]), int(t2[1]))
    bs = Books.objects.filter(ordertype=0, status=0)
    for b in bs:
        exp = b.ordertime.strftime('%Y-%m-%d %H:%M')
        tt = exp.split(' ')
        tt1 = tt[0].split('-')
        tt2 = tt[1].split(':')
        exp = datetime(int(tt1[0]), int(tt1[1]), int(tt1[2]), int(tt2[0]), int(tt2[1]))
        if exp < today:
            b.room.status = 1
            b.room.save()