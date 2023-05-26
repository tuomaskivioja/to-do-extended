from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a new item...'}),
        label=''
    )
    priority = forms.ChoiceField(
        choices=[('1', 'Priority 1'), ('2', 'Priority 2'), ('3', 'Priority 3')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=''
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a description', 'rows': 3}),
        label=''
    )
