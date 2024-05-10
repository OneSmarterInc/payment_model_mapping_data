from django.shortcuts import render
import csv
import sqlite3
from io import StringIO
from django.db.models import Q
from django.core.serializers import serialize
from django.urls import reverse
from django.http import JsonResponse,FileResponse,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import zipfile
import tempfile,time
from rest_framework.response import Response
import re
from io import BytesIO
from pathlib import Path
import os,json
import pdfplumber
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MappingData,Column_mapping_data,ban_onboarding_payment
from .serializers import post_mapping_serializer,get_mapping_serializer,column_serializer
from rest_framework import status

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES.get('file')
    try:
        df_csv = pd.read_csv(BytesIO(file.read()))
        df_csv.columns = df_csv.columns.str.strip()
        df_csv.columns = df_csv.columns.str.strip().str.replace('-', '').str.replace(r'\s+', ' ', regex=True).str.replace(' ', '_')
        columns_list = df_csv.columns.tolist()
        column_names_str = ','.join(columns_list)
        col_dict = {
                'columns':column_names_str
        }
        instance = Column_mapping_data(**col_dict)
        instance.save()
        with tempfile.NamedTemporaryFile(delete=False) as temper_file:
                for chunk in file.chunks():
                    temper_file.write(chunk)
                path = temper_file.name

        buffer_data_csv = {'csv_path': path}
        buffer_path_csv = Path('buffer_csv_map.json')
        with open(buffer_path_csv, 'w') as file:
                json.dump([buffer_data_csv], file)
                return Response({'status': 'success', 'message': 'CSV uploaded successfully.'}, status=200)

    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})
    
payment_instance = MappingData(Account_Number='Done', Remmitance_Address='123 Main St', Remmitance_City='Anytown', Remmitance_State='CA', Remmitance_Zip='12345', Remmitance_Country='USA', Payment_Mode='Credit Card', URL='https://example.com', Username='example_user', Password='example_password', Vendor_Name='Example Vendor', Bank_Name='Example Bank', Bank_Account_Number='9876543210', Bank_Routing_Number='123456789', Bank_Account_Type='Savings', Auto_Pay='Yes')
payment_instance.save()

class get_column_names(APIView):
    def get(self,request):
        db_data = Column_mapping_data.objects.all()
        serializer = column_serializer(db_data,many=True)
        return Response(serializer.data)
    
class post_mapping_data(APIView):
    def post(self,request):
        data = request.data
        serializer = post_mapping_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class get_mapping_data(APIView):
    def get(self,request):
        db_data = MappingData.objects.all()
        serializer = get_mapping_serializer(db_data, many=True)
        return Response(serializer.data)
    


    




            
