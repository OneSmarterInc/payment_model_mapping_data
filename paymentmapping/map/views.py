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
from .models import MappingData,Column_mapping_data,company_onbording_payment,sub_company_onbording_payment,vendor_onbording_payment,ban_onboarding_payment
from .serializers import post_mapping_serializer,get_mapping_serializer,column_serializer,company_onbording_payment_serializer,sub_company_onbording_payment_serializer,vendor_onbording_payment_serializer,ban_onbording_payment_serializer
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

company_instance = company_onbording_payment(company_name="Sample Company", company_address="123 Main St", company_city="Sample City", company_state="Sample State", company_zip="12345", company_tax_id="123-456-789", company_email="company@example.com", company_phone="123-456-7890", dm_first_name="John", dm_last_name="Doe", dm_email="john.doe@example.com", dm_phone="987-654-3210", payment_frequency="Monthly", weekdays=["Monday", "Tuesday", "Wednesday"], week="Week 1", date="2024-05-20", vendor_list=[{"vendor_name": "Vendor A", "vendor_address": "456 Market St", "vendor_city": "Vendor City", "vendor_state": "Vendor State", "vendor_zip": "54321", "vendor_email": "vendorA@example.com", "vendor_phone": "789-456-1230"}, {"vendor_name": "Vendor B", "vendor_address": "789 Grove St", "vendor_city": "Vendor City", "vendor_state": "Vendor State", "vendor_zip": "67890", "vendor_email": "vendorB@example.com", "vendor_phone": "987-654-3210"}])
company_instance.save()
sub_company_instance = sub_company_onbording_payment(company_name="Sample Company", sub_company_name="Sample Sub Company", sub_company_tax_id="987-654-321", sub_company_email="subcompany@example.com", sub_company_address="789 Elm St", sub_company_phone="987-654-3210", sub_company_city="Sub Company City", sub_company_state="Sub Company State", sub_company_zip="54321", dm_first_name="Jane", dm_last_name="Doe", dm_email="jane.doe@example.com", dm_phone="123-456-7890")
sub_company_instance.save()
vendor_instance = vendor_onbording_payment(vendor_name="Sample Vendor")
vendor_instance.save()


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
    
class edit_CompanyOnboardingPaymentDetail(APIView):
    def get_object(self, id):
        try:
            return company_onbording_payment.objects.get(id=id)
        except company_onbording_payment.DoesNotExist:
            return Response("record not found")

    def put(self, request, id):
        company_payment = self.get_object(id)
        serializer = company_onbording_payment_serializer(company_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class edit_SubCompanyOnboardingPaymentDetail(APIView):
    def get_object(self, id):
        try:
            return sub_company_onbording_payment.objects.get(id=id)
        except sub_company_onbording_payment.DoesNotExist:
            return Response("Record not found")

    def put(self, request, id):
        sub_company_payment = self.get_object(id)
        serializer = sub_company_onbording_payment_serializer(sub_company_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class edit_VendorOnboardingPaymentDetail(APIView):
    def get_object(self, id):
        try:
            return vendor_onbording_payment.objects.get(id=id)
        except vendor_onbording_payment.DoesNotExist:
            return Response("Record not found")

    def put(self, request, id):
        vendor_payment = self.get_object(id)
        serializer = vendor_onbording_payment_serializer(vendor_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class edit_banOnboardingPaymentDetails(APIView):
    def get_object(self, id):
        try:
            return ban_onboarding_payment.objects.get(id=id)
        except ban_onboarding_payment.DoesNotExist:
            return Response("Record not found")

    def put(self, request, id):
        ban_details = self.get_object(id)
        serializer = ban_onbording_payment_serializer(ban_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class delete_CompanyOnboardingPaymentDetail(APIView):
    def delete(self,request,id):
        instance = company_onbording_payment.objects.get(id=id)
        instance.delete()
        return Response("Record Deleted Sucessfully")
    
class delete_SubCompanyOnboardingPaymentDetail(APIView):
    def delete(self,request,id):
        instance = sub_company_onbording_payment.objects.get(id=id)
        instance.delete()
        return Response("Record Deleted Sucessfully")
    
class delete_VendorOnboardingPaymentDetail(APIView):
    def delete(self,request,id):
        instance = vendor_onbording_payment.objects.get(id=id)
        instance.delete()
        return Response("Record Deleted Sucessfully")
    
class delete_banOnboardingPaymentDetails(APIView):
    def delete(self,request,id):
        instance = ban_onboarding_payment.objects.get(id=id)
        instance.delete()
        return Response("Record Deleted Sucessfully")
    
class get_company_onboarding_details(APIView):
    def get(self,request):
        db_data = company_onbording_payment.objects.all()
        serializer = company_onbording_payment_serializer(db_data,many=True)
        return Response(serializer.data)
    
class get_vendor_onboarding_details(APIView):
    def get(self,request):
        db_data = vendor_onbording_payment.objects.all()
        serializer = vendor_onbording_payment_serializer(db_data,many=True)
        return Response(serializer.data)
    
class get_sub_company_onboarding_details(APIView):
    def get(self,request):
        data = request.data
        companyname = data.get("Companyname")
        subcompany = data.get("subcompanyname")
        db_data = sub_company_onbording_payment.objects.filter(company_name=companyname,sub_company_name=subcompany)
        serializer = sub_company_onbording_payment_serializer(db_data,many=True)
        return Response(serializer.data)

class get_ban_onboarding_payment_details(APIView):
    def get(self,request):
        data = request.data
        Companyname = data.get("Companyname")
        subcompany = data.get("subcompamyname")
        vendor = data.get("vendorname")
        db_data = ban_onboarding_payment.objects.filter(Company = Companyname,Sub_Company=subcompany,Vendor_Name=vendor)
        serializer = ban_onbording_payment_serializer(db_data,many=True)
        return Response(serializer.data)
    


    




            
