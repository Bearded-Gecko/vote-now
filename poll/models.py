from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Poll(models.Model): #create poll model

    #Poll Questions and Counts
    question = models.TextField() #text field
    option_one = models.CharField(max_length = 30) #character fields
    option_two = models.CharField(max_length = 30)
    option_three = models.CharField(max_length = 30)
    option_four = models.CharField(max_length = 30, null = True)
    option_five = models.CharField(max_length = 30, null = True)
    option_one_count = models.IntegerField(default = 0) #store vote counts for each option, default is to start at 0
    option_two_count = models.IntegerField(default = 0)
    option_three_count = models.IntegerField(default = 0)
    option_four_count = models.IntegerField(default = 0)
    option_five_count = models.IntegerField(default = 0)

    #time limit on poll
    start_time = models.DateTimeField(default = datetime.now, blank = True) #date and time of when poll was created
    poll_duration = models.DurationField(default = timedelta(minutes = 60) ) #duration for poll to be active; default to 60 minutes, i.e., 01:00:00

    #email addresses
    email_one = models.EmailField(max_length = 254, default = 'na@email.com')
    email_two = models.EmailField(max_length = 254, default = 'na@email.com')
    email_three = models.EmailField(max_length = 254, default = 'na@email.com')
    email_four = models.EmailField(max_length = 254, default = 'na@email.com')
    email_five = models.EmailField(max_length = 254, default = 'na@email.com')
    
    def total(self):
        #used to display the total number of votes in a poll
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count

