# Generated by Django 4.1.7 on 2023-02-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_cpg', models.FileField(upload_to='')),
                ('file_dbf', models.FileField(upload_to='')),
                ('file_prj', models.FileField(upload_to='')),
                ('file_shp', models.FileField(upload_to='')),
                ('file_shx', models.FileField(upload_to='')),
                ('file_version', models.FileField(upload_to='')),
            ],
        ),
    ]
