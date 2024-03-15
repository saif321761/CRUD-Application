from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


# Create your views here.
# student information add and show kry ga
def addandshow(request):
    if request.method == 'POST':
        obj = StudentRegistration(request.POST)
        if obj.is_valid():
            obj.save()
            obj = StudentRegistration()
    else:
        obj = StudentRegistration()
    student = User.objects.all()


    return render(request, 'enroll/addandshow.html',{'form':obj,'stu':student})

def delete_data(request,id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect('/')
    
def update_data(request, id):
    obj = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration(instance=obj)    

    return render(request, 'enroll/updatestudent.html', {'form': fm})