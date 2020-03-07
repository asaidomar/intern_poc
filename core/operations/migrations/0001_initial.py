# Generated by Django 3.0.4 on 2020-03-06 16:10
# noqa
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('description', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('number', models.CharField(max_length=255, unique=True)),
                ('emit_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('number', models.CharField(max_length=255, unique=True)),
                ('emit_date', models.DateField()),
                ('days_delays', models.IntegerField(default=60)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Lettering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('credit_amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('debit_amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('operation_type', models.CharField(choices=[('invoice', 'Facture'), ('misc', 'Facture'), ('payment', 'Paiement'), ('credit', 'Avoir')], max_length=255)),
                ('credit_amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('debit_amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('contract_number', models.CharField(max_length=255)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='operations', to='accounts.Account')),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Action')),
                ('credit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Credit')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Invoice')),
                ('lettering', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Lettering')),
                ('misc_operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Misc')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('cash', 'Comptant'), ('credit_cart', 'Carte de credit'), ('cheque', 'Cheque'), ('virement', 'Virement'), ('autre', 'Autre')], max_length=250)),
                ('payment_date', models.DateField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Unpaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('debit_amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Invoice')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Member')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='operations.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='OperationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('entry', models.TextField()),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Operation')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Member')),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Payment'),
        ),
        migrations.AddField(
            model_name='operation',
            name='recovery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Recovery'),
        ),
        migrations.CreateModel(
            name='InvoiceDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='operations.Invoice')),
            ],
        ),
    ]
