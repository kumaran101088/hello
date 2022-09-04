from asyncore import read
from django.shortcuts import render
from django.contrib import messages
from .store_csv import read_convert_file
import pandas as pd

def upload_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if str(file).endswith('.csv'):
            read_convert_file(file)
        else:
            messages.error(request, 'This is not a CSV file!')
    return render(request, 'index.html')
