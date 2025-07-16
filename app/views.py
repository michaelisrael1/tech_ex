import json
import os
from django.shortcuts import render

# Load JSON once
json_path = os.path.join(os.path.dirname(__file__), 'repair_data.json')
with open(json_path, 'r') as f:
    REPAIR_DATA = json.load(f)

def select_model_view(request):
    models = list(REPAIR_DATA.keys())
    return render(request, 'select_model.html', {'models': models})

def select_task_view(request, car):
    tasks = REPAIR_DATA.get(car)
    if not tasks:
        return render(request, 'error.html', {'error': 'Car not found'})
    return render(request, 'select_task.html', {'car': car, 'tasks': list(tasks.keys())})

def show_details_view(request, car, task):
    try:
        repair = REPAIR_DATA[car][task]
        return render(request, 'repair_detail.html', {
            'car': car,
            'task': task,
            'tools': repair.get('tools', []),
            'parts': repair.get('parts', []),
            'instructions': repair.get('instructions', [])
        })
    except KeyError:
        return render(request, 'error.html', {'error': 'Repair task not found'})
