# Generated by Django 4.1.6 on 2023-11-08 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0004_employee_employee_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='supply',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='toy',
            options={'managed': True},
        ),
    ]
