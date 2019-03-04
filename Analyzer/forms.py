from django import forms
from . import models

class addExpense_form(forms.ModelForm):
    class Meta():
        model=models.general_expenses
        fields="amount","category","remarks"

class mandExpense_form(forms.ModelForm):
    class Meta():
        model=models.mandatory_expenses
        fields="amount","category","remarks","date"
