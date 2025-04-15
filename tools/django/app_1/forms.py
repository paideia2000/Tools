from django import forms

class CreatNewTask(forms.Form):
    title = forms.CharField(label="Title for task", max_length=150)
    description = forms.CharField(label="Description to the task", widget= forms.Textarea)