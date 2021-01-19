from django.urls import path
from list import views


app_name = 'list'

urlpatterns = [
    path('create/',views.create_task_view,name='create'),
    path('delete/<id>',views.delete_task_view,name='delete')
]