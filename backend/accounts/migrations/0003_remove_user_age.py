# Generated by Django 3.2.13 on 2022-11-15 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
