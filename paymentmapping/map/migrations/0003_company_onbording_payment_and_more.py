# Generated by Django 5.0.1 on 2024-05-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_ban_onboarding_payment_account_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_onbording_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, default='', max_length=255)),
                ('company_address', models.TextField(blank=True, default='', max_length=255)),
                ('company_city', models.TextField(blank=True, default='', max_length=255)),
                ('company_state', models.TextField(blank=True, default='', max_length=255)),
                ('company_zip', models.TextField(blank=True, default='', max_length=255)),
                ('company_tax_id', models.CharField(blank=True, default='', max_length=255)),
                ('company_email', models.CharField(blank=True, default='', max_length=255)),
                ('company_phone', models.CharField(blank=True, default='', max_length=255)),
                ('dm_first_name', models.CharField(blank=True, default='', max_length=255)),
                ('dm_last_name', models.CharField(blank=True, default='', max_length=255)),
                ('dm_email', models.CharField(blank=True, default='', max_length=255)),
                ('dm_phone', models.CharField(blank=True, default='', max_length=255)),
                ('payment_frequency', models.CharField(blank=True, default='', max_length=255)),
                ('weekdays', models.JSONField(null=True)),
                ('week', models.CharField(blank=True, default='', max_length=255)),
                ('date', models.CharField(blank=True, default='', max_length=255)),
                ('vendor_list', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='sub_company_onbording_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, default='', max_length=255)),
                ('sub_company_name', models.CharField(blank=True, default='', max_length=255)),
                ('sub_company_tax_id', models.CharField(blank=True, default='', max_length=255)),
                ('sub_company_email', models.CharField(blank=True, default='', max_length=255)),
                ('sub_company_address', models.TextField(blank=True, default='', max_length=255)),
                ('sub_company_phone', models.CharField(blank=True, default='', max_length=255)),
                ('sub_company_city', models.TextField(blank=True, default='', max_length=255)),
                ('sub_company_state', models.TextField(blank=True, default='', max_length=255)),
                ('sub_company_zip', models.TextField(blank=True, default='', max_length=255)),
                ('dm_first_name', models.CharField(blank=True, default='', max_length=255)),
                ('dm_last_name', models.CharField(blank=True, default='', max_length=255)),
                ('dm_email', models.CharField(blank=True, default='', max_length=255)),
                ('dm_phone', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_onbording_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
    ]
