from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, "func_template.html")


class Index(TemplateView):
    template_name = "class_template.html"
