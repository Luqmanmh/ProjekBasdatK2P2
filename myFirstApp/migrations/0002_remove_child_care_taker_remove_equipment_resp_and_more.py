# Generated by Django 4.1.6 on 2023-11-07 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='care_taker',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='resp',
        ),
        migrations.RemoveField(
            model_name='supply',
            name='resp',
        ),
        migrations.RemoveField(
            model_name='toy',
            name='resp',
        ),
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFirstApp.parent'),
        ),
        migrations.AlterField(
            model_name='supply',
            name='supply_amt',
            field=models.CharField(max_length=100),
        ),
    ]
