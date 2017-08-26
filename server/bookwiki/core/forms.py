from bootstrap import widgets
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import ugettext_lazy as _


class ProfileForm (forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
        widgets = widgets.ModelWidgets(get_user_model())

class LoginForm (AuthenticationForm):
    
    username = UsernameField(
        max_length=254,
        widget=widgets.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=widgets.PasswordInput,
    )
