# Generated by Django 4.1.7 on 2023-03-01 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verbiage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('definition', models.TextField(max_length=250)),
            ],
        ),
    ]
