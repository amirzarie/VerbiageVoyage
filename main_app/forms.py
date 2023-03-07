from django.forms import ModelForm
from .models import Etymology


class EtymolodyForm(ModelForm):
    class Meta:
        model = Etymology
        fields = ["date", "example"]