from django.urls import path
from . import views

app_name = 'analyzer'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload'),
    path('result/<uuid:analysis_id>/', views.view_result, name='result'),
]