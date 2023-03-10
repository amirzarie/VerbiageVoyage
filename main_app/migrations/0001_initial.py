# Generated by Django 4.1.7 on 2023-03-10 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Verbiage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('definition', models.TextField(max_length=250)),
                ('facts', models.ManyToManyField(to='main_app.fact')),
            ],
        ),
        migrations.CreateModel(
            name='Etymology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('example', models.TextField(max_length=250)),
                ('verbiage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.verbiage')),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
    ]
