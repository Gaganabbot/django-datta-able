from django.shortcuts import redirect, render
from datetime import datetime,timedelta
from django.utils.timezone import datetime 
# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import WorkForm
from .models import Work

def Work_Suggestions(work_queryset):
    today = datetime.today()
    suggestions=[]
    work_model=Work.objects.filter(created_date__year=today.year,
                        created_date__month=today.month,
                        created_date__day=today.day)

    count_tasks=complete_count=0
    for i in work_queryset:
        if i.status=="Complete":
            complete_count=complete_count+1
        count_tasks=count_tasks+1
        
    if complete_count>1 and count_tasks>2:
            suggestions=["You can achieve it, Try to complete more task today"]
            if complete_count>2 and count_tasks>5:
                suggestions=["Great Work! Now Take a Break."]
    if complete_count==0:
        suggestions=["Try to put in more efforts"]

    return suggestions


@login_required(login_url="/login/")
def WorkEfficiency(request):
    work_model=Work.objects.all()
    complete_count= count_tasks=0
    suggestions_value=Work_Suggestions(work_model)

    form = WorkForm()
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():            
            form.save()

    context = {'segment': 'index','form':form, 'work_model':work_model, 'suggestions':suggestions_value}

    html_template = loader.get_template('work.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def AddWork(request):
    work_model=Work.objects.all()
    form = WorkForm()
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():            
            form.save()

    context = {'segment': 'index','form':form, 'work_model':work_model}

    html_template = loader.get_template('addtask.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def UpdateWork(request,pk):
    work_model=Work.objects.get(id=pk)
    form = WorkForm(instance=work_model)
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():            
            form.save()

    context = {'segment': 'index','form':form, 'work_model':work_model}

    html_template = loader.get_template('updatetask.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def DeleteWork(request,pk):
    work_model=Work.objects.get(id=pk)
    work_model.delete()
    return redirect('/apps/work')

