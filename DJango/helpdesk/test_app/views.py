from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def fun_view_test(request):
    return HttpResponse("<H1> This is a function based view </H1>")


class Cls_view_Test(TemplateView):
    template_name = "test-1.html"

