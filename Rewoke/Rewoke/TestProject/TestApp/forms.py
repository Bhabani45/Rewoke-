from django import forms

from TestApp.models import DemoEmployee

class CustomerForm(forms.ModelForm):
    class Meta:
        model = DemoEmployee
        fields = "__all__"
        