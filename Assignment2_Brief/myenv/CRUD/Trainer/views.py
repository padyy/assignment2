'''Coding Bootcamp - Assigment 
  -Title:  Assignment 2 Brief 
  -Last name : Pantelakis
  -First Name: Ioannis
  -Advisors: Giachoudis Nikolaos , Tzoumpa Danae 
  -Python ver:3.9.2
  -win: win10 64bit
'''
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render
from .models import Trainer
from .forms import TrainerForm

#view for a home page so the user decide what action want to take.
def home_page(request):
    return render(request, 'Trainer/home.html', {})

#view for adding(creating) new trainers
def create_trainer(request):
    if request.method == 'GET':
        form = TrainerForm()
    else:
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Trainer successfully added!'
            return HttpResponseRedirect('/trainer/success/'+msg+'/')
    return render(request, 'Trainer/create_trainer.html', {'form': form})

#class for reading the trainers from the db
class TrainerList(ListView):
    model = Trainer
    template_name = 'Trainer/read_trainer.html'
    context_object_name = 'trainer_list'
    queryset = Trainer.objects.order_by('lastname') 

#view for success page message
def success(request, message):
    return render(request, 'trainer/success.html', {'message': message})

#class for update page for the trainers from the db
class TrainerUpdateList(ListView):
    model = Trainer
    template_name = 'Trainer/update_trainer_page.html'
    context_object_name = 'trainer_list'
    queryset = Trainer.objects.order_by('lastname') 

#view for update/edit the trainers
def update_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    msg_blank=()
    
    if request.method == 'POST':
        message = 'You have successfully updated trainer: ' + trainer.lastname

        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        subject = request.POST.get('subject')
        courses = request.POST.get('courses')

        if ((name !=None) and (lastname !=None) and (subject !=None) and (courses !=None)): # The input is validated via the form in the template, but for future puprose i written an if-else statement for upgrade-extra safe.
            trainer.name = name
            trainer.lastname = lastname
            trainer.subject = subject
            trainer.courses = courses
            trainer.save()
            return HttpResponseRedirect('/trainer/success/'+message+'/')
        else:
            msg_blank = "You cant update with blank inputs. Please fill all the inputs"
    else:
        context = {
            'trainer': trainer, 'msg_blank' : msg_blank ,
        }

    return render(request, 'trainer/update_trainer.html', context)

#class for delete page for the trainers from the db
class TrainerDeleteList(ListView):
    model = Trainer
    template_name = 'Trainer/delete_trainer_page.html'
    context_object_name = 'trainer_list'
    queryset = Trainer.objects.order_by('lastname') 

#view for delete trainers from db
def delete_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    message = 'You have successfully deleted trainer: ' + trainer.lastname
    return HttpResponseRedirect('/trainer/success/'+message+'/')

#view for about page.
def about_page(request):
    return render(request, 'Trainer/about.html', {})