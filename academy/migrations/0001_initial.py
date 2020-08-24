# Generated by Django 3.1 on 2020-08-24 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField(default='')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Сandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('habitat_planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.planet')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('grade', models.CharField(choices=[('grand-master', 'Grand-Master'), ('master', 'Master'), ('knight', 'Knight'), ('padawan', 'Padawan')], max_length=25)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.planet')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
