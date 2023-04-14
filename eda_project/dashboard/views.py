from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def EDA1(request):
    return render(request, 'EDA1.html')
def EDA2(request):
    return render(request, 'EDA2.html')
def EDA3(request):
    return render(request, 'EDA3.html')
def EDA4(request):
    return render(request, 'EDA4.html')

def DataCleansing(request):
    return render(request, 'DataCleansing.html')