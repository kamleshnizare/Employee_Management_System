from django import forms

class EmployeeForm(forms.Form):
    eID = forms.IntegerField()
    eName = forms.CharField(max_length=64)
    eSalary = forms.FloatField()