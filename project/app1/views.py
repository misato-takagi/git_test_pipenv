from django.shortcuts import render
from django.views.generic import DeleteView
# Create your views here.

class DeleteHosView(DeleteView):
    template_name: str = 'delete.html'
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name: str = 'index.html'
