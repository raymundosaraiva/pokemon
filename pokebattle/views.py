from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'pokebattle/base.html', context)
