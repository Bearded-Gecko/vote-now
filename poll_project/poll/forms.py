from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll #set the model as poll
        fields = ['question', 'option_one', 'option_two', 'option_three'] #set the fields that are used 