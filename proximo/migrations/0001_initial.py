# Generated by Django 4.1.5 on 2023-08-04 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=256)),
                ('start_date', models.DateTimeField(default=None)),
                ('end_date', models.DateTimeField(default=None)),
                ('total_cost', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=256)),
                ('task_desc', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('contributor', models.JSONField(blank=True, default=list, null=True)),
                ('start_date', models.DateTimeField(default=None)),
                ('end_date', models.DateTimeField(default=None)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proximo.project')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proximo.project')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
