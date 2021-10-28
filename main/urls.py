from django.urls import path
from .import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test, name='test'),
    path('test/diet/<str:prognosis>/', views.diet, name='diet'),
    path('message/', views.message, name='message'),
]
