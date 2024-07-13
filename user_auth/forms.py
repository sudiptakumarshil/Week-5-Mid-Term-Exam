from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']