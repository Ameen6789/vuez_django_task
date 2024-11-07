from .models import Employee,User
from django import forms
class UserForm(forms.ModelForm):
    confirm_password=forms.CharField(required=False,max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
    password=forms.CharField(required=False,max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
    email=forms.EmailField(required=False,max_length=100,widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}))
    class Meta:
        model=User
        fields=["first_name","last_name","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last Name"}),
        }
    def clean(self):
        cleaned_data=super().clean()
        password = cleaned_data.get("password")
        if not password:
            cleaned_data.pop("password", None)
        email = cleaned_data.get("email")
        if not email:
            cleaned_data.pop("email", None)
            
        if cleaned_data.get('password') and cleaned_data.get("confirm_password"):
            password=cleaned_data.get('password')
            confirmpassword=cleaned_data.get("confirm_password")
            if len(password)<8:
                self.add_error("password","password should be atleast 8 characters")
            elif password!=confirmpassword:
                self.add_error("confirm_password","passwords do not match")
class EmployeeForm(forms.ModelForm): 
    class Meta:
        model=Employee
        fields=["phone_number","department","address"] 
        widgets={
            "phone_number":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Phone Number"}),
            "department":forms.Select(attrs={"class":"form-select","placeholder":"Enter Department"}),
            "address":forms.Textarea(attrs={"class":"form-control","rows":4,"placeholder":"Enter Address"})
        }
    def clean(self):
        cleaned_data=super().clean()
        if (cleaned_data.get("phone_number")):
            phone_number=cleaned_data.get("phone_number")
            if not phone_number:
                self.add_error("phone_number","phone_number required")
        
        
        if phone_number and len(str(phone_number))!=10:
            self.add_error("phone_number","phone number should be 10 digits")
    
