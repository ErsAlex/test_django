# Generated by Django 4.2.7 on 2023-11-17 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=60)),
                ('modification', models.CharField(max_length=60, null=True)),
                ('body_type', models.CharField(max_length=50, null=True)),
                ('years', models.CharField(max_length=20, null=True)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_models', to='parser.mark')),
            ],
        ),
    ]