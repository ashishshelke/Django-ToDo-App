from django import forms

class AddTaskForm(forms.Form):
    task = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))