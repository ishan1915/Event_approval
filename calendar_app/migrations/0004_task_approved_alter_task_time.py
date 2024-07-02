# Generated by Django 5.0.6 on 2024-06-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_rename_dropdown_field_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.CharField(choices=[('6:00 AM', '6:00AM'), ('7:00 AM', '7:00AM'), ('8:00 AM', '8:00AM'), ('9:00 AM', '9:00AM'), ('10:00 AM', '10:00AM'), ('11:00 AM', '11:00AM'), ('12:00 PM', '12:00PM'), ('1:00 PM', '1:00PM'), ('2:00 PM', '2:00PM'), ('3:00 PM', '3:00PM'), ('4:00 PM', '4:00PM'), ('5:00 PM', '5:00PM'), ('6:00 PM', '6:00PM'), ('7:00 PM', '7:00PM'), ('8:00 PM', '8:00PM'), ('9:00 PM', '9:00PM')], max_length=20),
        ),
    ]
