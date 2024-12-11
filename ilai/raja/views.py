from django.shortcuts import render,redirect
from raja.form import registerform 
from raja.models import data
from django.contrib import messages
# Create your views here.
def home(request):
    myform=registerform()
    mydata=data.objects.all()
    if mydata!='':
        return render(request,"index.html",{'form':myform,'data':mydata})
    else:
        return render(request,"index.html",{'form':myform})
def adddata(request):
    if request.method=="POST":
        myform=registerform(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Record added successfully .....!!!!")
            return redirect('home')

def updatedata(request,id):
    mydata=data.objects.get(id=id)
    myform=registerform(instance=mydata)
    if request.method=='POST':
        myform=registerform(request.POST,instance=mydata)
        if myform.is_valid():
            myform.save()
            messages.success(request,"record updated successfully...!!!")
            return redirect('home')
    context={'forms':myform}
    return render(request,"update.html",context)


def deletedata(request,id):
    mydata=data.objects.get(id=id)
    mydata.delete()
    messages.success(request,"record deleted successfully ....!!!")
    return redirect('home')


