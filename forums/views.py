from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'forums/main.html')


def base(request):
    return render(request, 'forums/detail.html')
