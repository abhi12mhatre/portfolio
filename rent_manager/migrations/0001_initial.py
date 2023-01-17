# Generated by Django 4.1.3 on 2023-01-16 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enitity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, '1RK'), (1, '1BHK'), (2, 'Shop')], default=0)),
                ('number', models.IntegerField(default=0)),
                ('details', models.TextField(blank=True)),
                ('area', models.FloatField(default=0.0)),
                ('rent', models.FloatField(default=0.0)),
                ('deposit', models.FloatField(default=0.0)),
                ('amenities', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TenantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('alternate_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('code', models.CharField(max_length=10)),
                ('pan_card', models.ImageField(upload_to='')),
                ('aadhaar_card', models.ImageField(upload_to='')),
                ('photo', models.ImageField(upload_to='')),
                ('village_address', models.TextField(max_length=1000)),
                ('work_address', models.TextField(max_length=1000)),
                ('pdf', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TenantPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount_due', models.FloatField(default=0.0)),
                ('paid', models.FloatField(default=0.0)),
                ('balance', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_manager.tenantprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_amount', models.IntegerField(default=0)),
                ('deposit_amount', models.IntegerField(default=0)),
                ('agreement_start', models.DateField(blank=True, null=True)),
                ('agreement_end', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_manager.enitity')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent_manager.tenantprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_manager.enitity')),
            ],
        ),
    ]
