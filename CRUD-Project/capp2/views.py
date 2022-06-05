from django.shortcuts import render,redirect
from capp2.models import Employee
from capp2.forms import EmployeeForm

# Create your views here.

def home_view(request):
	employees = Employee.objects.all()
	return render(request,'capp2/home.html',{'employees':employees})

def insert_view(request):
	form = EmployeeForm()
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/home')
	return render(request,'capp2/insert.html',{'form':form})


def delete_view(request,id):
	employees = Employee.objects.get(id=id)
	employees.delete()
	return redirect('/home')


def update_view(request,id):
	employees = Employee.objects.get(id=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST,instance=employees)
		form.save()
		return redirect('/home')
	return render(request,'capp2/update.html',{'employees':employees})