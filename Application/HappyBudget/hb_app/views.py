from django.shortcuts import render
from django.http import HttpResponse
from hb_app.models import Goals,Transactions,Users

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello I am from first_app/views.py"}
    return render(request,'hb_app/index.html', context=my_dict)

def png(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/png.html',context=random)

def accounts(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/accounts.html',context=random)

def finances(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/finances.html',context=random)

def home(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/home.html',context=random)

def login(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/login.html',context=random)

def personalGoals(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/personalGoals.html',context=random)

def dummy(request):
    webpages_list = Users.objects.order_by('user_id').using('HappyBudget')
    date_dict = {'access_records':webpages_list}

    random = {'wow':'wow'}
    return render(request,'hb_app/dummy.html',context=date_dict)
