# Generated by Django 3.1.4 on 2023-11-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_alter_mark_mark_name_alter_model_body_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='body_type',
        ),
        migrations.RemoveField(
            model_name='model',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='model',
            name='modification',
        ),
        migrations.RemoveField(
            model_name='model',
            name='years',
        ),
        migrations.AlterField(
            model_name='mark',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='model',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
