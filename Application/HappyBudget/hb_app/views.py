from django.shortcuts import render, redirect
from django.http import HttpResponse
from hb_app.models import Goals,Transactions,Users

from . import forms 

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

def signUp(request):
    form = forms.SignUpForm()
    if 'message' in request.session: 
        if request.session['message'] == "E-mail already registered" or request.session['message'] == "Either e-mail does not match or passwords do not match":
            print("HERE")
            old_value = request.session['message']
            del request.session['message']
            request.session.modified = True
            return render(request, 'hb_app/signUp.html', {'form':form, 'message':old_value})
        else:
            #remove the old message 
            del request.session['message']
            request.session.modified = True
            return render(request, 'hb_app/signUp.html', {'form':form})
    else:
        print("HERE HERE")
        return render(request, 'hb_app/signUp.html', {'form':form})



def login(request):
    form = forms.LoginForm()
    if 'message' in request.session:
        #THIS PART DOES NOT CHEKC IF THEIR IS AN ACCOUNT WITH THAT EMAIL
        if request.session['message'] == "Account has been created" or request.session['message'] == "Inputted wrong account information":
            #return render(request, 'hb_app/login.html', {'form':form, 'message':request.session['message']})
            print("HERE")
            old_value = request.session['message']
            del request.session['message']
            request.session.modified = True
            return render(request,'hb_app/login.html',context={'message': old_value, 'form': form})
        else:
            #remove the old message 
            del request.session['message']
            request.session.modified = True
            return render(request,'hb_app/login.html', context={'form': form})
    else:
        #return render(request, 'hb_app/login.html', {'form':form})
        print("HERE HERE")
        return render(request,'hb_app/login.html', context={'form': form})

def personalGoals(request):
    goals_list = Goals.objects.order_by('goal_id')
    date_dict = {'personal_goals':goals_list}

    random = {'wow':'wow'}
    return render(request,'hb_app/personalGoals.html',context=date_dict)

def dummy(request):
    webpages_list = Users.objects.order_by('user_id')
    
    date_dict = {'access_records':webpages_list}

    random = {'wow':'wow'}

    return render(request,'hb_app/dummy.html',context=date_dict)

def interactivePet(request):
    random = {'wow':'wow'}
    return render(request,'hb_app/interactivePet.html',context=random)

def newGoal(request):
    name = request.POST.get("goalname1")
    target = request.POST.get("goaltarget1")
    current = request.POST.get("goalcurrent1")

    #THIS IS A TEMPORARY SOLUTION
    goal_id_TEMP = 10
    #############################

    o_ref = Goals(goal_name=name, goal_target=target, goal_current=current)
    o_ref.save()

    #return render(request, 'hb_app/personalGoals.html', {"message": "registered"})
    return redirect('personalGoals')
    
def deleteGoal(request, gn):
    goal_to_delete = Goals.objects.get(goal_name=gn)
    goal_to_delete.delete()
    return redirect('personalGoals')


def signUp(request):
    form = forms.SignUpForm()
    if 'message' in request.session: 
        if request.session['message'] == "E-mail already registered" or request.session['message'] == "Either e-mail does not match or passwords do not match":
            print("HERE")
            old_value = request.session['message']
            del request.session['message']
            request.session.modified = True
            return render(request, 'hb_app/signUp.html', {'form':form, 'message':old_value})
        else:
            #remove the old message 
            del request.session['message']
            request.session.modified = True
            return render(request, 'hb_app/signUp.html', {'form':form})
    else:
        print("HERE HERE")
        return render(request, 'hb_app/signUp.html', {'form':form})

def processSignUp(request):
    print(request.method == 'POST')
    if(request.method == 'POST'):
        form = forms.SignUpForm(request.POST)
        print(form.is_valid())
        if(form.is_valid()):
            print("RIGHJT ERE ")
            # DO SOMETHING HERE 
            #print("VALDIATION SUCCESS")
            #print("NAME: " + form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            #username = request.POST.get("username")
            #password = request.POST.get("password")
            #email = request.POST.get("email")
            #webpages_list = Users.objects.order_by('user_id').using('HappyBudget')
            users_list = Users.objects.values_list('user_id', 'user_email').filter(user_email=email)
            if len(users_list) > 0:
                #form = forms.SignUpForm()
                #return render(request, 'hb_app/signUp.html', {"message": "E-mail already registered", 'form':form})
                print("ERROR", len(users_list))
                request.session['message'] = "E-mail already registered"
                return redirect('signUp')
            else:
                #form = forms.SignUpForm()
                o_ref = Users(user_name=username, user_password=password, user_email=email)
                o_ref.save()
                #return render(request, 'hb_app/login.html', {"message": "Account has been created", 'form':form})
                print("CREATE ACCOUNT")
                #login(request)
                request.session['message'] = "Account has been created"
                return redirect('login')
        # form is invalid:
        request.session['message'] = "Either e-mail does not match or passwords do not match"
        return redirect('signUp')
    return render(request, 'hb_app/login.html', {"message": "ERROR OCCURED"})

def processLogin(request):
    print(request.method == 'POST')
    if(request.method == 'POST'):
        form = forms.LoginForm(request.POST)
        print(form.is_valid())
        if(form.is_valid()):
            print("RIGHJT ERE ")
            # DO SOMETHING HERE 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users_list = Users.objects.values_list('user_id', 'user_email').filter(user_name=username)
            if len(users_list) > 0:
                #valid user 
                request.session['username'] = username
                return redirect('home')
            #wrong login information
            else:
                #print("ERROR", len(users_list))
                request.session['message'] = "Inputted wrong account information"
                #return redirect('signUp')
                return redirect('login')
        # form is invalid:
        request.session['message'] = "Either e-mail does not match or passwords do not match"
        return redirect('signUp')
    return render(request, 'hb_app/login.html', {"message": "ERROR OCCURED"})

