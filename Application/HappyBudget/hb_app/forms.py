from django import forms 
from django.core import validators

#create own validator 

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")
#then put this in validators 

class SignUpForm(forms.Form):
    username = forms.CharField()
    profile_name = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    verify_password = forms.CharField(widget = forms.PasswordInput)
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')

    botcatcher = forms.CharField(required=False,
        widget = forms.HiddenInput,
        validators = [validators.MaxLengthValidator(0)])
    #clean whole form and validate
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        password = all_clean_data['password']
        vpassword = all_clean_data['verify_password']


        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAIL MATCHES")
        if password != vpassword:
            raise forms.ValidationError("MAKE SURE PASSWORD MATCHES")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    botcatcher = forms.CharField(required=False,
        widget = forms.HiddenInput,
        validators = [validators.MaxLengthValidator(0)])
    #clean whole form and validate
    def clean(self):
        all_clean_data = super().clean()


    #use the built in validators instead
    '''
    #creating for cleaning / form validaiton
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
    '''