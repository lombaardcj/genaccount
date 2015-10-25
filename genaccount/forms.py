from django import forms

from .models import Account

class ShowAccountForm(forms.Form):
    account = forms.ModelChoiceField(
        queryset=Account.objects.all(), label='', empty_label='',
        widget=forms.Select(
            attrs={'onchange': 'this.form.submit();',
                   'class': 'form-control account-autocomplete',
                   'placeholder': 'Jump to an Account'}),
    )
