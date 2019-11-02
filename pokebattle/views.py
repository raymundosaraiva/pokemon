from django.shortcuts import render

from .controller import *


def index(request):
    user = login(request)
    if user:
        context = {'user': user}
        return render(request, 'pokebattle/base.html', context)
    else:
        return render(request, 'pokebattle/404.html')

