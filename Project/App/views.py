from django.shortcuts import render
from .form import EmployeeForm

# Create your views here.
def django_fun(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form1 = EmployeeForm(request.POST)
        if form1.is_valid():
            eid = form1.cleaned_data['eID']
            ename = form1.cleaned_data['eName']
            esalary = form1.cleaned_data['eSalary']
            return render(request,'index.html',{'eid':eid,'ename':ename,'esalary':esalary})
    return render(request,'form.html',{'form':form})

