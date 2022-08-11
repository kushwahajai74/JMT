# Generated by Django 4.0.1 on 2022-07-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homeJMT', '0002_delete_carosule'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=250)),
                ('button', models.BooleanField(default=False)),
                ('button_title', models.CharField(max_length=50)),
            ],
        ),
    ]
