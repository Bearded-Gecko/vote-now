from django.db import models

# Create your models here.

class Poll(models.Model): #create poll model
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

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count

