from django.urls import include, path
from first_app import views

urlpatterns = [
    #views.index because we called the function index
    path('', views.index, name='index'), 
    path('png',views.png, name='png'),
]