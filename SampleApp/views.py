from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Hello World!!!</h1>")

def sam(request):
	return HttpResponse("<h2>Welcome to django online intership session</h2>")

def dyn(request,a):
	return HttpResponse("<h1>my roll number is :{}</h1>".format(a))

def data(request,b,id):
	return HttpResponse("<h2> {} ")


def temp(request):
	return render(request,'temp.html',{})

def table(request):
	return render(request,'table.html',{})

def details(request,id,name):
	return render(request,'details.html',{'i':id,'n':name})

def inline(request):
	return render(request,'inline.html')

def internal(request):
	return render(request,'internal.html')

def external(request):
	return render(request,'external.html')

	