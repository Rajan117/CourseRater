# Generated by Django 2.2.17 on 2021-03-11 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseRate', '0002_auto_20210311_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departments',
            options={'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='modules',
            options={'verbose_name_plural': 'Modules'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name_plural': 'Universities'},
        ),
    ]