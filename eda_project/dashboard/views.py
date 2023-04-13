from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def EDA(request):
    return render(request, 'EDA.html')

def DataCleansing(request):
    return render(request, 'DataCleansing.html')