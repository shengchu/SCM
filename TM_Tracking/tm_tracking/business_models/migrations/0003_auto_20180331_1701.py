# Generated by Django 2.0.3 on 2018-03-31 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_models', '0002_auto_20180331_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
