from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll #set the model as poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'option_five', 'poll_duration', 'email_one', 'email_two', 'email_three', 'email_four', 'email_five'] #set the fields that are used 