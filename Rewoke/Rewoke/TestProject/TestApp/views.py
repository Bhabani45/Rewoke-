from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from TestApp.models import DemoEmployee 
from TestApp.forms import CustomerForm


# Create your views here.
def edit(request,id):
    customer = DemoEmployee.objects.get(id=id)
    return render(request , "edit.html", {"customer":customer})

def update(request, id):
    customer = DemoEmployee.objects.get(id=id)
    form = CustomerForm(request.POST , instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/list')
        return render(request , "edit.html", {"customer":customer})

def delete(request , id):
    customer = DemoEmployee.objects.get(id=id)
    customer.delete()
    return redirect("/list")

def list(request):
    context = {'list': DemoEmployee.objects.all()}
    return render(request , 'list.html' , context)



def add(request ):
    
    if request.method == "POST":
        form = CustomerForm(request.POST)
        #form.save()
        if form.is_valid():
            try:
                form.save()
                return redirect('/list')
            except:
                pass
    else :
        form = CustomerForm
        return render(request , "add.html" , {"form":form})


