import datetime
import uuid

from .models import *


def login(request):
    mac = hex(uuid.getnode())
    if not mac:
        return None
    try:
        trainer = Trainer.objects.get(mac=mac)
        print(f'Login from IP: {ip} at {datetime.datetime.now()}')
    except Trainer.DoesNotExist:
        trainer = Trainer(mac=mac)
        trainer.save()
        print('Creating new user!')
    return trainer
