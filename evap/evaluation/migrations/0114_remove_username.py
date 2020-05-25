# Generated by Django 3.0.5 on 2020-05-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0113_import_names'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('last_name', 'first_name', 'email'), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
