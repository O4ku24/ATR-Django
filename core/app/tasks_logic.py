from .models import Task

def task_add(title:str, executioner:str, direct:str, description:str, endTime:str) -> None:
    Task.objects.create(title=title, 
                        executioner=executioner, 
                        direct=direct, 
                        description=description, 
                        endTime=endTime, 
                        )

def task_del():
    pass

def task_edit():
    pass

def task_done():
    pass

def tasks_list() -> dict[str]:
    data = {'ordering':{},'names':{}}
    orders = Task.objects.values()
        
    for order in orders:          
        data['ordering'][order['id']] = {
             'status':order['status'],
             'id':order['id'],
             'title':order['title'],
             'description':order['description'],
             'executioner':order['executioner'],
             'direct':order['direct'],
             'startTime':order['startTime'],
             'endTime':order['endTime']
             }
    return data