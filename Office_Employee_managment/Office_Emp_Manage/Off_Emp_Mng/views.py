from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')



def Add_Employee(request):
    if request.method =='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      phone=int(request.POST['phone'])
      dept=int(request.POST['dept'])
      role=int(request.POST['role'])
      salary=int(request.POST['salary'])
      bonus=int(request.POST['bonus'])
      new_emp=Employee(first_name=first_name,last_name=last_name,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now(), salary=salary,bonus=bonus )
      new_emp.save()
      return HttpResponse('Add SuccessFully')
    elif request.method=='GET':
        return render(request,'AddEmployee.html')
    else:
         return HttpResponse('An Error Occured')
     
     
     

def Remove_Employee(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse('Employee Removed SuccessFully')
        except:
            return HttpResponse('Enter a valide Emp_Id')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'RemoveEmployee.html',context)


def All_Employee(request): 
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'ViewEmployee.html',context)


def Filter_Employee(request):
    if request.method =='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) |Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        context={
        'emps':emps
          }
        return render(request,'ViewEmployee.html',context)
    elif request.method=='GET':
        return render(request,'FilterDetails.html')
    else:
        return HttpResponse('An Exception Occured')
          