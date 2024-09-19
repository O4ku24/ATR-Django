from django.shortcuts import render
from .tasks_logic import tasks_list, task_add
from .models import Users, Task

def start(request):
    return render(request=request, template_name='app/home.html')

def cash(request):
    return render(request=request, template_name='app/cash.html')

def tasks_add_render(request):
    if request.method == 'GET':
        data = {'ordering':{},'names':{}}
        namesData = Users.objects.values()
        for name in namesData:
            data['names'][name['name']] = {
                'name':name['name']
            }
        return render(request=request, template_name='app/ordering.html', context=data)
    
    if request.method == 'POST':
        
        title = request.POST.get('title')
        executioner = request.POST.get('executioner')
        direct = request.POST.get('direct')
        description = request.POST.get('descreption')
        endTime = request.POST.get('endTime')

        task_add(title=title, 
                 executioner=executioner,
                 direct=direct,
                 description=description,
                 endTime=endTime)
        
        return render(request=request, template_name='app/ordering.html')
    
def tasks(request):
    if request.method == 'GET':       
        return render(request=request, template_name='app/tasks.html', context=tasks_list())
    
    if request.method == 'PUT':
        pass
    
    if request.mrethod == 'DELETE':
        pass
