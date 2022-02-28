
from django import forms

class Loandata(forms.Form):
    loanDate=forms.DateField()
    releasedata=forms.DateField()
    principalAmount=forms.IntegerField()