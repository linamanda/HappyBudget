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

    path('signUp', views.signUp, name = 'signUp'),
    path('processSignUp', views.processSignUp, name = 'processSignUp'),
    path('processLogin', views.processLogin, name = 'processLogin'),


    path('personalGoals',views.personalGoals, name='personalGoals'),
    path('interactivePet',views.interactivePet, name='interactivePet'),
    #random file to test db connections
    path('dummy',views.dummy, name='dummy'),
    path('new', views.newPage)
]