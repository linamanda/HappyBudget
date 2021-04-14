from django.urls import include, path
from hb_app import views

urlpatterns = [
    #views.index because we called the function index
    path('', views.index, name='index'), 
    path('png',views.png, name='png'),
    #happy budget stuff 
    path('accounts',views.accounts, name='accounts'),
    path('finances',views.finances, name='finances'),
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('personalGoals',views.personalGoals, name='personalGoals'),

    #random file to test db connections
    path('dummy',views.dummy, name='dummy'),
]