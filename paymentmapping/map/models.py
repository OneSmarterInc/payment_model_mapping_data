from django.db import models
class Column_mapping_data(models.Model):
    columns = models.CharField(max_length=1000)

class MappingData(models.Model):
    Account_Number = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_Address = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_City = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_State = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_Zip = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_Country = models.CharField(max_length=100, default='NA',null=True)
    Payment_Mode = models.CharField(max_length=100, default='NA',null=True)
    URL = models.CharField(max_length=100, default='NA',null=True)
    Username = models.CharField(max_length=100, default='NA',null=True) 
    Password = models.CharField(max_length=100, default='NA',null=True)
    Vendor_Name = models.CharField(max_length=100, default='NA',null=True)
    Bank_Name = models.CharField(max_length=100, default='NA',null=True)
    Bank_Account_Number = models.CharField(max_length=100, default='NA',null=True)
    Bank_Routing_Number = models.CharField(max_length=100, default='NA',null=True)
    Bank_Account_Type = models.CharField(max_length=100, default='NA',null=True)
    Auto_Pay = models.CharField(max_length=100, default='NA',null=True)

class ban_onboarding_payment(models.Model):
    Company = models.CharField(max_length=100, default='NA',null=True)
    Sub_Company = models.CharField(max_length=100, default='NA',null=True)
    Account_Number = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_Address = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_City = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_State = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_Zip = models.CharField(max_length=100, default='NA',null=True)
    Remmitance_Country = models.CharField(max_length=100, default='NA',null=True)
    Payment_Mode = models.CharField(max_length=100, default='NA',null=True)
    URL = models.CharField(max_length=100, default='NA',null=True)
    Username = models.CharField(max_length=100, default='NA',null=True) 
    Password = models.CharField(max_length=100, default='NA',null=True)
    Vendor_Name = models.CharField(max_length=100, default='NA',null=True)
    Bank_Name = models.CharField(max_length=100, default='NA',null=True)
    Bank_Account_Number = models.CharField(max_length=100, default='NA',null=True)
    Bank_Routing_Number = models.CharField(max_length=100, default='NA',null=True)
    Bank_Account_Type = models.CharField(max_length=100, default='NA',null=True)
    Auto_Pay = models.CharField(max_length=100, default='NA',null=True)


class company_onbording_payment(models.Model):
    # Basic Company Details
    company_name = models.CharField(max_length=255,default="", blank=True)
    company_address = models.TextField(max_length=255,default="", blank=True)
    company_city = models.TextField(max_length=255,default="", blank=True)
    company_state = models.TextField(max_length=255,default="", blank=True)
    company_zip = models.TextField(max_length=255,default="", blank=True)
    company_tax_id = models.CharField(max_length=255,default="", blank=True)
    company_email = models.CharField(max_length=255,default="", blank=True)
    company_phone = models.CharField(max_length=255,default="", blank=True)

    # Decision Maker Details
    dm_first_name = models.CharField(max_length=255,default="", blank=True)
    dm_last_name = models.CharField(max_length=255,default="", blank=True)
    dm_email = models.CharField(max_length=255,default="", blank=True)
    dm_phone = models.CharField(max_length=255,default="", blank=True)

    # Payment Details  
    payment_frequency = models.CharField(max_length=255,default="", blank=True)
    weekdays = models.JSONField(null=True)
    week = models.CharField(max_length=255,default="", blank=True)
    date = models.CharField(max_length=255,default="", blank=True)

    # vednor list
    vendor_list= models.JSONField(blank=True)

class sub_company_onbording_payment(models.Model):
    # Basic Company Details
    company_name = models.CharField(max_length=255,default="", blank=True)

    sub_company_name = models.CharField(max_length=255,default="", blank=True)
    sub_company_tax_id = models.CharField(max_length=255,default="", blank=True)
    sub_company_email = models.CharField(max_length=255,default="", blank=True)
    sub_company_address = models.TextField(max_length=255,default="", blank=True)
    sub_company_phone = models.CharField(max_length=255,default="", blank=True)
    sub_company_city = models.TextField(max_length=255,default="", blank=True)
    sub_company_state = models.TextField(max_length=255,default="", blank=True)
    sub_company_zip = models.TextField(max_length=255,default="", blank=True)

    # Decision Maker Details
    dm_first_name = models.CharField(max_length=255,default="", blank=True)
    dm_last_name = models.CharField(max_length=255,default="", blank=True)
    dm_email = models.CharField(max_length=255,default="", blank=True)
    dm_phone = models.CharField(max_length=255,default="", blank=True)



class vendor_onbording_payment(models.Model):
    # Basic vendor Details
    vendor_name = models.CharField(max_length=255,default="", null=True)


