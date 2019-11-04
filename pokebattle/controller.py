import datetime

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

from .models import *

USER_LOGIN = 'user_login'


def login(request):
    try:
        trainer_id = request.session[USER_LOGIN]
        trainer = Trainer.objects.get(id=trainer_id)
        print(f'Login from user: {trainer_id} at {datetime.datetime.now()}')
    except KeyError:
        print('Creating new user!')
        trainer = Trainer()
        trainer.save()
        request.session['user_login'] = trainer.id

    return {'trainer': trainer}


def remove_user(request):
    del request.session[USER_LOGIN]


@csrf_exempt
def change_nickname(request):
    trainer_id = request.session[USER_LOGIN]
    trainer = Trainer.objects.get(id=trainer_id)
    new_nickname = request.POST.get('nickname')
    if new_nickname:
        trainer.nickname = new_nickname
        trainer.save()
    return HttpResponse(new_nickname)

