from django.contrib import admin
from django.urls import path
from employeeapp.views import *
urlpatterns=[
    path("",home,name=""),
    path("view_employee",view_employee,name="view_employee"),
    path("employee_profile",employee_profile,name="employee_profile"),
    path("signup",signup,name="signup"),
    path("approve_employee/<int:id>",approve_employee,name="approve_employee"),
    path("delete_employee/<int:id>",delete_employee,name="delete_employee"),
    path("edit_employee/<int:id>",edit_employee,name="edit_employee"),
    path("logouts",logouts,name="logouts"),


]