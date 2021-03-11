from django.shortcuts import render
from .models import Profile,Data
from .forms import Employee

# Create your views here.
def home(request):
    profile = Profile.objects
    if request.method == 'POST':
        fm = Employee(request.POST) 
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pn = fm.cleaned_data['phone']
            pr = fm.cleaned_data['Project']
            reg = Data(name=nm ,email=em,phone=pn,Project=pr)
            reg.save()
            fm = Employee() 

    else:
        fm = Employee() 

    return render(request,'home.html',{'profile': profile, 'form':fm})
