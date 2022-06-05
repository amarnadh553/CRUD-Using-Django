from django import forms
from capp2.models import Employee

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'