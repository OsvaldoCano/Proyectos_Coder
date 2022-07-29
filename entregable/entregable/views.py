from django.http import HttpResponse
from django.shortcuts import render
def saludo(request):
    return HttpResponse('Hola desde colombia')

def primer_template(request):
    context = {
    'name' : 'Osvaldo',
    'last_name':'Cano'
    }
    return render(request, 'template_1.html',context={})