import email
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistraion
from .models import User
# Create your views here.

# this function is used for add the data


def add_show(request):

    if request.method == 'POST':
        fm = StudentRegistraion(request.POST)
        # if fm.is_valid(): this is one way to save the data into database
        #     fm.save()
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            fm = User(name=nm, email=em, password=pw)
            fm.save()
            fm = StudentRegistraion()

    else:
        fm = StudentRegistraion()
    student = User.objects.all()
    return render(request, "enroll/addandshow.html", {"form": fm, 'student': student})


# this function for update
def update_data(request, id):
    if request.method == 'POST':
        pk = User.objects.get(pk=id)
        pf = StudentRegistraion(request.POST, instance=pk)
        if pf.is_valid():
            pf.save()
    else:
        pk = User.objects.get(pk=id)
        pf = StudentRegistraion(instance=pk)

    return render(request, 'enroll/updatestudent.html', {'form': pf})


# this function for delete
def delete_data(request, id):
    if request.method == 'POST':
        us = User.objects.get(pk=id)
        us.delete()
    return HttpResponseRedirect('/')
