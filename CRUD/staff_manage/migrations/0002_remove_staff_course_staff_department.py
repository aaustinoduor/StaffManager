# Generated by Django 5.1 on 2024-08-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_manage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='course',
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.CharField(choices=[('ICT', 'ICT'), ('I&C', 'I&C'), ('BSC', 'BSC'), ('AGED', 'AGED')], default='ICT', max_length=20),
            preserve_default=False,
        ),
    ]
