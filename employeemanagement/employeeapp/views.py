from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import User,Employee
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm,EmployeeForm
from django.db import IntegrityError

def home(request):
    if request.method=="POST":
        
        username=request.POST["email"]
        password=request.POST["password"]
        
        user=authenticate(username=username,password=password)
        
        
        if user is not None:
            if user.is_superuser==1:
                login(request,user)
                return JsonResponse({'success':True,'usertype':'admin'},status=200)

            elif user.is_staff==1:
                
                request.session["emp_id"]=user.id
                login(request,user)

                return JsonResponse({'success':True,'usertype':'employee'},status=200)
        else:
           
            return JsonResponse({'success':False},status=400)
    return render(request,"index.html")


def view_employee(request):
    data=Employee.objects.all()
    return render(request,"view_employee.html",{"employee_data":data})

def employee_profile(request):
    empid=request.user 
    data=Employee.objects.get(user_id=empid)
    return render(request,"employee_profile.html",{"employee":data})

def delete_employee(request,id):
    employee=User.objects.get(id=id)
    employee.delete()
    return redirect("view_employee")

def signup(request):
    if request.method=="POST":
       
        user_form=UserForm(request.POST)
        employee_form=EmployeeForm(request.POST)
        
        if user_form.is_valid() and employee_form.is_valid():
            try:
                
                username=user_form.cleaned_data.get("email")
                user=user_form.save(commit=False)
                password=user_form.cleaned_data.get("password")
                user.set_password(password)
                user.username=username
                user.user_type="employee"
                user.is_active=0
                user.is_staff=1
                user.save()
                user_id=user.id
                employee=employee_form.save(commit=False)
                employee.user_id=user_id
                employee.save()
            
                
                return JsonResponse({"success":True})
            except IntegrityError as e:
                other_errors="Account already exists"
                return JsonResponse({"success":False,"other_errors":other_errors},status=400)
        else:
            return JsonResponse({"success":False,"errors":[employee_form.errors,user_form.errors]},status=400)
        
        
    else:
        user_form=UserForm()
        employee_form=EmployeeForm()
        
    return render(request,"register.html",{"user_form":user_form,"employee_form":employee_form})
def approve_employee(request,id):
    employee=User.objects.get(id=id)
    employee.is_active=1
    employee.save()
    return redirect("view_employee")

def edit_employee(request,id):
    employee=Employee.objects.get(user_id=id)
    user=User.objects.get(id=id)
    emp_id=id
    if request.method=="POST":
        user_form=UserForm(request.POST,instance=user)
        employee_form=EmployeeForm(request.POST,instance=employee)
        
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            
            return JsonResponse({"success":True})
        else:
            return JsonResponse({"success":False,"errors":employee_form.errors},status=400)
    else:
        
        user_form=UserForm(instance=user)
        employee_form=EmployeeForm(instance=employee)
        
        return render(request,"edit_employee.html",{"user_form":user_form,"employee_form":employee_form,"emp_id":emp_id})



def logouts(request):
    logout(request)
    return redirect("")


