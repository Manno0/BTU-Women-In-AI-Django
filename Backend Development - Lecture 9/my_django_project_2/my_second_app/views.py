from django.http import HttpResponse
from django.views import View


def home(request):
    return HttpResponse("Welcome to the Home Page!")


class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")

from django.shortcuts import render

# Create your views here.
