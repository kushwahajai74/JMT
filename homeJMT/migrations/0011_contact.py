# Generated by Django 4.0.6 on 2022-07-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeJMT', '0010_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('query', models.TextField()),
            ],
        ),
    ]
