# Generated by Django 5.0.1 on 2024-05-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ban_onboarding_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Number', models.CharField(default='NA', max_length=100)),
                ('Remmitance_Address', models.CharField(default='NA', max_length=100)),
                ('Remmitance_City', models.CharField(default='NA', max_length=100)),
                ('Remmitance_State', models.CharField(default='NA', max_length=100)),
                ('Remmitance_Zip', models.CharField(default='NA', max_length=100)),
                ('Remmitance_Country', models.CharField(default='NA', max_length=100)),
                ('Payment_Mode', models.CharField(default='NA', max_length=100)),
                ('URL', models.CharField(default='NA', max_length=100)),
                ('Username', models.CharField(default='NA', max_length=100)),
                ('Password', models.CharField(default='NA', max_length=100)),
                ('Vendor_Name', models.CharField(default='NA', max_length=100)),
                ('Bank_Name', models.CharField(default='NA', max_length=100)),
                ('Bank_Account_Number', models.CharField(default='NA', max_length=100)),
                ('Bank_Routing_Number', models.CharField(default='NA', max_length=100)),
                ('Bank_Account_Type', models.CharField(default='NA', max_length=100)),
                ('Auto_Pay', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Column_mapping_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columns', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MappingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Number', models.CharField(default='NA', max_length=100)),
                ('Remmitance_Address', models.CharField(default='NA', max_length=100)),
                ('Remmitance_City', models.CharField(default='NA', max_length=100)),
                ('Remmitance_State', models.CharField(default='NA', max_length=100)),
                ('Remmitance_Zip', models.CharField(default='NA', max_length=100)),
                ('Remmitance_Country', models.CharField(default='NA', max_length=100)),
                ('Payment_Mode', models.CharField(default='NA', max_length=100)),
                ('URL', models.CharField(default='NA', max_length=100)),
                ('Username', models.CharField(default='NA', max_length=100)),
                ('Password', models.CharField(default='NA', max_length=100)),
                ('Vendor_Name', models.CharField(default='NA', max_length=100)),
                ('Bank_Name', models.CharField(default='NA', max_length=100)),
                ('Bank_Account_Number', models.CharField(default='NA', max_length=100)),
                ('Bank_Routing_Number', models.CharField(default='NA', max_length=100)),
                ('Bank_Account_Type', models.CharField(default='NA', max_length=100)),
                ('Auto_Pay', models.CharField(default='NA', max_length=100)),
            ],
        ),
    ]
