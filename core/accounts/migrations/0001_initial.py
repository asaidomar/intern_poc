# Generated by Django 3.0.4 on 2020-03-06 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('iban', models.CharField(max_length=30, unique=True)),
                ('bank', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_address', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_creation_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('tva_number', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('siret', models.CharField(max_length=20, unique=True)),
                ('code_naf', models.CharField(max_length=20)),
                ('activity', models.TextField()),
                ('employee_number', models.IntegerField(default=1)),
                ('creation_date', models.DateField()),
                ('update_date', models.DateField(auto_now=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_created=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.ManyToManyField(blank=True, null=True, related_name='members', to='accounts.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContractDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company'),
        ),
        migrations.CreateModel(
            name='MemberPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.Phone')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_phones', to='accounts.Member')),
            ],
            bases=('accounts.phone',),
        ),
        migrations.CreateModel(
            name='MemberAddress',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.Address')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Member')),
            ],
            bases=('accounts.address',),
        ),
        migrations.CreateModel(
            name='CompanyPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.Phone')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies_phones', to='accounts.Company')),
            ],
            bases=('accounts.phone',),
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.Address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
            bases=('accounts.address',),
        ),
    ]
