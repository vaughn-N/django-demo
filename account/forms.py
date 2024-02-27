

from django import forms

from account.models import Developer


class EntryForm(forms.Form):
    firstname = forms.CharField()    
    middlename = forms.CharField()
    birthdate = forms.DateField()

class EntryModelForm():

    class Meta:
        model = Developer
        fields = "__all__"