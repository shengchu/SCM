# Generated by Django 2.0.3 on 2018-03-31 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=10)),
                ('legal_name', models.CharField(max_length=100)),
                ('external_id', models.CharField(max_length=50)),
                ('addresses', models.ManyToManyField(to='business_models.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.TimeField()),
                ('reference_number', models.CharField(max_length=100)),
                ('gross_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gross_volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comments', models.TextField()),
                ('reference_contract', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order_BusinessPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_models.BusinessPartner')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_models.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='businesspartner',
            field=models.ManyToManyField(through='business_models.Order_BusinessPartner', to='business_models.BusinessPartner'),
        ),
        migrations.AddField(
            model_name='order',
            name='cargos',
            field=models.ManyToManyField(to='business_models.Cargo'),
        ),
        migrations.AddField(
            model_name='order',
            name='destination_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_location', to='business_models.Location'),
        ),
        migrations.AddField(
            model_name='order',
            name='source_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_location', to='business_models.Location'),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='business_models.Person'),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='contacts',
            field=models.ManyToManyField(related_name='contacts', to='business_models.Person'),
        ),
    ]