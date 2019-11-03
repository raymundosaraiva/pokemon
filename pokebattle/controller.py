import datetime

from .models import *


def login(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        trainer = Trainer.objects.get(ip=ip)
        print(f'Login from IP: {ip} at {datetime.datetime.now()}')
    except Trainer.DoesNotExist:
        trainer = Trainer(ip=ip)
        trainer.save()
        print('Creating new user!')
    return trainer
