# Generated by Django 3.0.7 on 2020-08-30 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0019_auto_20200831_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jedi',
            name='count_padavans',
        ),
    ]