# Generated by Django 3.0.7 on 2020-08-30 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0017_auto_20200830_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='сandidate',
            name='answered_questions',
        ),
    ]