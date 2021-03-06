# Generated by Django 2.2.11 on 2020-03-08 16:08

from django.db import migrations, models
import file_crud.helpers.file_crud_helpers
import file_crud.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField()),
                ('explanation', models.CharField(max_length=300)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
