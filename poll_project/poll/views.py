from django.shortcuts import render, redirect #render combines a given template with a given context dictionary and returns HttpResponse object with that rendered text
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse
from django.utils import timezone #for time-out feature
from django.core.mail import send_mail #for notify-user feature
import pandas as pd



# Create your views here.

def home(request): #define one home for home.html that takes in a request
    polls = Poll.objects.all() #will give you all the polls from the DB

    context = {
        'polls' : polls
        }
    
    return render(request, 'poll/home.html', context) #return poll directory and name of home.html 

def create(request): 

    if request.method == 'POST':
        form = CreatePollForm(request.POST) #instantiate the form and pass in the POST data
        if form.is_valid():
            # print(form.cleaned_data['option_one']) #prints out the value in the key, e.g., question, option_[insert]
            form.save() #save it to database
            return redirect('home') #redirect user to home
    else:
        form = CreatePollForm() #instantiate form in create view; instantiate with nothing

    context = {
        'form' : form #passing form into context which then goes to the template
    }
    return render(request, 'poll/create.html', context) 

def vote(request, poll_id): #vote and result have to work with specific pole, thus we have pole_id

    poll = Poll.objects.get(pk = poll_id) #query for particular poll for id being passed in, primary key is poll_id

    #check if poll is still active
    current_time = timezone.now() #what is the current date+time?
    end_time = poll.start_time + poll.poll_duration #poll end date+time
    if current_time > end_time: #if we are past the end time
        return render(request, 'poll/poll_closed.html') #return page that says poll is closed

    #if submit is clicked = handle form submission and vote counting
    if request.method == 'POST': #check if it is a post request (submit)
        selected_option = request.POST['poll'] #displays which option was selected after clicking submit
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        elif selected_option == 'option5':
            poll.option_five_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')
        
        poll.save() #save result to DB

        return redirect('results', poll.id) #return to results page via particular poll id

    context = {
        'poll' : poll
    }

    return render(request, 'poll/vote.html', context)

def results(request, poll_id): #vote and result have to work with specific pole, thus we have pole_id
    poll = Poll.objects.get(pk = poll_id) #query for the poll in question

    #format result output for email
    options = [poll.option_one, poll.option_two, poll.option_three, poll.option_four, poll.option_five]
    vote_counts = [poll.option_one_count, poll.option_two_count, poll.option_three_count, poll.option_four_count, poll.option_five_count]
    df = pd.DataFrame({'Options': options, 'Votes': vote_counts}) #create dataframe from two lists of options and votes
    df_sorted = df.sort_values('Votes', ascending = False) #sort in descending order
    email_body = df_sorted.to_string(index=False) #convert df to string; do not include index
    
    email_subject = poll.question #question of poll

    email_recipients = [poll.email_one, poll.email_two, poll.email_three, poll.email_four, poll.email_five] #list of receipients to email

    #send email to users
    if request.method == 'POST': #check if email results was clicked
        current_time = timezone.now() #what is the current date+time?
        end_time = poll.start_time + poll.poll_duration #poll end date+time
        if current_time > end_time: #if we are past the end time
            
            #email results
            send_mail(poll.question, #email subject
            email_body, #body
            'testing.mikeho@gmail.com', #from
            email_recipients, #recipients
            fail_silently = False
            )

            return render(request, 'poll/results_sent.html')
        else:
            return render(request, 'poll/still_active.html')

    context = {
        'poll' : poll #pass poll to context which goes to the template
    }


    return render(request, 'poll/results.html', context)