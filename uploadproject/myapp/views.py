import pandas as pd
from google.cloud import storage
from django.shortcuts import render
from django.contrib import messages
from .store_csv import read_convert_file

storage_client = storage.Client()

def upload_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if str(file).endswith('.csv'):
            read_convert_file(file)
            bucket = storage_client.get_bucket('my-fourth-bucket')
            blob = bucket.blob('MOCK_DATA.csv')
            try:
                blob.delete()
                blob.upload_from_filename('MOCK_DATA.csv')
            except Exception as e:
                print(e)
        else:
            messages.error(request, 'This is not a CSV file!')
    return render(request, 'index.html')
