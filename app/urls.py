from django.urls import path
from app.views import select_model_view, select_task_view, show_details_view

urlpatterns = [
    path('lookup/', select_model_view, name='select_model'),
    path('lookup/<car>/', select_task_view, name='select_task'),
    path('lookup/<car>/<task>/', show_details_view, name='repair_detail'),
]
