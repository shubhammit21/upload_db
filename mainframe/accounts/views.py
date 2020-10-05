from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from tablib import Dataset
from .models import Person
from django.contrib import messages
from .resources import PersonResource
from subprocess import run,PIPE
import sys
#from .import script


def home(request):
    return render(request, 'index.html')

@login_required
def upload(request):
    if request.method == 'POST':
        managers_resource = PersonResource()
        dataset = Dataset()
        BOB_Resource = request.FILES['myfile']

        if not BOB_Resource.name.endswith('xlsx'):
            messages.info(request,'worng format')
        else:
            messages.info(request,'File upload successful')
        imported_data = dataset.load(BOB_Resource.read(), format='xlsx')

        for data in imported_data:
            print(data[1])
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
                data[21],
                data[22]

            )
            value.save()
    return render(request, 'mainframe.html')

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def export_csv(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response

def export_json(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response


def external(request):
    out = run([sys.executable,'D://Django_project//mainframe//script.py'],shell=False,stdout=PIPE)
    if not out:
        messages.info(request, 'unsuccessfull')
    else:
        messages.info(request, 'json to excel Executed successfully')
    return render(request, 'mainframe.html')
   # response = HttpResponse(content_type='application/excel')# response['Content-Disposition'] = 'attachment; filename="output.xlsx"'#   response = HttpResponse(request,{'data1':out.stdout})

def external_excel(request):
    outs = run([sys.executable,'D://Django_project//mainframe//code.py'],shell=False,stdout=PIPE)
    if not outs:
        messages.info(request, 'unsuccessfull')
    else:
        messages.info(request, 'Excel to Nested json Executed successfully')
        print("data2")
    return render(request, 'mainframe.html',{'data2':outs.stdout})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})
