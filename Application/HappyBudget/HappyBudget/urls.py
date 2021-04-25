"""HappyBudget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from first_app import views
from hb_app import views as hb_views



urlpatterns = [
    #views.index because we called the function index
    path('', views.index, name='index'), 
    path('png', views.png, name='png'), #this lets it so you do not need 'first_appl/png'
    path('formpage/', views.form_name_view, name = 'form_name'),
    #using url includes
    path('first_app/', include('first_app.urls')),
    path('hb_app/', include('hb_app.urls')),
    path('admin/', admin.site.urls),
]
