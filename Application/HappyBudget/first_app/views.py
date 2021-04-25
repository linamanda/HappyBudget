from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms 

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}


    my_dict = {'insert_me': "Hello I am from first_app/views.py"}
    return render(request,'first_app/index.html', context=date_dict)

def index2(request):
    my_dict = {'insert_me': "Hello I am from first_app/views.py"}
    return render(request,'first_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if(request.method == 'POST'):
        form = forms.FormName(request.POST)

        if(form.is_valid()):
            # DO SOMETHING HERE 
            print("VALDIATION SUCCESS")
            print("NAME: " + form.cleaned_data['name'])

    return render(request, 'first_app/form_page.html', {'form':form})

def png(request):
    random = {'wow':'wow'}
    return render(request,'first_app/png.html',context=random)