from django.shortcuts import render, redirect


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def login(request):
    return render(request, 'core/login.html')


def contact(request):
    return render(request, 'core/contacts.html')


def page1(request):
    return render(request, 'core/type01.html')


def page2(request):
    return render(request, 'core/type02.html')


def page3(request):
    return render(request, 'core/type03.html')

