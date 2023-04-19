from django.shortcuts import render, redirect #render combines a given template with a given context dictionary and returns HttpResponse object with that rendered text
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse

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

    if request.method == 'POST': #check if it is a post request (submit)
        selected_option = request.POST['poll'] #displays which option was selected after clicking submit
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')
        
        poll.save() #save result

        return redirect('results', poll.id) #return to results page via particular poll id

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

def results(request, poll_id): #vote and result have to work with specific pole, thus we have pole_id
    poll = Poll.objects.get(pk = poll_id) #query for the poll in question
    context = {
        'poll' : poll #pass poll to context which goes to the template
    }
    return render(request, 'poll/results.html', context)