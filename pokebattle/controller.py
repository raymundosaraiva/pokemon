import datetime

from .models import *


def login(request):
    ip = request.META.get('HTTP_X_REAL_IP')
    try:
        trainer = Trainer.objects.get(ip=ip)
        print(f'Login from IP: {ip} at {datetime.datetime.now()}')
    except Trainer.DoesNotExist:
        trainer = Trainer(ip=ip)
        trainer.save()
        print('Creating new user!')
    return trainer
